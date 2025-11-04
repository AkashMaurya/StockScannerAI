# 🔧 Troubleshooting Guide - NSE Stock Scanner

## Common Issues and Solutions

### 1. "Failed to fetch stock data. Please try again."

**Cause:** NSE API is unavailable or market is closed.

**Solution:**
- ✅ **App now uses automatic fallback to historical data**
- The app will fetch the last available trading day's data from Yahoo Finance
- You'll see an info message: "Using historical data fallback"
- This is normal and expected when:
  - Market is closed (after 3:30 PM IST on weekdays)
  - Weekends and holidays
  - NSE website is under maintenance
  - Network connectivity issues

**What to do:**
1. Continue using the app normally - historical data is accurate
2. For live data, try during market hours (9:15 AM - 3:30 PM IST, Mon-Fri)
3. Check your internet connection

---

### 2. All Stocks Showing HOLD Signal

**Cause:** ML model not trained yet.

**Solution:**
1. Go to the **sidebar** (left panel)
2. Look for "🤖 AI Model" section
3. Click **"🧠 Train AI Model"** button
4. Wait 2-5 minutes for training to complete
5. You'll see: "✅ Model Trained - Accuracy: XX.X%"
6. Now scan stocks again - you'll get BUY/SELL signals

**Why this happens:**
- Without ML training, the app uses basic rule-based signals
- Rule-based signals are conservative and often show HOLD
- ML model learns from 60-day historical patterns and gives better signals

---

### 3. Low Model Accuracy (<60%)

**Cause:** Market volatility or insufficient training data.

**Solution:**
1. **Retrain the model** - Click "🧠 Train AI Model" again
2. **Wait for better market conditions** - High volatility reduces accuracy
3. **Use higher confidence threshold** - Only trade signals with >70% confidence
4. **Combine with your own analysis** - AI is a tool, not a guarantee

**Expected accuracy:**
- 70-85%: Good model performance ✅
- 60-70%: Acceptable, use with caution ⚠️
- <60%: Retrain or wait for stable market conditions ❌

---

### 4. Charts Not Showing

**Cause:** Historical data not available or yfinance error.

**Solution:**
1. **Check internet connection**
2. **Refresh the page** (F5 or Ctrl+R)
3. **Try a different stock** - Some stocks may have limited data
4. **Check if yfinance is installed:**
   ```bash
   pip install yfinance --upgrade
   ```

---

### 5. App Crashes or Freezes During Training

**Cause:** Memory issues or network timeout.

**Solution:**
1. **Close other applications** to free up memory
2. **Check internet connection** - Training downloads historical data
3. **Restart the app:**
   ```bash
   streamlit run streamlit_app.py
   ```
4. **If problem persists**, reduce training stocks:
   - Edit `streamlit_app.py` line 115
   - Change `training_stocks = st.session_state.scanner.get_stock_list()[:50]`
   - To `training_stocks = st.session_state.scanner.get_stock_list()[:20]`

---

### 6. Search Dropdown Not Working

**Cause:** Browser compatibility or Streamlit version.

**Solution:**
1. **Use a modern browser** (Chrome, Firefox, Edge)
2. **Clear browser cache** (Ctrl+Shift+Delete)
3. **Update Streamlit:**
   ```bash
   pip install streamlit --upgrade
   ```
4. **Refresh the page** (F5)

**How to use search:**
- Click the dropdown
- Start typing any part of the stock name
- Example: Type "REL" to find RELIANCE
- Example: Type "TAT" to find TATA stocks

---

### 7. Confidence Always Shows 50%

**Cause:** ML model not trained.

**Solution:**
1. Train the AI model first (see issue #2 above)
2. After training, confidence will range from 50-100%
3. Higher confidence = More reliable signal

---

### 8. "Module not found" Errors

**Cause:** Missing dependencies.

**Solution:**
Install all required packages:
```bash
pip install streamlit pandas numpy plotly yfinance nsepython scikit-learn
```

Or use requirements file:
```bash
pip install -r requirements.txt
```

---

### 9. Slow Performance During Scanning

**Cause:** Scanning many stocks takes time.

**Expected behavior:**
- Single stock: 2-5 seconds
- Sector (20-30 stocks): 30-60 seconds
- All stocks (200+): 3-5 minutes

**Tips to speed up:**
1. **Use sector filtering** instead of scanning all stocks
2. **Search for specific stocks** when you know what you want
3. **Be patient** - ML analysis takes time for accuracy
4. **Rate limiting is intentional** - Prevents API blocking

---

### 10. Data Seems Outdated

**Cause:** Using historical data fallback.

**Solution:**
1. **Check if market is open** (9:15 AM - 3:30 PM IST, Mon-Fri)
2. **During market hours**, NSE API should provide live data
3. **After market hours**, historical data is expected and normal
4. **Click "🔄 Refresh Data"** in sidebar to update

**Data freshness:**
- Market hours: Live data (real-time)
- After hours: Last trading day's closing data
- Weekends/Holidays: Last trading day's data

---

## Best Practices

### ✅ DO:
1. **Train the ML model before scanning**
2. **Use during market hours for live data**
3. **Focus on high confidence signals (>70%)**
4. **Use stop-loss always**
5. **Combine AI signals with your own analysis**
6. **Start with paper trading to test**
7. **Retrain model weekly with fresh data**

### ❌ DON'T:
1. **Don't trade without training the model first**
2. **Don't ignore low confidence warnings**
3. **Don't trade based on AI alone**
4. **Don't skip stop-loss orders**
5. **Don't expect 100% accuracy**
6. **Don't panic if model accuracy fluctuates**
7. **Don't use real money without testing first**

---

## Getting Help

### Check These First:
1. ✅ Is the ML model trained? (Check sidebar)
2. ✅ Is your internet working?
3. ✅ Are you using the latest version?
4. ✅ Did you install all dependencies?

### Still Having Issues?
1. **Restart the app:**
   ```bash
   Ctrl+C (in terminal)
   streamlit run streamlit_app.py
   ```

2. **Check terminal for error messages**
   - Look for red error text
   - Copy the error message

3. **Clear Streamlit cache:**
   - Click the hamburger menu (☰) in top-right
   - Select "Clear cache"
   - Refresh the page

---

## System Requirements

### Minimum:
- Python 3.8+
- 4GB RAM
- Internet connection
- Modern web browser

### Recommended:
- Python 3.10+
- 8GB RAM
- Stable internet (for data fetching)
- Chrome/Firefox browser

---

## Quick Diagnostic

Run this checklist:

```
[ ] Python version 3.8 or higher?
[ ] All packages installed? (streamlit, pandas, yfinance, etc.)
[ ] Internet connection working?
[ ] ML model trained? (Check sidebar)
[ ] Using modern browser?
[ ] Tried refreshing the page?
[ ] Checked terminal for errors?
```

If all checked and still having issues, restart the app and try again.

---

## Performance Tips

1. **For faster scanning:**
   - Use sector filtering
   - Search specific stocks
   - Scan during off-peak hours

2. **For better accuracy:**
   - Train model with more stocks
   - Retrain weekly
   - Use delivery/swing mode (more reliable than intraday)

3. **For smoother experience:**
   - Close unnecessary browser tabs
   - Use wired internet connection
   - Scan during market hours for live data

---

## Data Sources

- **Live Data:** NSE India (nsepython library)
- **Historical Data:** Yahoo Finance (yfinance library)
- **Fallback:** Automatic switch to historical when live unavailable

**Note:** The app intelligently switches between live and historical data to ensure uninterrupted service.

---

## Version Information

- **App Version:** 2.0 (ML-Powered)
- **ML Model:** Gradient Boosting Classifier
- **Features:** 14 technical indicators
- **Training Data:** 60-day historical OHLCV

---

**Remember:** This is an educational tool. Always do your own research and use proper risk management when trading!

