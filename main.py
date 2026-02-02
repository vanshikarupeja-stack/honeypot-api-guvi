import os
from fastapi import FastAPI, HTTPException, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
import re
import uvicorn
from datetime import datetime

app = FastAPI(
    title="Agentic Honey-Pot API",
    description="Scam message intelligence extraction API for GUVI-HCL Hackathon 2026",
    version="1.0.0"
)

# CORS middleware for accessibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key Configuration
VALID_API_KEY = "guvi-hackathon-2026-key"

# Request/Response Models
class ScamRequest(BaseModel):
    message: str = Field(..., description="The scam message text to analyze")
    metadata: Optional[Dict] = Field(default=None, description="Optional metadata")

class IntelligenceResponse(BaseModel):
    scam_type: str
    risk_level: str
    confidence_score: float
    extracted_urls: List[str]
    extracted_emails: List[str]
    extracted_phones: List[str]
    extracted_crypto_addresses: List[str]
    indicators: List[str]
    analysis: str
    timestamp: str

# Intelligence Extraction Functions
class ScamAnalyzer:
    
    @staticmethod
    def extract_urls(text: str) -> List[str]:
        """Extract URLs from text"""
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)
        domain_pattern = r'(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
        domains = re.findall(domain_pattern, text)
        return list(set(urls + [d for d in domains if d not in urls]))
    
    @staticmethod
    def extract_emails(text: str) -> List[str]:
        """Extract email addresses from text"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return list(set(re.findall(email_pattern, text)))
    
    @staticmethod
    def extract_phones(text: str) -> List[str]:
        """Extract phone numbers from text"""
        patterns = [
            r'\+?1?\d{9,15}',
            r'\(\d{3}\)\s*\d{3}[-.\s]?\d{4}',
            r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}',
        ]
        phones = []
        for pattern in patterns:
            phones.extend(re.findall(pattern, text))
        return list(set(phones))
    
    @staticmethod
    def extract_crypto_addresses(text: str) -> List[str]:
        """Extract cryptocurrency wallet addresses"""
        btc_pattern = r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b'
        eth_pattern = r'\b0x[a-fA-F0-9]{40}\b'
        
        crypto_addresses = []
        crypto_addresses.extend(re.findall(btc_pattern, text))
        crypto_addresses.extend(re.findall(eth_pattern, text))
        return list(set(crypto_addresses))
    
    @staticmethod
    def detect_scam_indicators(text: str) -> List[str]:
        """Detect common scam indicators"""
        indicators = []
        text_lower = text.lower()
        
        urgency_words = ['urgent', 'immediately', 'act now', 'limited time', 'expire', 'deadline']
        if any(word in text_lower for word in urgency_words):
            indicators.append('urgency_tactics')
        
        money_words = ['won', 'prize', 'lottery', 'inheritance', 'million', 'reward', 'refund', 'claim']
        if any(word in text_lower for word in money_words):
            indicators.append('too_good_to_be_true')
        
        authority_words = ['bank', 'irs', 'government', 'police', 'tax', 'social security', 'paypal', 'amazon']
        if any(word in text_lower for word in authority_words):
            indicators.append('authority_impersonation')
        
        info_words = ['social security', 'ssn', 'password', 'pin', 'account number', 'credit card', 'verify']
        if any(word in text_lower for word in info_words):
            indicators.append('personal_info_request')
        
        threat_words = ['suspend', 'block', 'locked', 'arrest', 'legal action', 'lawsuit']
        if any(word in text_lower for word in threat_words):
            indicators.append('threatening_language')
        
        if text.count('!!!') > 0 or text.count('???') > 0:
            indicators.append('excessive_punctuation')
        
        if 'click here' in text_lower or 'click this link' in text_lower:
            indicators.append('suspicious_link')
        
        payment_words = ['send money', 'wire transfer', 'gift card', 'bitcoin', 'cryptocurrency', 'paypal']
        if any(word in text_lower for word in payment_words):
            indicators.append('payment_request')
        
        common_misspellings = ['accont', 'verfiy', 'securty', 'imediately', 'importnt']
        if any(word in text_lower for word in common_misspellings):
            indicators.append('spelling_errors')
        
        return indicators
    
    @staticmethod
    def classify_scam_type(text: str, indicators: List[str]) -> str:
        """Classify the type of scam"""
        text_lower = text.lower()
        
        if 'verify' in text_lower or 'confirm' in text_lower or 'account' in text_lower:
            return 'phishing'
        
        if 'won' in text_lower or 'lottery' in text_lower or 'prize' in text_lower:
            return 'lottery_scam'
        
        if 'love' in text_lower or 'dating' in text_lower or 'relationship' in text_lower:
            return 'romance_scam'
        
        if 'invest' in text_lower or 'profit' in text_lower or 'returns' in text_lower:
            return 'investment_scam'
        
        if 'virus' in text_lower or 'infected' in text_lower or 'tech support' in text_lower:
            return 'tech_support_scam'
        
        if 'donate' in text_lower or 'charity' in text_lower or 'help' in text_lower:
            return 'charity_scam'
        
        if 'inherit' in text_lower or 'estate' in text_lower or 'deceased' in text_lower:
            return 'inheritance_scam'
        
        if 'tax' in text_lower or 'irs' in text_lower or 'refund' in text_lower:
            return 'tax_scam'
        
        if 'job' in text_lower or 'hiring' in text_lower or 'employment' in text_lower:
            return 'job_scam'
        
        if 'bitcoin' in text_lower or 'crypto' in text_lower or 'ethereum' in text_lower:
            return 'crypto_scam'
        
        return 'general_scam'
    
    @staticmethod
    def calculate_risk_level(indicators: List[str], has_urls: bool, has_payment: bool) -> tuple:
        """Calculate risk level and confidence score"""
        score = 0
        
        score += len(indicators) * 10
        
        if has_urls:
            score += 15
        if has_payment:
            score += 20
        if 'personal_info_request' in indicators:
            score += 25
        if 'threatening_language' in indicators:
            score += 20
        
        confidence_score = min(score, 100) / 100.0
        
        if confidence_score >= 0.7:
            risk_level = 'critical'
        elif confidence_score >= 0.5:
            risk_level = 'high'
        elif confidence_score >= 0.3:
            risk_level = 'medium'
        else:
            risk_level = 'low'
        
        return risk_level, confidence_score
    
    @classmethod
    def analyze(cls, message: str) -> Dict:
        """Main analysis function"""
        urls = cls.extract_urls(message)
        emails = cls.extract_emails(message)
        phones = cls.extract_phones(message)
        crypto_addresses = cls.extract_crypto_addresses(message)
        indicators = cls.detect_scam_indicators(message)
        
        scam_type = cls.classify_scam_type(message, indicators)
        
        has_payment = 'payment_request' in indicators
        risk_level, confidence_score = cls.calculate_risk_level(
            indicators, 
            len(urls) > 0, 
            has_payment
        )
        
        analysis = cls.generate_analysis(scam_type, indicators, urls, emails, phones, crypto_addresses)
        
        return {
            'scam_type': scam_type,
            'risk_level': risk_level,
            'confidence_score': round(confidence_score, 2),
            'extracted_urls': urls,
            'extracted_emails': emails,
            'extracted_phones': phones,
            'extracted_crypto_addresses': crypto_addresses,
            'indicators': indicators,
            'analysis': analysis,
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }
    
    @staticmethod
    def generate_analysis(scam_type: str, indicators: List[str], urls: List[str], 
                         emails: List[str], phones: List[str], crypto: List[str]) -> str:
        """Generate human-readable analysis"""
        analysis_parts = []
        
        analysis_parts.append(f"This message appears to be a {scam_type.replace('_', ' ')}.")
        
        if indicators:
            analysis_parts.append(f"Detected {len(indicators)} suspicious indicator(s): {', '.join(indicators[:3])}.")
        
        if urls:
            analysis_parts.append(f"Contains {len(urls)} suspicious URL(s).")
        
        if emails:
            analysis_parts.append(f"Found {len(emails)} email address(es).")
        
        if phones:
            analysis_parts.append(f"Found {len(phones)} phone number(s).")
        
        if crypto:
            analysis_parts.append(f"Contains {len(crypto)} cryptocurrency address(es) - high risk of financial scam.")
        
        if 'personal_info_request' in indicators:
            analysis_parts.append("WARNING: Requests personal/financial information.")
        
        return " ".join(analysis_parts)


# API Endpoints
@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "service": "Agentic Honey-Pot API",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "uptime": "operational",
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    }

@app.post("/api/honeypot", response_model=IntelligenceResponse)
async def analyze_scam(
    request: ScamRequest,
    x_api_key: str = Header(..., description="API Key for authentication")
):
    """
    Main endpoint for scam message analysis
    """
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    if not request.message or len(request.message.strip()) == 0:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    try:
        analysis_result = ScamAnalyzer.analyze(request.message)
        return IntelligenceResponse(**analysis_result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/analyze")
async def analyze_alternative(
    request: ScamRequest,
    x_api_key: str = Header(..., description="API Key for authentication")
):
    """Alternative endpoint (same functionality)"""
    return await analyze_scam(request, x_api_key)

if __name__ == "__main__":
    # Support both local and cloud deployment
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
