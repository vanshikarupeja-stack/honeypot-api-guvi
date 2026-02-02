# Agentic Honey-Pot API
## GUVI-HCL Hackathon 2026

A production-ready API for detecting and analyzing scam messages with intelligent risk assessment.

---

## 🧪 Test Your API

```bash
# Health check
curl https://YOUR-URL.com/health

# Test scam detection
curl -X POST https://YOUR-URL.com/api/honeypot \
  -H "x-api-key: guvi-hackathon-2026-key" \
  -H "Content-Type: application/json" \
  -d '{"message": "URGENT! Your account will be closed. Click here."}'
```

---

## ✨ Features

- **10+ Scam Types**: Phishing, lottery, tech support, romance, investment, etc.
- **Intelligence Extraction**: URLs, emails, phones, crypto addresses
- **Risk Assessment**: Automatic scoring (critical/high/medium/low)
- **9+ Indicators**: Urgency, threats, personal info requests, etc.
- **Fast**: <100ms response time
- **Secure**: API key authentication

---

## 📊 API Endpoints

### `GET /health`
Health check endpoint

### `POST /api/honeypot`
Main scam analysis endpoint

**Headers:**
- `x-api-key: guvi-hackathon-2026-key`
- `Content-Type: application/json`

**Request:**
```json
{
  "message": "Your scam message here"
}
```

**Response:**
```json
{
  "scam_type": "phishing",
  "risk_level": "high",
  "confidence_score": 0.85,
  "extracted_urls": ["http://fake-site.com"],
  "extracted_emails": [],
  "extracted_phones": [],
  "extracted_crypto_addresses": [],
  "indicators": ["urgency_tactics", "suspicious_link"],
  "analysis": "This message appears to be a phishing scam...",
  "timestamp": "2026-02-02T14:30:00Z"
}
```

---

## 📚 Files Included

- `main.py` - Core API application
- `requirements.txt` - Python dependencies
- `render.yaml` - Render.com config (auto-deploy)
- `vercel.json` - Vercel config
- `Procfile` - Heroku config
- `runtime.txt` - Python version
- `DEPLOY_NOW.md` - Detailed deployment guide

---



**Built for GUVI-HCL Hackathon 2026** 🏆
