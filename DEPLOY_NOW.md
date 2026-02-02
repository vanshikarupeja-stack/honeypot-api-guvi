# 🚀 DEPLOY YOUR HONEY-POT API - GET A CLEAN URL

## ⚡ FASTEST: Deploy to Render.com (10 minutes)

### Step 1: Prepare Your Files
You already have everything you need! Just these 4 files:
- `main.py` ✓
- `requirements.txt` ✓
- `render.yaml` ✓
- `runtime.txt` ✓

### Step 2: Push to GitHub

```bash
# Navigate to your project folder
cd honeypot_api

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Honey-Pot API for GUVI Hackathon"

# Create a new repo on GitHub (https://github.com/new)
# Name it: honeypot-api-guvi

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/honeypot-api-guvi.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render

1. **Go to Render**: https://render.com
2. **Sign Up** (free) - Use GitHub to sign up
3. **New Web Service**: Click "New +" → "Web Service"
4. **Connect Repository**: 
   - Click "Connect account" if needed
   - Select your `honeypot-api-guvi` repository
5. **Render Auto-Detects Everything!** (because of render.yaml)
6. **Click "Create Web Service"**
7. **Wait 2-3 minutes** for deployment

### Step 4: Get Your Clean URL

After deployment completes, you'll see:
```
✓ Live at: https://honeypot-api-guvi.onrender.com
```

**This is your clean, professional URL!** No "manus" in it! 🎉

---

## ⚡ ALTERNATIVE: Deploy to Railway.app (10 minutes)

### Step 1: Push to GitHub (same as above)

### Step 2: Deploy on Railway

1. **Go to Railway**: https://railway.app
2. **Sign Up** with GitHub (free)
3. **New Project** → "Deploy from GitHub repo"
4. **Select** your `honeypot-api-guvi` repository
5. **Railway auto-detects Python** and deploys
6. **Add Domain**: 
   - Click on your service
   - Go to "Settings" → "Networking"
   - Click "Generate Domain"

### Your Clean URL:
```
✓ Live at: https://honeypot-api-guvi.up.railway.app
```

---

## ⚡ SUPER FAST: Deploy to Vercel (5 minutes)

### Step 1: Create vercel.json

Already included! Just use these files.

### Step 2: Deploy

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd honeypot_api
vercel --prod
```

Follow the prompts and you'll get:
```
✓ Live at: https://honeypot-api-guvi.vercel.app
```

---

## 🧪 Test Your Deployed API

### Test Health Endpoint:
```bash
curl https://YOUR-DEPLOYED-URL.com/health
```

### Test Main Endpoint:
```bash
curl -X POST https://YOUR-DEPLOYED-URL.com/api/honeypot \
  -H "x-api-key: guvi-hackathon-2026-key" \
  -H "Content-Type: application/json" \
  -d '{"message": "Congratulations! You won $1,000,000!"}'
```

Expected response: JSON with scam analysis ✓

---

## 📝 What to Submit to Hackathon

After deployment:

**Deployed URL**: `https://honeypot-api-guvi.onrender.com` (or your URL)  
**API KEY**: `guvi-hackathon-2026-key`

---

## ❓ Which Platform Should I Choose?

| Platform | Pros | Best For |
|----------|------|----------|
| **Render** | ✓ Most reliable<br>✓ Auto-scaling<br>✓ Zero config | **Recommended** |
| **Railway** | ✓ Never sleeps<br>✓ Fast deploys<br>✓ Good free tier | Great alternative |
| **Vercel** | ✓ Super fast<br>✓ Edge network<br>✓ CLI deploy | Quick testing |

**My recommendation: Use Render.com** - It's the most reliable for hackathons!

---

## 🆘 Troubleshooting

### "Port binding failed"
- Solution: Already fixed! The code uses `PORT` environment variable

### "Deployment taking too long"
- Normal for first deploy (3-5 min)
- Check logs for errors

### "Can't connect to GitHub"
- Make sure repo is public
- Re-authorize Render/Railway in GitHub settings

### "API not responding"
- Wait 30 seconds after first deployment
- Free tiers may sleep - first request wakes it up

---

## ✅ Deployment Checklist

- [ ] All 4 files in folder (`main.py`, `requirements.txt`, `render.yaml`, `runtime.txt`)
- [ ] Pushed to GitHub
- [ ] Deployed on Render/Railway/Vercel
- [ ] Got clean URL (no "manus"!)
- [ ] Tested `/health` endpoint
- [ ] Tested `/api/honeypot` endpoint
- [ ] Ready to submit!

---

**🎯 Your new URL will look like:**
- `https://honeypot-api-guvi.onrender.com` ✓
- `https://honeypot-api-guvi.up.railway.app` ✓
- `https://honeypot-api-guvi.vercel.app` ✓

**No more "manus" URLs!** 🎉

---

*Last updated: February 2, 2026*
