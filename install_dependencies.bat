@echo off
echo ========================================
echo Installing NSE Stock Scanner Dependencies
echo ========================================
echo.

echo Activating virtual environment...
call myenv\Scripts\activate.bat

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing dependencies one by one...
echo.

echo [1/10] Installing streamlit...
pip install streamlit==1.29.0

echo [2/10] Installing nsepython...
pip install nsepython

echo [3/10] Installing pandas...
pip install pandas

echo [4/10] Installing numpy...
pip install numpy

echo [5/10] Installing scikit-learn...
pip install scikit-learn

echo [6/10] Installing plotly...
pip install plotly

echo [7/10] Installing ta...
pip install ta

echo [8/10] Installing requests...
pip install requests

echo [9/10] Installing beautifulsoup4...
pip install beautifulsoup4

echo [10/10] Installing yfinance...
pip install yfinance

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Testing installation...
python test_installation.py

echo.
pause

