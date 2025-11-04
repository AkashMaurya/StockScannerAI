"""
Test script to verify NSE Stock Scanner installation
"""

import sys

def test_imports():
    """Test if all required packages are installed"""
    print("=" * 60)
    print("Testing Package Imports...")
    print("=" * 60)
    
    packages = [
        ('streamlit', 'Streamlit'),
        ('pandas', 'Pandas'),
        ('numpy', 'NumPy'),
        ('sklearn', 'Scikit-learn'),
        ('plotly', 'Plotly'),
        ('nsepython', 'NSEPython'),
        ('requests', 'Requests'),
    ]
    
    failed = []
    
    for package, name in packages:
        try:
            __import__(package)
            print(f"✓ {name:20s} - OK")
        except ImportError as e:
            print(f"✗ {name:20s} - FAILED")
            failed.append(name)
    
    print("=" * 60)
    
    if failed:
        print(f"\n❌ Failed to import: {', '.join(failed)}")
        print("\nPlease install missing packages:")
        print("pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_nse_connection():
    """Test NSE data fetching"""
    print("\n" + "=" * 60)
    print("Testing NSE Data Connection...")
    print("=" * 60)
    
    try:
        from nsepython import nse_quote_ltp
        
        print("Fetching RELIANCE stock price...")
        price = nse_quote_ltp("RELIANCE")
        
        if price:
            print(f"✓ RELIANCE LTP: ₹{price}")
            print("✅ NSE connection working!")
            return True
        else:
            print("⚠ Could not fetch price (market might be closed)")
            return True  # Not a critical error
            
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        print("❌ NSE connection failed")
        return False

def test_modules():
    """Test custom modules"""
    print("\n" + "=" * 60)
    print("Testing Custom Modules...")
    print("=" * 60)
    
    try:
        from nse_scanner import NSEScanner
        print("✓ NSEScanner module - OK")
        
        from ml_engine import MLRecommendationEngine
        print("✓ MLRecommendationEngine module - OK")
        
        # Test initialization
        scanner = NSEScanner()
        print(f"✓ Scanner initialized with {len(scanner.get_stock_list())} stocks")
        
        ml_engine = MLRecommendationEngine()
        print("✓ ML Engine initialized")
        
        print("=" * 60)
        print("✅ All custom modules working!")
        return True
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        print("=" * 60)
        print("❌ Module test failed")
        return False

def test_ml_model():
    """Test ML model training"""
    print("\n" + "=" * 60)
    print("Testing ML Model...")
    print("=" * 60)
    
    try:
        from ml_engine import MLRecommendationEngine
        
        ml_engine = MLRecommendationEngine()
        print("Training ML model...")
        
        success = ml_engine.train_model()
        
        if success:
            print("✓ Model trained successfully")
            
            # Test prediction
            test_data = {
                'symbol': 'TEST',
                'ltp': 100,
                'change': 2.5,
                'volume': 1000000,
                'high': 102,
                'low': 98,
                'close': 100,
            }
            
            test_indicators = {
                'rsi': 45,
                'resistance': 105,
                'support': 95,
                'ma_20': 100,
                'atr': 2,
            }
            
            prediction = ml_engine.predict_signal(test_data, test_indicators)
            
            if prediction:
                print(f"✓ Test prediction: {prediction['signal']} (Confidence: {prediction['confidence']}%)")
                print("=" * 60)
                print("✅ ML model working!")
                return True
            else:
                print("⚠ Prediction returned None")
                return False
        else:
            print("✗ Model training failed")
            return False
            
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        print("=" * 60)
        print("❌ ML model test failed")
        return False

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "NSE STOCK SCANNER - INSTALLATION TEST" + " " * 10 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")
    
    results = []
    
    # Test 1: Package imports
    results.append(("Package Imports", test_imports()))
    
    # Test 2: NSE connection
    results.append(("NSE Connection", test_nse_connection()))
    
    # Test 3: Custom modules
    results.append(("Custom Modules", test_modules()))
    
    # Test 4: ML model
    results.append(("ML Model", test_ml_model()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:20s} : {status}")
    
    print("=" * 60)
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
        print("\nYou can now run the application:")
        print("  streamlit run streamlit_app.py")
    else:
        print("\n⚠ SOME TESTS FAILED")
        print("\nPlease fix the issues and run this test again.")
        print("\nCommon fixes:")
        print("  1. Activate virtual environment: myenv\\Scripts\\activate")
        print("  2. Install dependencies: pip install -r requirements.txt")
        print("  3. Check internet connection")
    
    print("\n")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

