# 📈 NSE Stock Scanner & AI Recommender

A powerful real-time stock scanner for NSE (National Stock Exchange) with AI/ML-powered trading recommendations.

## 🌟 Features

- **Real-time NSE Data**: Fetch live stock prices using `nsepython` library
- **AI-Powered Recommendations**: Machine Learning models for buy/sell signals
- **Beautiful Streamlit UI**: Modern, responsive interface with interactive charts
- **200+ Stocks Coverage**: Scan all major NSE stocks automatically
- **Multiple Trading Modes**: Intraday, Delivery, and Swing Trading
- **Risk Management**: Automatic calculation of entry, target, and stop-loss levels
- **Trend Calculator**: Gann-style trend line calculator
- **Export Results**: Download scan results as CSV

## 📋 Stock List

The scanner monitors 200+ NSE stocks including:
- Banking: HDFCBANK, ICICIBANK, SBIN, AXISBANK, KOTAKBANK, etc.
- IT: TCS, INFOSYS, WIPRO, HCLTECH, TECHM, etc.
- Auto: MARUTI, M&M, TATAMOTORS, EICHERMOT, etc.
- Pharma: SUNPHARMA, DRREDDY, CIPLA, LUPIN, etc.
- Energy: RELIANCE, ONGC, BPCL, IOC, etc.
- And many more...

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Virtual environment (myenv already created)

### Quick Start

1. **Activate Virtual Environment**:
   ```bash
   myenv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run streamlit_app.py
   ```

### Or Use the Batch Script (Windows)
Simply double-click `setup_and_run.bat` to install dependencies and run the app.

## 📊 Usage

### 1. Stock Scanner Tab
- Select scan type (Intraday/Delivery/Swing Trading)
- Choose risk level (Low/Medium/High)
- Click "Start Scanning" to analyze all stocks
- View results in a beautiful table with:
  - Buy/Sell/Hold signals
  - Entry price, Target, and Stop Loss
  - AI confidence score
  - RSI and other indicators
- Download results as CSV

### 2. Trend Calculator Tab
- Enter High and Low values
- Calculate resistance and support levels
- Get next predicted high/low using Gann's formula

### 3. Stock Details Tab
- Select individual stock
- View detailed metrics and charts
- Analyze price movements

### 4. Settings Tab
- Configure scanner parameters
- Adjust ML model settings
- Set auto-refresh intervals

## 🤖 AI/ML Features

The scanner uses Machine Learning algorithms to:
- Analyze technical indicators (RSI, Moving Averages, ATR)
- Identify chart patterns
- Calculate optimal entry/exit points
- Provide confidence scores for each recommendation
- Risk-reward ratio calculation
- Position sizing based on capital and risk tolerance

## 📈 Technical Indicators

- **RSI (Relative Strength Index)**: Momentum indicator
- **Support & Resistance**: Gann-style calculations
- **ATR (Average True Range)**: Volatility measurement
- **Volume Analysis**: Trading volume patterns
- **Price Action**: Candlestick patterns

## 🎯 Trading Signals

### BUY Signal
- RSI < 40 (Oversold)
- Price near support
- Positive momentum
- High volume

### SELL Signal
- RSI > 60 (Overbought)
- Price near resistance
- Negative momentum
- Distribution pattern

### HOLD Signal
- Neutral indicators
- Consolidation phase
- Wait for better opportunity

## ⚙️ Configuration

### Risk Levels
- **Low Risk**: Conservative targets, wider stop-loss
- **Medium Risk**: Balanced approach
- **High Risk**: Aggressive targets, tighter stop-loss

### Scan Types
- **Intraday**: Quick trades, same-day exit
- **Delivery**: Positional trades, 1-5 days
- **Swing Trading**: Medium-term, 5-15 days

## 📁 Project Structure

```
GannSetup/
├── streamlit_app.py      # Main Streamlit application
├── nse_scanner.py        # NSE data fetching and scanning logic
├── ml_engine.py          # Machine Learning recommendation engine
├── app.py                # Original Flask app (legacy)
├── requirements.txt      # Python dependencies
├── setup_and_run.bat     # Windows setup script
├── myenv/                # Virtual environment
└── templates/            # Flask templates (legacy)
```

## 🔧 Dependencies

- **streamlit**: Web UI framework
- **nsepython**: NSE data API
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **scikit-learn**: Machine Learning
- **plotly**: Interactive charts
- **ta**: Technical analysis library

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. 

- **Not Financial Advice**: Do not consider this as financial or investment advice
- **Do Your Research**: Always conduct your own research before trading
- **Risk Warning**: Stock trading involves substantial risk of loss
- **No Guarantees**: Past performance does not guarantee future results
- **Use at Your Own Risk**: The developers are not responsible for any trading losses

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📝 License

This project is for educational purposes only.

## 📞 Support

For issues or questions, please create an issue in the repository.

---

**Happy Trading! 📈💰**

*Remember: The best investment you can make is in yourself. Learn, practice, and trade responsibly.*

