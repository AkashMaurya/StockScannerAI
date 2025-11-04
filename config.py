"""
Configuration file for NSE Stock Scanner
Customize these settings according to your preferences
"""

# ============================================================================
# SCANNER SETTINGS
# ============================================================================

# Rate limiting (seconds between API calls)
API_DELAY = 0.1

# Default scan type
DEFAULT_SCAN_TYPE = "intraday"  # Options: "intraday", "delivery", "swing"

# Default risk level
DEFAULT_RISK_LEVEL = "medium"  # Options: "low", "medium", "high"

# Auto-refresh interval (seconds)
AUTO_REFRESH_INTERVAL = 60

# ============================================================================
# TECHNICAL INDICATOR SETTINGS
# ============================================================================

# RSI Settings
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
RSI_PERIOD = 14

# Moving Average Settings
MA_SHORT_PERIOD = 20
MA_LONG_PERIOD = 50

# ATR Settings
ATR_PERIOD = 14

# Gann Trend Calculator
GANN_CONSTANT = 0.45

# ============================================================================
# TRADING SIGNAL SETTINGS
# ============================================================================

# Signal thresholds (0-100)
BUY_THRESHOLD = 60
SELL_THRESHOLD = 60
HOLD_THRESHOLD = 50

# Signal weights (must sum to 100)
SIGNAL_WEIGHTS = {
    'price_change': 20,
    'rsi': 30,
    'support_resistance': 25,
    'volume': 15,
    'momentum': 10,
}

# ============================================================================
# RISK MANAGEMENT SETTINGS
# ============================================================================

# Risk per trade (percentage of capital)
RISK_PER_TRADE = {
    'low': 1.0,
    'medium': 2.0,
    'high': 3.0,
}

# ATR multipliers for targets and stop loss
ATR_MULTIPLIERS = {
    'intraday': {
        'target': 1.5,
        'stop_loss': 1.0,
    },
    'delivery': {
        'target': 2.5,
        'stop_loss': 1.2,
    },
    'swing': {
        'target': 3.0,
        'stop_loss': 1.5,
    },
}

# Risk-reward ratio minimum
MIN_RISK_REWARD_RATIO = 1.5

# ============================================================================
# ML MODEL SETTINGS
# ============================================================================

# Model type
ML_MODEL_TYPE = "random_forest"  # Options: "random_forest", "xgboost", "neural_network"

# Random Forest settings
RF_N_ESTIMATORS = 100
RF_MAX_DEPTH = 10
RF_RANDOM_STATE = 42

# Confidence threshold for signals
ML_CONFIDENCE_THRESHOLD = 0.75

# Feature importance threshold
FEATURE_IMPORTANCE_THRESHOLD = 0.05

# ============================================================================
# DATA SETTINGS
# ============================================================================

# Cache duration (seconds)
CACHE_DURATION = 300  # 5 minutes

# Historical data period
HISTORICAL_PERIOD = "1mo"  # Options: "1d", "5d", "1mo", "3mo", "6mo", "1y"

# Data source priority
DATA_SOURCE_PRIORITY = ["nsepython", "yfinance"]

# ============================================================================
# UI SETTINGS
# ============================================================================

# Theme colors
THEME_COLORS = {
    'primary': '#3b82f6',
    'success': '#10b981',
    'danger': '#ef4444',
    'warning': '#f59e0b',
    'info': '#06b6d4',
}

# Chart settings
CHART_HEIGHT = 400
CHART_WIDTH = 800

# Table settings
TABLE_PAGE_SIZE = 50
TABLE_HEIGHT = 600

# ============================================================================
# NOTIFICATION SETTINGS
# ============================================================================

# Enable notifications
ENABLE_NOTIFICATIONS = False

# Notification types
NOTIFICATION_TYPES = {
    'buy_signal': True,
    'sell_signal': True,
    'target_reached': True,
    'stop_loss_hit': True,
}

# ============================================================================
# EXPORT SETTINGS
# ============================================================================

# Export format
DEFAULT_EXPORT_FORMAT = "csv"  # Options: "csv", "excel", "json"

# Export filename format
EXPORT_FILENAME_FORMAT = "nse_scanner_{date}_{time}.{format}"

# Include timestamp in export
INCLUDE_TIMESTAMP = True

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

# Enable logging
ENABLE_LOGGING = True

# Log level
LOG_LEVEL = "INFO"  # Options: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"

# Log file
LOG_FILE = "nse_scanner.log"

# Log format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================

# Enable backtesting
ENABLE_BACKTESTING = False

# Backtest period
BACKTEST_PERIOD = "1y"

# Enable paper trading
ENABLE_PAPER_TRADING = False

# Paper trading capital
PAPER_TRADING_CAPITAL = 100000

# Enable alerts
ENABLE_ALERTS = False

# Alert conditions
ALERT_CONDITIONS = {
    'price_change': 5.0,  # Alert if price changes by 5%
    'volume_spike': 2.0,  # Alert if volume is 2x average
    'rsi_extreme': True,  # Alert on RSI < 30 or > 70
}

# ============================================================================
# STOCK LIST CUSTOMIZATION
# ============================================================================

# You can customize the stock list here
# Leave empty to use default list from nse_scanner.py
CUSTOM_STOCK_LIST = []

# Example:
# CUSTOM_STOCK_LIST = [
#     "RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK",
#     "HINDUNILVR", "BHARTIARTL", "ITC", "KOTAKBANK", "LT"
# ]

# Exclude stocks from scanning
EXCLUDE_STOCKS = []

# Example:
# EXCLUDE_STOCKS = ["IDEA", "YESBANK"]

# ============================================================================
# SECTOR CLASSIFICATION
# ============================================================================

SECTOR_MAPPING = {
    'Banking': ['HDFCBANK', 'ICICIBANK', 'SBIN', 'AXISBANK', 'KOTAKBANK', 'INDUSINDBK'],
    'IT': ['TCS', 'INFY', 'WIPRO', 'HCLTECH', 'TECHM', 'LTIM', 'MPHASIS', 'COFORGE'],
    'Auto': ['MARUTI', 'M&M', 'TATAMOTORS', 'EICHERMOT', 'BAJAJ-AUTO', 'HEROMOTOCO'],
    'Pharma': ['SUNPHARMA', 'DRREDDY', 'CIPLA', 'LUPIN', 'DIVISLAB', 'BIOCON'],
    'Energy': ['RELIANCE', 'ONGC', 'BPCL', 'IOC', 'COALINDIA', 'NTPC', 'POWERGRID'],
    'FMCG': ['HINDUNILVR', 'ITC', 'NESTLEIND', 'BRITANNIA', 'DABUR', 'MARICO'],
    'Metals': ['TATASTEEL', 'JSWSTEEL', 'HINDALCO', 'VEDL', 'JINDALSTEL', 'SAIL'],
    'Telecom': ['BHARTIARTL', 'IDEA', 'JIOFIN'],
}

# ============================================================================
# MARKET HOURS (IST)
# ============================================================================

MARKET_OPEN_TIME = "09:15"
MARKET_CLOSE_TIME = "15:30"
PRE_MARKET_OPEN = "09:00"
POST_MARKET_CLOSE = "16:00"

# Trading days
TRADING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# ============================================================================
# API SETTINGS
# ============================================================================

# NSE API settings
NSE_BASE_URL = "https://www.nseindia.com"
NSE_TIMEOUT = 10  # seconds

# User agent for requests
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Request headers
REQUEST_HEADERS = {
    'User-Agent': USER_AGENT,
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
}

# ============================================================================
# DISCLAIMER
# ============================================================================

DISCLAIMER_TEXT = """
⚠️ DISCLAIMER:
This tool is for educational and informational purposes only.
- Not financial advice
- Do your own research before trading
- Stock trading involves substantial risk of loss
- Past performance does not guarantee future results
- Use at your own risk
"""

# Show disclaimer on startup
SHOW_DISCLAIMER = True

