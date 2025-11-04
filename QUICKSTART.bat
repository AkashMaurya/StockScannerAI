@echo off
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║         NSE STOCK SCANNER - QUICK START                   ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

echo [1/3] Activating virtual environment...
call myenv\Scripts\activate.bat

echo.
echo [2/3] Testing installation...
python test_installation.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Installation test failed!
    echo Please run: pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo.
echo [3/3] Starting Streamlit app...
echo.
echo ════════════════════════════════════════════════════════════
echo  The app will open in your browser at http://localhost:8501
echo  Press Ctrl+C to stop the server
echo ════════════════════════════════════════════════════════════
echo.

streamlit run streamlit_app.py

