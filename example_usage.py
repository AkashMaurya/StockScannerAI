"""
Example usage of NSE Scanner and ML Engine
This script demonstrates how to use the scanner programmatically
"""

from nse_scanner import NSEScanner
from ml_engine import MLRecommendationEngine
import pandas as pd
from datetime import datetime

def example_1_fetch_single_stock():
    """Example 1: Fetch data for a single stock"""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: Fetch Single Stock Data")
    print("=" * 60)
    
    scanner = NSEScanner()
    
    # Fetch RELIANCE stock data
    stock_data = scanner.fetch_stock_data("RELIANCE")
    
    if stock_data:
        print(f"\nStock: {stock_data['symbol']}")
        print(f"LTP: ₹{stock_data['ltp']:.2f}")
        print(f"Change: {stock_data['change']:.2f}%")
        print(f"High: ₹{stock_data['high']:.2f}")
        print(f"Low: ₹{stock_data['low']:.2f}")
        print(f"Volume: {stock_data['volume']:,}")
    else:
        print("Failed to fetch data (market might be closed)")

def example_2_calculate_indicators():
    """Example 2: Calculate technical indicators"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Calculate Technical Indicators")
    print("=" * 60)
    
    scanner = NSEScanner()
    
    # Fetch data
    stock_data = scanner.fetch_stock_data("TCS")
    
    if stock_data:
        # Calculate indicators
        indicators = scanner.calculate_technical_indicators(stock_data)
        
        print(f"\nStock: {stock_data['symbol']}")
        print(f"RSI: {indicators.get('rsi', 0):.2f}")
        print(f"Resistance: ₹{indicators.get('resistance', 0):.2f}")
        print(f"Support: ₹{indicators.get('support', 0):.2f}")
        print(f"ATR: ₹{indicators.get('atr', 0):.2f}")

def example_3_generate_signals():
    """Example 3: Generate trading signals"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Generate Trading Signals")
    print("=" * 60)
    
    scanner = NSEScanner()
    
    # Fetch data
    stock_data = scanner.fetch_stock_data("INFY")
    
    if stock_data:
        # Calculate indicators
        indicators = scanner.calculate_technical_indicators(stock_data)
        
        # Generate signals
        signals = scanner.generate_signals(
            stock_data, 
            indicators, 
            scan_type='intraday',
            risk_level='medium'
        )
        
        if signals:
            print(f"\nStock: {stock_data['symbol']}")
            print(f"Signal: {signals['signal']}")
            print(f"Entry: ₹{signals['entry']:.2f}")
            print(f"Target: ₹{signals['target']:.2f}")
            print(f"Stop Loss: ₹{signals['stop_loss']:.2f}")
            print(f"AI Score: {signals['score']}/100")

def example_4_ml_prediction():
    """Example 4: ML-based prediction"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: ML-Based Prediction")
    print("=" * 60)
    
    scanner = NSEScanner()
    ml_engine = MLRecommendationEngine()
    
    # Train model
    print("\nTraining ML model...")
    ml_engine.train_model()
    
    # Fetch data
    stock_data = scanner.fetch_stock_data("HDFCBANK")
    
    if stock_data:
        # Calculate indicators
        indicators = scanner.calculate_technical_indicators(stock_data)
        
        # Get ML prediction
        prediction = ml_engine.predict_signal(stock_data, indicators)
        
        if prediction:
            print(f"\nStock: {stock_data['symbol']}")
            print(f"ML Signal: {prediction['signal']}")
            print(f"Confidence: {prediction['confidence']:.2f}%")
            print(f"\nProbabilities:")
            for signal, prob in prediction['probabilities'].items():
                print(f"  {signal}: {prob:.2f}%")

def example_5_advanced_recommendation():
    """Example 5: Advanced recommendation with position sizing"""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Advanced Recommendation")
    print("=" * 60)
    
    scanner = NSEScanner()
    ml_engine = MLRecommendationEngine()
    
    # Train model
    ml_engine.train_model()
    
    # Fetch data
    stock_data = scanner.fetch_stock_data("TATAMOTORS")
    
    if stock_data:
        # Calculate indicators
        indicators = scanner.calculate_technical_indicators(stock_data)
        
        # Get advanced recommendation
        recommendation = ml_engine.generate_advanced_recommendation(
            stock_data,
            indicators,
            scan_type='delivery',
            capital=100000,  # ₹1 Lakh
            risk_per_trade=2  # 2% risk
        )
        
        if recommendation:
            print(f"\nStock: {recommendation['symbol']}")
            print(f"Signal: {recommendation['signal']}")
            print(f"Confidence: {recommendation['confidence']:.2f}%")
            print(f"\nTrade Details:")
            print(f"  Entry: ₹{recommendation['entry']:.2f}")
            print(f"  Target: ₹{recommendation['target']:.2f}")
            print(f"  Stop Loss: ₹{recommendation['stop_loss']:.2f}")
            print(f"  Position Size: {recommendation['position_size']} shares")
            print(f"  Risk-Reward Ratio: 1:{recommendation['risk_reward_ratio']}")
            print(f"  Scan Type: {recommendation['scan_type']}")

def example_6_scan_multiple_stocks():
    """Example 6: Scan multiple stocks"""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Scan Multiple Stocks")
    print("=" * 60)
    
    scanner = NSEScanner()
    
    # List of stocks to scan
    stocks_to_scan = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK"]
    
    results = []
    
    print(f"\nScanning {len(stocks_to_scan)} stocks...\n")
    
    for symbol in stocks_to_scan:
        print(f"Scanning {symbol}...", end=" ")
        
        # Fetch data
        stock_data = scanner.fetch_stock_data(symbol)
        
        if stock_data:
            # Calculate indicators
            indicators = scanner.calculate_technical_indicators(stock_data)
            
            # Generate signals
            signals = scanner.generate_signals(stock_data, indicators)
            
            if signals:
                results.append({
                    'Symbol': symbol,
                    'LTP': stock_data['ltp'],
                    'Change %': stock_data['change'],
                    'Signal': signals['signal'],
                    'Entry': signals['entry'],
                    'Target': signals['target'],
                    'Stop Loss': signals['stop_loss'],
                    'Score': signals['score'],
                })
                print("✓")
            else:
                print("✗")
        else:
            print("✗")
    
    # Display results
    if results:
        df = pd.DataFrame(results)
        print("\n" + "=" * 60)
        print("SCAN RESULTS")
        print("=" * 60)
        print(df.to_string(index=False))
        
        # Summary
        buy_count = len(df[df['Signal'] == 'BUY'])
        sell_count = len(df[df['Signal'] == 'SELL'])
        hold_count = len(df[df['Signal'] == 'HOLD'])
        
        print("\n" + "=" * 60)
        print(f"BUY Signals: {buy_count}")
        print(f"SELL Signals: {sell_count}")
        print(f"HOLD Signals: {hold_count}")

def example_7_trend_calculator():
    """Example 7: Gann Trend Calculator"""
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Gann Trend Calculator")
    print("=" * 60)
    
    high_value = 1500.0
    low_value = 1450.0
    
    # Calculation
    high_trend = ((high_value + 0.45) * 0.45) / 100
    low_trend = ((high_value - 0.45) * 0.45) / 100
    
    high_resistance = high_trend + high_value
    low_support = low_trend + low_value
    next_high = high_resistance + high_trend
    next_low = low_support - low_trend
    
    print(f"\nInput:")
    print(f"  High: ₹{high_value:.2f}")
    print(f"  Low: ₹{low_value:.2f}")
    
    print(f"\nResults:")
    print(f"  High Resistance: ₹{high_resistance:.2f} (+{high_trend:.2f})")
    print(f"  Low Support: ₹{low_support:.2f} ({low_trend:.2f})")
    print(f"  Next High: ₹{next_high:.2f}")
    print(f"  Next Low: ₹{next_low:.2f}")

def main():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "NSE STOCK SCANNER - USAGE EXAMPLES" + " " * 13 + "║")
    print("╚" + "=" * 58 + "╝")
    
    print("\nNote: Some examples may fail if market is closed or internet is unavailable.")
    print("Press Enter to continue...")
    input()
    
    # Run examples
    example_1_fetch_single_stock()
    example_2_calculate_indicators()
    example_3_generate_signals()
    example_4_ml_prediction()
    example_5_advanced_recommendation()
    example_6_scan_multiple_stocks()
    example_7_trend_calculator()
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)
    print("\nFor the full web interface, run:")
    print("  streamlit run streamlit_app.py")
    print("\n")

if __name__ == "__main__":
    main()

