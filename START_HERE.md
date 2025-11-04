# 🚀 START HERE - Quick Setup Guide

## ⚠️ You're seeing an import error because dependencies aren't installed yet!

Follow these simple steps to get started:

---

## 📋 Step 1: Install Dependencies

### Option A: Using Batch File (Easiest)
1. **Double-click** `install_dependencies.bat`
2. Wait for installation to complete (2-3 minutes)
3. Press any key when done

### Option B: Using Command Prompt
1. Open **Command Prompt** in this folder
2. Run these commands:
```bash
myenv\Scripts\activate
pip install -r requirements.txt
```

### Option C: Manual Installation
1. Open **Command Prompt** in this folder
2. Run these commands one by one:
```bash
myenv\Scripts\activate
pip install streamlit
pip install nsepython
pip install pandas
pip install numpy
pip install scikit-learn
pip install plotly
pip install ta
pip install requests
pip install beautifulsoup4
pip install yfinance
```

---

## 📋 Step 2: Verify Installation

Run the test script:
```bash
myenv\Scripts\activate
python test_installation.py
```

You should see all green checkmarks ✓

---

## 📋 Step 3: Run the App

### Option A: Using Batch File
Double-click `QUICKSTART.bat`

### Option B: Using Command Prompt
```bash
myenv\Scripts\activate
streamlit run streamlit_app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 🔧 Troubleshooting

### Error: "pip is not recognized"
**Solution:**
```bash
python -m pip install --upgrade pip
```

### Error: "streamlit is not recognized"
**Solution:** Make sure virtual environment is activated
```bash
myenv\Scripts\activate
pip install streamlit
```

### Error: "nsepython import failed"
**Solution:**
```bash
myenv\Scripts\activate
pip install nsepython
```

### Error: "plotly import failed" (Your current error)
**Solution:**
```bash
myenv\Scripts\activate
pip install plotly
```

---

## ✅ Quick Fix for Your Current Error

Open **Command Prompt** in this folder and run:

```bash
myenv\Scripts\activate
pip install plotly pandas numpy scikit-learn streamlit nsepython
streamlit run streamlit_app.py
```

---

## 📞 Need Help?

1. Make sure you're in the correct folder: `E:\Personal\StockStrategyPython\GannSetup`
2. Make sure virtual environment exists: Check if `myenv` folder is present
3. Make sure you have internet connection (needed to download packages)
4. Try running `install_dependencies.bat` - it installs everything automatically

---

## 🎯 What to Expect

After successful installation:
1. The Streamlit app will open in your browser
2. You'll see 4 tabs: Scanner, Trend Calculator, Stock Details, Settings
3. You can scan 200+ NSE stocks for buy/sell signals
4. You can use the Trend Calculator (your original feature)

---

## ⏱️ Time Required

- **Installation**: 2-3 minutes
- **First Run**: 30 seconds
- **Full Stock Scan**: 2-3 minutes (200 stocks)

---

## 🚀 Ready? Let's Go!

**Run this command now:**

```bash
install_dependencies.bat
```

Then run:

```bash
QUICKSTART.bat
```

**That's it! You're done! 🎉**

