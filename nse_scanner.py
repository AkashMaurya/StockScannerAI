import pandas as pd
import numpy as np
from nsepython import *
import yfinance as yf
import time
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class NSEScanner:
    """NSE Stock Scanner using nsepython library"""

    def __init__(self):
        self.stock_list = [
            "ABB", "ADANIENT", "ADANIGREEN", "ADANIPORTS", "ADANITRANS", "APOLLOHOSP",
            "ASIANPAINT", "ASTRAL", "ATUL", "AXISBANK", "BAJAJFINSV", "BAJFINANCE",
            "BALKRISIND", "BANDHANBNK", "BANKBARODA", "BERGEPAINT", "BHARATFORG",
            "BHARTIARTL", "BHEL", "BIOCON", "BOSCHLTD", "BPCL", "BRITANNIA", "BSE",
            "CANBK", "CHOLAFIN", "CIPLA", "COALINDIA", "COFORGE", "COLPAL", "CONCOR",
            "COROMANDEL", "CUB", "CUMMINSIND", "DABUR", "DALBHARAT", "DEEPAKNTR",
            "DIVISLAB", "DIXON", "DLF", "DRREDDY", "EICHERMOT", "ESCORTS", "EXIDEIND",
            "FEDERALBNK", "GAIL", "GLENMARK", "GODREJCP", "GODREJPROP", "GRANULES",
            "GRASIM", "GUJGASLTD", "HAL", "HAVELLS", "HCLTECH", "HDFCBANK", "HDFCLIFE",
            "HEROMOTOCO", "HINDALCO", "HINDCOPPER", "HINDPETRO", "HINDUNILVR",
            "ICICIBANK", "ICICIGI", "IDBI", "IDEA", "IDFCFIRSTB", "IEX", "INDIACEM",
            "INDIAMART", "INDIGO", "INDUSINDBK", "INDUSTOWER", "INFY", "IOC", "IPCALAB",
            "IRCTC", "ITC", "JINDALSTEL", "JIOFIN", "JSWENERGY", "JSWSTEEL", "JUBLFOOD",
            "KOTAKBANK", "LT", "LTIM", "LTTS", "LUPIN", "M&M", "M&MFIN", "MANAPPURAM",
            "MARICO", "MARUTI", "MCDOWELL-N", "METROPOLIS", "MFSL", "MGL", "MPHASIS",
            "MRF", "MUTHOOTFIN", "NAVINFLUOR", "NESTLEIND", "NMDC", "NTPC", "ONGC",
            "PAGEIND", "PEL", "PERSISTENT", "PETRONET", "PFC", "PIDILITIND", "PNB",
            "POLYCAB", "POONAWALLA", "POWERGRID", "PVRINOX", "RAMCOCEM", "RBLBANK",
            "RECLTD", "RELIANCE", "SAIL", "SBICARD", "SBILIFE", "SBIN", "SHREECEM",
            "SIEMENS", "SRF", "SUNPHARMA", "SUNTV", "SYNGENE", "TATACHEM", "TATACOMM",
            "TATACONSUM", "TATAMOTORS", "TATAPOWER", "TATASTEEL", "TCS", "TECHM",
            "TITAN", "TORNTPOWER", "TRENT", "TVSMOTOR", "UBL", "ULTRACEMCO",
            "UNIONBANK", "UPL", "VEDL", "VOLTAS", "WIPRO", "YESBANK", "ZOMATO", "ZYDUSLIFE"
        ]

        # Sector mapping
        self.sector_mapping = {
            'Banking': ['HDFCBANK', 'ICICIBANK', 'SBIN', 'AXISBANK', 'KOTAKBANK', 'INDUSINDBK',
                       'BANDHANBNK', 'FEDERALBNK', 'IDFCFIRSTB', 'BANKBARODA', 'PNB', 'CANBK',
                       'UNIONBANK', 'IDBI', 'RBLBANK'],
            'IT': ['TCS', 'INFY', 'WIPRO', 'HCLTECH', 'TECHM', 'LTIM', 'MPHASIS', 'COFORGE',
                  'PERSISTENT', 'LTTS'],
            'Auto': ['MARUTI', 'M&M', 'TATAMOTORS', 'EICHERMOT', 'BAJAJ-AUTO', 'HEROMOTOCO',
                    'ESCORTS', 'TVSMOTOR', 'MRF', 'BALKRISIND', 'EXIDEIND'],
            'Pharma': ['SUNPHARMA', 'DRREDDY', 'CIPLA', 'LUPIN', 'DIVISLAB', 'BIOCON',
                      'GLENMARK', 'IPCALAB', 'SYNGENE', 'GRANULES'],
            'Energy': ['RELIANCE', 'ONGC', 'BPCL', 'IOC', 'COALINDIA', 'NTPC', 'POWERGRID',
                      'GAIL', 'HINDPETRO', 'PETRONET', 'ADANIGREEN', 'TATAPOWER', 'JSWENERGY',
                      'PFC', 'RECLTD', 'TORNTPOWER'],
            'FMCG': ['HINDUNILVR', 'ITC', 'NESTLEIND', 'BRITANNIA', 'DABUR', 'MARICO',
                    'GODREJCP', 'COLPAL', 'TATACONSUM', 'MCDOWELL-N', 'UBL', 'JUBLFOOD'],
            'Metals': ['TATASTEEL', 'JSWSTEEL', 'HINDALCO', 'VEDL', 'JINDALSTEL', 'SAIL',
                      'NMDC', 'HINDCOPPER'],
            'Telecom': ['BHARTIARTL', 'IDEA', 'JIOFIN', 'INDUSTOWER'],
            'Cement': ['ULTRACEMCO', 'SHREECEM', 'RAMCOCEM', 'INDIACEM'],
            'Realty': ['DLF', 'GODREJPROP'],
            'Infra': ['LT', 'HAL', 'BHEL', 'CONCOR'],
            'Consumer': ['TITAN', 'TRENT', 'PVRINOX', 'DIXON', 'VOLTAS', 'HAVELLS', 'POLYCAB'],
            'Finance': ['BAJAJFINSV', 'BAJFINANCE', 'CHOLAFIN', 'M&MFIN', 'MFSL', 'SBICARD',
                       'SBILIFE', 'HDFCLIFE', 'ICICIGI', 'MANAPPURAM', 'MUTHOOTFIN', 'POONAWALLA'],
            'Others': ['ADANIENT', 'ADANIPORTS', 'ADANITRANS', 'APOLLOHOSP', 'ASIANPAINT',
                      'ASTRAL', 'ATUL', 'BERGEPAINT', 'BHARATFORG', 'BOSCHLTD', 'BSE',
                      'COROMANDEL', 'CUB', 'CUMMINSIND', 'DALBHARAT', 'DEEPAKNTR', 'GRASIM',
                      'GUJGASLTD', 'IEX', 'INDIAMART', 'INDIGO', 'IRCTC', 'METROPOLIS', 'MGL',
                      'NAVINFLUOR', 'PAGEIND', 'PEL', 'PIDILITIND', 'SRF', 'SUNTV', 'TATACHEM',
                      'TATACOMM', 'SIEMENS', 'YESBANK', 'ZOMATO', 'ZYDUSLIFE', 'ABB']
        }

        self.data_cache = {}
        self.last_refresh = None

    def get_stock_list(self):
        """Return list of stocks"""
        return self.stock_list

    def get_sectors(self):
        """Return list of available sectors"""
        return list(self.sector_mapping.keys())

    def get_stocks_by_sector(self, sector):
        """Get stocks filtered by sector"""
        if sector == "All Sectors" or sector not in self.sector_mapping:
            return self.stock_list
        return self.sector_mapping.get(sector, [])

    def get_stock_sector(self, symbol):
        """Get sector for a given stock symbol"""
        for sector, stocks in self.sector_mapping.items():
            if symbol in stocks:
                return sector
        return "Others"

    def search_stock(self, search_term):
        """Search for a stock by symbol with smart fuzzy matching

        Examples:
            'rel' -> RELIANCE
            'tat' -> TATAMOTORS (first match)
            'hdfc' -> HDFCBANK
            'tcs' -> TCS
            'infy' -> INFY
        """
        if not search_term:
            return None

        search_term = search_term.upper().strip()

        # Exact match
        if search_term in self.stock_list:
            return search_term

        # Partial match - find all stocks containing the search term
        matches = [stock for stock in self.stock_list if search_term in stock]

        if matches:
            # Prioritize: exact start match > contains match
            exact_start = [s for s in matches if s.startswith(search_term)]
            if exact_start:
                return exact_start[0]
            return matches[0]

        return None

    def search_stocks_multiple(self, search_term):
        """Return all matching stocks for a search term (for autocomplete/suggestions)"""
        if not search_term:
            return []

        search_term = search_term.upper().strip()

        # Find all matches
        matches = [stock for stock in self.stock_list if search_term in stock]

        # Sort: exact match first, then starts-with, then contains
        exact = [s for s in matches if s == search_term]
        starts = [s for s in matches if s.startswith(search_term) and s not in exact]
        contains = [s for s in matches if s not in exact and s not in starts]

        return exact + starts + contains

    def fetch_stock_data(self, symbol):
        """Fetch live stock data from NSE with fallback to historical data"""
        try:
            # Try to get live quote data from NSE
            quote = nse_quote(symbol)

            if quote and 'priceInfo' in quote:
                price_info = quote['priceInfo']

                data = {
                    'symbol': symbol,
                    'ltp': price_info.get('lastPrice', 0),
                    'open': price_info.get('open', 0),
                    'high': price_info.get('intraDayHighLow', {}).get('max', 0),
                    'low': price_info.get('intraDayHighLow', {}).get('min', 0),
                    'close': price_info.get('close', 0),
                    'change': price_info.get('pChange', 0),
                    'volume': quote.get('preOpenMarket', {}).get('totalTradedVolume', 0),
                }

                return data
            else:
                # Fallback 1: try to get LTP only
                try:
                    ltp = nse_quote_ltp(symbol)
                    if ltp:
                        return {
                            'symbol': symbol,
                            'ltp': float(ltp),
                            'open': 0,
                            'high': 0,
                            'low': 0,
                            'close': 0,
                            'change': 0,
                            'volume': 0,
                        }
                except:
                    pass

                # Fallback 2: Use historical data (last available day)
                try:
                    history = self.get_price_history(symbol, period='5d', interval='1d')
                    if history is not None and len(history) > 0:
                        last_row = history.iloc[-1]
                        prev_row = history.iloc[-2] if len(history) > 1 else last_row

                        change_pct = ((last_row['close'] - prev_row['close']) / prev_row['close']) * 100 if prev_row['close'] > 0 else 0

                        return {
                            'symbol': symbol,
                            'ltp': float(last_row['close']),
                            'open': float(last_row['open']),
                            'high': float(last_row['high']),
                            'low': float(last_row['low']),
                            'close': float(last_row['close']),
                            'change': round(change_pct, 2),
                            'volume': int(last_row['volume']),
                        }
                except Exception as hist_error:
                    print(f"Historical data fallback failed for {symbol}: {str(hist_error)}")
                    pass

                return None

        except Exception as e:
            print(f"Error fetching {symbol}: {str(e)}")

            # Final fallback: Try historical data
            try:
                history = self.get_price_history(symbol, period='5d', interval='1d')
                if history is not None and len(history) > 0:
                    last_row = history.iloc[-1]
                    prev_row = history.iloc[-2] if len(history) > 1 else last_row

                    change_pct = ((last_row['close'] - prev_row['close']) / prev_row['close']) * 100 if prev_row['close'] > 0 else 0

                    return {
                        'symbol': symbol,
                        'ltp': float(last_row['close']),
                        'open': float(last_row['open']),
                        'high': float(last_row['high']),
                        'low': float(last_row['low']),
                        'close': float(last_row['close']),
                        'change': round(change_pct, 2),
                        'volume': int(last_row['volume']),
                    }
            except:
                pass

            return None

    def calculate_technical_indicators(self, data):
        """Calculate technical indicators for stock"""
        if not data or data['ltp'] == 0:
            return {}

        ltp = data['ltp']
        high = data['high'] if data['high'] > 0 else ltp
        low = data['low'] if data['low'] > 0 else ltp
        close = data['close'] if data['close'] > 0 else ltp

        # Simple RSI approximation
        change = data['change']
        rsi = 50 + (change * 2)  # Simplified RSI
        rsi = max(0, min(100, rsi))

        # Support and Resistance (Gann style)
        high_trend = ((high + 0.45) * 0.45) / 100
        low_trend = ((low - 0.45) * 0.45) / 100

        resistance = high + high_trend
        support = low - abs(low_trend)

        # Moving average approximation
        ma_20 = close

        indicators = {
            'rsi': rsi,
            'resistance': resistance,
            'support': support,
            'ma_20': ma_20,
            'atr': high - low if high > low else ltp * 0.02,
        }

        return indicators

    def generate_signals(self, symbol, data, indicators, scan_type='intraday', risk_level='medium', ml_engine=None):
        """Generate buy/sell signals using ML model with 60-day historical data"""
        if not data or not indicators:
            return None

        ltp = data['ltp']
        change = data['change']
        rsi = indicators.get('rsi', 50)
        support = indicators.get('support', ltp * 0.98)
        resistance = indicators.get('resistance', ltp * 1.02)
        atr = indicators.get('atr', ltp * 0.02)

        # Use ML model if available
        signal = "HOLD"
        score = 50
        confidence = 50.0
        model_accuracy = 0.0

        if ml_engine and ml_engine.is_trained:
            # Get 60-day historical data
            history = self.get_price_history(symbol, period='3mo', interval='1d')

            if history is not None and len(history) >= 60:
                # Use ML prediction
                ml_prediction = ml_engine.predict_signal_from_history(history)

                if ml_prediction:
                    signal = ml_prediction['signal']
                    confidence = ml_prediction['confidence']
                    score = confidence
                    model_accuracy = ml_prediction.get('model_accuracy', 0.0)
                else:
                    # Fallback to rule-based
                    signal, score = self._rule_based_signal(data, indicators)
            else:
                # Fallback to rule-based if not enough history
                signal, score = self._rule_based_signal(data, indicators)
        else:
            # Fallback to rule-based
            signal, score = self._rule_based_signal(data, indicators)

    def _rule_based_signal(self, data, indicators):
        """Rule-based signal generation (fallback)"""
        ltp = data['ltp']
        change = data['change']
        rsi = indicators.get('rsi', 50)
        support = indicators.get('support', ltp * 0.98)
        resistance = indicators.get('resistance', ltp * 1.02)

        # Buy conditions
        buy_score = 0
        if change > 0:
            buy_score += 20
        if rsi < 40:
            buy_score += 30
        if ltp <= support * 1.01:
            buy_score += 25
        if data['volume'] > 0:
            buy_score += 15

        # Sell conditions
        sell_score = 0
        if change < 0:
            sell_score += 20
        if rsi > 60:
            sell_score += 30
        if ltp >= resistance * 0.99:
            sell_score += 25

        # Determine signal
        if buy_score > 60:
            return "BUY", buy_score
        elif sell_score > 60:
            return "SELL", sell_score
        else:
            return "HOLD", max(buy_score, sell_score)

        # Calculate entry, target, and stop loss
        if signal == "BUY":
            entry = ltp
            if scan_type == 'intraday':
                target = entry + (atr * 1.5)
                stop_loss = entry - atr
            else:  # delivery/swing
                target = entry + (atr * 2.5)
                stop_loss = entry - (atr * 1.2)
        elif signal == "SELL":
            entry = ltp
            if scan_type == 'intraday':
                target = entry - (atr * 1.5)
                stop_loss = entry + atr
            else:
                target = entry - (atr * 2.5)
                stop_loss = entry + (atr * 1.2)
        else:
            entry = ltp
            target = resistance
            stop_loss = support

        # Risk adjustment
        risk_multiplier = {'low': 0.7, 'medium': 1.0, 'high': 1.3}.get(risk_level, 1.0)
        target = entry + (target - entry) * risk_multiplier

        return {
            'signal': signal,
            'entry': round(entry, 2),
            'target': round(target, 2),
            'stop_loss': round(stop_loss, 2),
            'score': min(100, score),
            'rsi': round(rsi, 2),
            'confidence': round(confidence, 2),
            'model_accuracy': round(model_accuracy, 2),
        }

    def scan_all_stocks(self, scan_type='intraday', risk_level='medium', progress_callback=None,
                       stock_filter=None, sector_filter=None, ml_engine=None):
        """Scan all stocks and return recommendations using ML model

        Args:
            scan_type: Type of scan ('intraday', 'delivery', 'swing')
            risk_level: Risk level ('low', 'medium', 'high')
            progress_callback: Callback function for progress updates
            stock_filter: Single stock symbol to scan (optional)
            sector_filter: Sector to filter stocks (optional)
            ml_engine: ML engine instance for predictions (optional)
        """
        results = []

        # Determine which stocks to scan
        if stock_filter:
            # Single stock search
            stocks_to_scan = [stock_filter] if stock_filter in self.stock_list else []
        elif sector_filter and sector_filter != "All Sectors":
            # Sector-based filtering
            stocks_to_scan = self.get_stocks_by_sector(sector_filter)
        else:
            # All stocks
            stocks_to_scan = self.stock_list

        total_stocks = len(stocks_to_scan)

        for idx, symbol in enumerate(stocks_to_scan):
            if progress_callback:
                progress = (idx + 1) / total_stocks
                progress_callback(progress, f"Scanning {symbol}... ({idx + 1}/{total_stocks})")

            # Fetch data
            data = self.fetch_stock_data(symbol)

            if data:
                # Calculate indicators
                indicators = self.calculate_technical_indicators(data)

                # Generate signals with ML
                signals = self.generate_signals(symbol, data, indicators, scan_type, risk_level, ml_engine)

                if signals:
                    results.append({
                        'Symbol': symbol,
                        'Sector': self.get_stock_sector(symbol),
                        'LTP': data['ltp'],
                        'Change %': data['change'],
                        'Signal': signals['signal'],
                        'Entry': signals['entry'],
                        'Target': signals['target'],
                        'Stop Loss': signals['stop_loss'],
                        'Score': signals['score'],
                        'RSI': signals['rsi'],
                        'Volume': data['volume'],
                        'Confidence': signals.get('confidence', 50.0),
                        'Model_Accuracy': signals.get('model_accuracy', 0.0),
                    })

            # Rate limiting
            time.sleep(0.1)

        # Convert to DataFrame
        if results:
            df = pd.DataFrame(results)
            df = df.sort_values('Score', ascending=False)
            self.last_refresh = datetime.now()
            return df

        return None

    def get_stock_details(self, symbol):
        """Get detailed information for a specific stock"""
        return self.fetch_stock_data(symbol)
    def get_price_history(self, symbol, period='6mo', interval='1d'):
        """Fetch historical OHLCV for charts using yfinance
        Returns a DataFrame with columns: date, open, high, low, close, adj_close, volume
        """
        try:
            yf_symbol = f"{symbol}.NS"
            df = yf.download(yf_symbol, period=period, interval=interval, progress=False, auto_adjust=False)
            if df is None or df.empty:
                # Fallback to safer defaults
                df = yf.download(yf_symbol, period='3mo', interval='1d', progress=False, auto_adjust=False)
            if df is None or df.empty:
                return None
            df = df.reset_index().rename(columns={
                'Date': 'date', 'Open': 'open', 'High': 'high', 'Low': 'low',
                'Close': 'close', 'Adj Close': 'adj_close', 'Volume': 'volume'
            })
            return df
        except Exception as e:
            print(f"Error fetching history for {symbol}: {e}")
            return None


    def refresh_data(self):
        """Refresh cached data"""
        self.data_cache = {}
        self.last_refresh = datetime.now()

