# 🚀 Deploy NSE Stock Scanner to Render

This guide will help you deploy your NSE Stock Scanner app to Render for free.

---

## 📋 Prerequisites

1. **GitHub Account** - Create one at https://github.com if you don't have
2. **Render Account** - Sign up at https://render.com (free)
3. **Git installed** on your computer

---

## 📁 Files Created for Deployment

The following files have been created in your project:

✅ **render.yaml** - Render service configuration
✅ **requirements.txt** - Python dependencies
✅ **runtime.txt** - Python version specification
✅ **Procfile** - Start command for the app
✅ **packages.txt** - System packages
✅ **.streamlit/config.toml** - Streamlit configuration

---

## 🔧 Step-by-Step Deployment

### **STEP 1: Push Your Code to GitHub**

1. **Open terminal/command prompt** in your project folder:
   ```bash
   cd E:\Personal\StockStrategyPython\GannSetup
   ```

2. **Initialize Git** (if not already done):
   ```bash
   git init
   ```

3. **Add all files:**
   ```bash
   git add .
   ```

4. **Commit your code:**
   ```bash
   git commit -m "Initial commit - NSE Stock Scanner with ML"
   ```

5. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Repository name: `nse-stock-scanner`
   - Make it **Public** (required for Render free tier)
   - Don't initialize with README (you already have files)
   - Click "Create repository"

6. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/nse-stock-scanner.git
   git branch -M main
   git push -u origin main
   ```
   
   Replace `YOUR_USERNAME` with your actual GitHub username.

---

### **STEP 2: Deploy on Render**

1. **Go to Render Dashboard:**
   - Visit https://dashboard.render.com
   - Sign in with your GitHub account (recommended)

2. **Create New Web Service:**
   - Click **"New +"** button (top right)
   - Select **"Web Service"**

3. **Connect Your Repository:**
   - Click **"Connect account"** if not connected
   - Find and select your `nse-stock-scanner` repository
   - Click **"Connect"**

4. **Configure the Service:**
   
   **Basic Settings:**
   - **Name:** `nse-stock-scanner` (or any name you like)
   - **Region:** Choose closest to you (e.g., Singapore for India)
   - **Branch:** `main`
   - **Root Directory:** Leave blank
   - **Runtime:** `Python 3`
   
   **Build & Deploy:**
   - **Build Command:** 
     ```
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```
     streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
     ```
   
   **Plan:**
   - Select **"Free"** plan
   - Note: Free plan has limitations (see below)

5. **Advanced Settings (Optional):**
   - **Environment Variables:** None needed for basic setup
   - **Auto-Deploy:** Keep enabled (deploys on every git push)

6. **Create Web Service:**
   - Click **"Create Web Service"** button
   - Wait 5-10 minutes for deployment

7. **Access Your App:**
   - Once deployed, you'll get a URL like: `https://nse-stock-scanner.onrender.com`
   - Click the URL to open your app

---

## 🎯 Alternative: Deploy Using render.yaml (Easier)

If you want to use the `render.yaml` file I created:

1. **Push code to GitHub** (follow Step 1 above)

2. **Go to Render Dashboard:**
   - Click **"New +"** → **"Blueprint"**
   - Connect your repository
   - Render will automatically detect `render.yaml`
   - Click **"Apply"**
   - Done! 🎉

---

## ⚙️ Render Free Tier Limitations

**What's Included (Free):**
- ✅ 750 hours/month (enough for 24/7 if only one service)
- ✅ 512 MB RAM
- ✅ Shared CPU
- ✅ Custom domain support
- ✅ Auto-deploy from GitHub
- ✅ HTTPS enabled

**Limitations:**
- ⚠️ **Spins down after 15 minutes of inactivity**
- ⚠️ **Cold start takes 30-60 seconds** when accessing after inactivity
- ⚠️ Limited to 512 MB RAM (may affect ML model training)
- ⚠️ Slower performance than paid plans

**Workaround for Spin Down:**
- Use a service like **UptimeRobot** (free) to ping your app every 14 minutes
- This keeps your app always running

---

## 🔍 Troubleshooting Deployment

### Issue 1: Build Failed

**Error:** `Could not find a version that satisfies the requirement...`

**Solution:**
- Check `requirements.txt` has correct package names
- Remove version numbers if causing issues:
  ```
  streamlit
  pandas
  numpy
  ```

### Issue 2: App Crashes on Startup

**Error:** `Application failed to respond`

**Solution:**
- Check the **Logs** in Render dashboard
- Common issue: Port not set correctly
- Ensure start command includes `--server.port=$PORT`

### Issue 3: ML Model Training Fails

**Error:** `Memory limit exceeded`

**Solution:**
- Reduce training stocks in `streamlit_app.py`:
  ```python
  training_stocks = st.session_state.scanner.get_stock_list()[:20]  # Reduced from 50
  ```
- Or upgrade to paid plan ($7/month for 2GB RAM)

### Issue 4: NSE Data Not Loading

**Error:** `Failed to fetch stock data`

**Solution:**
- This is normal - NSE API may block cloud IPs
- App will automatically use historical data fallback
- Users will see: "Using historical data fallback"

### Issue 5: Slow Performance

**Cause:** Free tier has limited resources

**Solution:**
- Use sector filtering instead of scanning all stocks
- Search specific stocks
- Consider upgrading to paid plan for better performance

---

## 📊 Monitoring Your Deployment

### View Logs:
1. Go to Render Dashboard
2. Click on your service
3. Click **"Logs"** tab
4. See real-time logs

### Check Status:
- **Green dot** = Running ✅
- **Yellow dot** = Deploying 🔄
- **Red dot** = Failed ❌

### Metrics:
- View CPU, Memory, and Bandwidth usage
- Available in the **"Metrics"** tab

---

## 🔄 Updating Your Deployed App

**Method 1: Auto-Deploy (Recommended)**
1. Make changes to your code locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Updated features"
   git push
   ```
3. Render automatically deploys the new version
4. Wait 2-5 minutes for deployment

**Method 2: Manual Deploy**
1. Go to Render Dashboard
2. Click on your service
3. Click **"Manual Deploy"** → **"Deploy latest commit"**

---

## 🌐 Custom Domain (Optional)

1. **Buy a domain** (e.g., from Namecheap, GoDaddy)
2. **In Render Dashboard:**
   - Go to your service
   - Click **"Settings"** → **"Custom Domain"**
   - Add your domain (e.g., `stockscanner.yourdomain.com`)
3. **Update DNS records** at your domain registrar:
   - Add CNAME record pointing to your Render URL
4. Wait for DNS propagation (5-30 minutes)

---

## 💡 Tips for Better Performance on Free Tier

1. **Reduce Training Data:**
   - Train with 20-30 stocks instead of 50
   - Reduces memory usage

2. **Use Caching:**
   - Streamlit's `@st.cache_data` is already used
   - Helps reduce repeated calculations

3. **Optimize Scanning:**
   - Encourage users to use sector filtering
   - Single stock search is faster

4. **Keep App Alive:**
   - Use UptimeRobot to ping every 14 minutes
   - Prevents cold starts

5. **Monitor Usage:**
   - Check logs regularly
   - Watch for memory issues

---

## 🚀 Upgrade Options

If you need better performance:

**Render Starter Plan ($7/month):**
- 2 GB RAM (4x more)
- Faster CPU
- No spin down
- Better for ML model training

**Render Standard Plan ($25/month):**
- 4 GB RAM
- Dedicated CPU
- Best performance

---

## 📝 Environment Variables (If Needed)

If you want to add API keys or secrets:

1. **In Render Dashboard:**
   - Go to your service
   - Click **"Environment"** tab
   - Click **"Add Environment Variable"**

2. **Example variables:**
   ```
   SECRET_KEY=your_secret_key
   API_KEY=your_api_key
   ```

3. **Access in code:**
   ```python
   import os
   secret = os.getenv('SECRET_KEY')
   ```

---

## 🎉 Success Checklist

After deployment, verify:

- [ ] App URL is accessible
- [ ] Homepage loads correctly
- [ ] Can search for stocks
- [ ] Can train ML model (may take longer on free tier)
- [ ] Can scan stocks
- [ ] Charts display properly
- [ ] No errors in Render logs

---

## 📞 Getting Help

**Render Documentation:**
- https://render.com/docs

**Render Community:**
- https://community.render.com

**Streamlit Deployment Guide:**
- https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app

---

## 🔐 Security Notes

1. **Don't commit sensitive data:**
   - Use environment variables for secrets
   - Add `.env` to `.gitignore`

2. **Public repository:**
   - Your code will be visible on GitHub
   - Don't include API keys in code

3. **Rate limiting:**
   - NSE API may block excessive requests
   - App has built-in rate limiting (0.1s delay)

---

## 📊 Expected Deployment Timeline

| Step | Time |
|------|------|
| Push to GitHub | 1-2 minutes |
| Create Render service | 2-3 minutes |
| Initial deployment | 5-10 minutes |
| First app load | 30-60 seconds (cold start) |
| **Total** | **~15 minutes** |

---

## 🎯 Quick Start Commands

```bash
# Navigate to project
cd E:\Personal\StockStrategyPython\GannSetup

# Initialize git (if needed)
git init

# Add all files
git add .

# Commit
git commit -m "NSE Stock Scanner - Ready for deployment"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/nse-stock-scanner.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Then go to Render and deploy! 🚀

---

## ✅ Files Checklist

Make sure these files are in your repository:

- [x] `streamlit_app.py` - Main app
- [x] `nse_scanner.py` - Scanner logic
- [x] `ml_engine.py` - ML model
- [x] `config.py` - Configuration
- [x] `requirements.txt` - Dependencies
- [x] `render.yaml` - Render config
- [x] `runtime.txt` - Python version
- [x] `Procfile` - Start command
- [x] `packages.txt` - System packages
- [x] `.streamlit/config.toml` - Streamlit config

---

**You're all set! Follow the steps above to deploy your NSE Stock Scanner to Render.** 🎉📈

**Your app will be live at:** `https://your-app-name.onrender.com`

Good luck with your deployment! 🚀

