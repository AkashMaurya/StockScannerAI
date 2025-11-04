# 🚀 Installation Guide - NSE Stock Scanner

## Step-by-Step Installation

### Method 1: Using Batch Script (Easiest - Windows)

1. **Double-click** `setup_and_run.bat`
2. Wait for installation to complete
3. The app will start automatically in your browser

### Method 2: Manual Installation

#### Step 1: Activate Virtual Environment

Open Command Prompt or PowerShell in the project directory:

```bash
# Windows
myenv\Scripts\activate

# You should see (myenv) in your command prompt
```

#### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (Web UI)
- nsepython (NSE data)
- pandas (Data processing)
- numpy (Numerical operations)
- scikit-learn (Machine Learning)
- plotly (Charts)
- ta (Technical Analysis)
- requests, beautifulsoup4, yfinance

#### Step 3: Run the Application

```bash
streamlit run streamlit_app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

## 🔍 Troubleshooting

### Issue 1: Virtual Environment Not Activating

**Solution:**
```bash
# Create new virtual environment
python -m venv myenv

# Activate it
myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Issue 2: nsepython Installation Error

**Solution:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install nsepython
pip install nsepython
```

### Issue 3: Streamlit Not Found

**Solution:**
```bash
# Make sure virtual environment is activated
myenv\Scripts\activate

# Install streamlit
pip install streamlit

# Verify installation
streamlit --version
```

### Issue 4: Port Already in Use

**Solution:**
```bash
# Run on different port
streamlit run streamlit_app.py --server.port 8502
```

### Issue 5: NSE Data Not Loading

**Possible Causes:**
- Market is closed (NSE operates 9:15 AM - 3:30 PM IST)
- Internet connection issues
- NSE API rate limiting

**Solution:**
- Check your internet connection
- Wait a few minutes and try again
- The scanner has built-in rate limiting (0.1s delay between requests)

## 📱 First Time Usage

1. **Start the App**: Run `streamlit run streamlit_app.py`

2. **Navigate to Scanner Tab**: Click on "🔍 Scanner" tab

3. **Configure Settings**:
   - Select Scan Type: Intraday/Delivery/Swing Trading
   - Choose Risk Level: Low/Medium/High

4. **Start Scanning**: Click "🚀 Start Scanning" button

5. **Wait for Results**: The scanner will fetch data for 200+ stocks (takes 2-3 minutes)

6. **Analyze Results**: 
   - View BUY/SELL/HOLD signals
   - Check entry, target, and stop-loss levels
   - Review AI confidence scores

7. **Download Results**: Click "📥 Download Results as CSV"

## 🎯 Quick Test

To verify everything is working:

1. Activate virtual environment:
   ```bash
   myenv\Scripts\activate
   ```

2. Test nsepython:
   ```bash
   python -c "from nsepython import *; print(nse_quote_ltp('RELIANCE'))"
   ```
   
   Should print Reliance stock price.

3. Run Streamlit:
   ```bash
   streamlit run streamlit_app.py
   ```
   
   Should open browser with the app.

## 💡 Tips

1. **Market Hours**: NSE operates Mon-Fri, 9:15 AM - 3:30 PM IST
2. **Scanning Time**: Full scan takes 2-3 minutes for 200 stocks
3. **Rate Limiting**: Built-in 0.1s delay to avoid API blocks
4. **Data Refresh**: Use "🔄 Refresh Data" button in sidebar
5. **Export Data**: Always download results for record-keeping

## 🔐 Security Notes

- No API keys required for nsepython
- All data is fetched from public NSE APIs
- No personal data is collected or stored
- Run locally on your machine

## 📊 System Requirements

- **OS**: Windows 10/11, macOS, Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Internet**: Stable connection required
- **Browser**: Chrome, Firefox, Edge, Safari

## 🆘 Getting Help

If you encounter issues:

1. Check this troubleshooting guide
2. Verify all dependencies are installed
3. Ensure virtual environment is activated
4. Check internet connection
5. Verify market hours (for live data)

## 📝 Next Steps

After successful installation:

1. Read the README.md for feature details
2. Explore the Trend Calculator tab
3. Try scanning with different risk levels
4. Experiment with different scan types
5. Review the Settings tab for customization

---

**Happy Trading! 📈**

