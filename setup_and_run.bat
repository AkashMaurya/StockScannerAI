@echo off
echo ========================================
echo NSE Stock Scanner Setup
echo ========================================
echo.

echo Activating virtual environment...
call myenv\Scripts\activate.bat

echo.
echo Installing required packages...
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the Streamlit app, use:
echo streamlit run streamlit_app.py
echo.
echo Or run this script again to start the app automatically.
echo.
pause

echo.
echo Starting Streamlit app...
streamlit run streamlit_app.py

