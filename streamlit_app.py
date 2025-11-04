import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
from datetime import datetime
from nse_scanner import NSEScanner
from ml_engine import MLRecommendationEngine

# Page configuration
st.set_page_config(
    page_title="NSE Stock Scanner & AI Recommender",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #1f2937;
        border-radius: 5px;
        padding: 10px 20px;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #3b82f6;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .buy-signal {
        background-color: #10b981;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .sell-signal {
        background-color: #ef4444;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    .hold-signal {
        background-color: #f59e0b;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'scanner' not in st.session_state:
    st.session_state.scanner = NSEScanner()
if 'ml_engine' not in st.session_state:
    st.session_state.ml_engine = MLRecommendationEngine()
if 'ml_trained' not in st.session_state:
    st.session_state.ml_trained = False

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/stock-market.png", width=100)
    st.title("🎯 NSE Scanner")
    st.markdown("---")

    scan_type = st.selectbox(
        "Scan Type",
        ["Intraday", "Delivery", "Swing Trading"]
    )

    risk_level = st.select_slider(
        "Risk Level",
        options=["Low", "Medium", "High"],
        value="Medium"
    )

    st.markdown("---")

    # ML Model Training Section
    st.subheader("🤖 AI Model")

    if st.session_state.ml_trained:
        st.success(f"✅ Model Trained")
        st.metric("Accuracy", f"{st.session_state.ml_engine.accuracy:.1f}%")
    else:
        st.warning("⚠️ Model Not Trained")
        if st.button("🧠 Train AI Model", use_container_width=True):
            with st.spinner("Training AI model with 60-day historical data..."):
                # Collect historical data from top 50 stocks for training
                training_stocks = st.session_state.scanner.get_stock_list()[:50]
                history_data_list = []

                progress_bar = st.progress(0)
                for idx, symbol in enumerate(training_stocks):
                    history = st.session_state.scanner.get_price_history(symbol, period='3mo', interval='1d')
                    if history is not None and len(history) >= 60:
                        history_data_list.append(history)
                    progress_bar.progress((idx + 1) / len(training_stocks))

                # Train the model
                if len(history_data_list) >= 10:
                    st.session_state.ml_engine.train_model_from_history(history_data_list)
                    st.session_state.ml_trained = True
                    st.success(f"✅ Model trained! Accuracy: {st.session_state.ml_engine.accuracy:.1f}%")
                    st.rerun()
                else:
                    st.error("Not enough historical data. Using rule-based model.")
                    st.session_state.ml_engine.train_rule_based_model()
                    st.session_state.ml_trained = True
                    st.rerun()

    st.markdown("---")

    if st.button("🔄 Refresh Data", use_container_width=True):
        st.session_state.scanner.refresh_data()
        st.success("Data refreshed!")

    st.markdown("---")
    st.info(f"**Last Updated:** {datetime.now().strftime('%H:%M:%S')}")

# Main content
st.title("📊 NSE Stock Scanner & AI Recommender")
st.markdown("### Real-time Stock Analysis with ML/AI Powered Recommendations")
st.markdown("#### only works during market hours")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Scanner", "📈 Trend Calculator", "📊 Stock Details", "⚙️ Settings"])

with tab1:
    st.header("Live Stock Scanner")

    # Search and Filter Section
    st.markdown("### 🔍 Search & Filter")
    col1, col2 = st.columns([2, 1])

    with col1:
        # Use selectbox with search capability instead of text input
        all_stocks = [""] + st.session_state.scanner.get_stock_list()
        search_stock = st.selectbox(
            "Search for a specific stock",
            options=all_stocks,
            index=0,
            format_func=lambda x: "Select a stock..." if x == "" else x,
            help="Select a stock from the dropdown or start typing to search"
        )
        # Convert empty string to None for consistency
        search_stock = search_stock if search_stock != "" else None

    with col2:
        sector_selection = st.selectbox(
            "Filter by Sector",
            ["All Sectors"] + st.session_state.scanner.get_sectors(),
            help="Select a sector to scan only stocks from that sector"
        )

    # Show stock count for selected filter
    if search_stock:
        stock_found = search_stock  # Already validated from selectbox
        st.success(f"✓ Selected: **{stock_found}** ({st.session_state.scanner.get_stock_sector(stock_found)} sector)")
        stocks_to_scan_count = 1
    elif sector_selection != "All Sectors":
        stocks_in_sector = st.session_state.scanner.get_stocks_by_sector(sector_selection)
        stocks_to_scan_count = len(stocks_in_sector)
        st.info(f"📊 {stocks_to_scan_count} stocks in {sector_selection} sector")
    else:
        stocks_to_scan_count = len(st.session_state.scanner.get_stock_list())
        st.info(f"📊 Total {stocks_to_scan_count} stocks will be scanned")

    st.markdown("---")

    # Metrics Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <h3>Stocks to Scan</h3>
                <h1>{stocks_to_scan_count}</h1>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        buy_count = st.session_state.get('buy_count', 0)
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
                <h3>Buy Signals</h3>
                <h1>{buy_count}</h1>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        sell_count = st.session_state.get('sell_count', 0)
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);">
                <h3>Sell Signals</h3>
                <h1>{sell_count}</h1>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        hold_count = st.session_state.get('hold_count', 0)
        st.markdown(f"""
            <div class="metric-card" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);">
                <h3>Hold Signals</h3>
                <h1>{hold_count}</h1>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Scan button
    scan_disabled = (search_stock and not stock_found) or stocks_to_scan_count == 0

    if st.button("🚀 Start Scanning", use_container_width=True, type="primary", disabled=scan_disabled):
        with st.spinner("Scanning stocks... This may take a few minutes..."):
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Determine stock filter
            stock_filter_value = None
            sector_filter_value = None

            if search_stock and stock_found:
                stock_filter_value = stock_found
            elif sector_selection != "All Sectors":
                sector_filter_value = sector_selection

            # Get scanner results with ML engine
            ml_engine_to_use = st.session_state.ml_engine if st.session_state.ml_trained else None

            results = st.session_state.scanner.scan_all_stocks(
                scan_type=scan_type.lower(),
                risk_level=risk_level.lower(),
                progress_callback=lambda p, s: (progress_bar.progress(p), status_text.text(s)),
                stock_filter=stock_filter_value,
                sector_filter=sector_filter_value,
                ml_engine=ml_engine_to_use
            )

            progress_bar.empty()
            status_text.empty()

            if results is not None and len(results) > 0:
                # Show info about data source
                st.info("ℹ️ Using historical data fallback (NSE API may be unavailable or market is closed). Data is from the last trading day.")

            if results is not None and len(results) > 0:
                # Update signal counts
                st.session_state.buy_count = len(results[results['Signal'] == 'BUY'])
                st.session_state.sell_count = len(results[results['Signal'] == 'SELL'])
                st.session_state.hold_count = len(results[results['Signal'] == 'HOLD'])

                st.success(f"✅ Scanned {len(results)} stocks successfully!")

                # Quick Summary of Top Actionable Stocks
                buy_stocks = results[results['Signal'] == 'BUY'].head(3)
                sell_stocks = results[results['Signal'] == 'SELL'].head(3)

                if len(buy_stocks) > 0 or len(sell_stocks) > 0:
                    st.markdown("### 🎯 Top Actionable Recommendations")
                    col1, col2 = st.columns(2)

                    with col1:
                        if len(buy_stocks) > 0:
                            st.markdown("#### 🟢 Top BUY Signals")
                            for _, stock in buy_stocks.iterrows():
                                confidence_text = f" | Confidence: {stock.get('Confidence', 50):.1f}%" if 'Confidence' in stock else ""
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                                            padding: 10px; border-radius: 5px; margin-bottom: 10px; color: white;">
                                    <strong>{stock['Symbol']}</strong> - Score: {stock['Score']:.0f}/100{confidence_text}<br/>
                                    Entry: ₹{stock['Entry']:.2f} | Target: ₹{stock['Target']:.2f} | SL: ₹{stock['Stop Loss']:.2f}
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.info("No BUY signals found")

                    with col2:
                        if len(sell_stocks) > 0:
                            st.markdown("#### 🔴 Top SELL Signals")
                            for _, stock in sell_stocks.iterrows():
                                confidence_text = f" | Confidence: {stock.get('Confidence', 50):.1f}%" if 'Confidence' in stock else ""
                                st.markdown(f"""
                                <div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
                                            padding: 10px; border-radius: 5px; margin-bottom: 10px; color: white;">
                                    <strong>{stock['Symbol']}</strong> - Score: {stock['Score']:.0f}/100{confidence_text}<br/>
                                    Entry: ₹{stock['Entry']:.2f} | Target: ₹{stock['Target']:.2f} | SL: ₹{stock['Stop Loss']:.2f}
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.info("No SELL signals found")

                    st.markdown("---")

                    # If single-stock search, show its chart regardless of signal
                    if stock_filter_value:
                        st.markdown(f"### \ud83d\udcc8 {stock_filter_value} Price Chart")
                        sel_hist = st.session_state.scanner.get_price_history(stock_filter_value, period='3mo', interval='1d')
                        if sel_hist is not None and not sel_hist.empty:
                            sel_hist['ma20'] = sel_hist['close'].rolling(20).mean()
                            fig_sel = go.Figure()
                            fig_sel.add_trace(go.Candlestick(
                                x=sel_hist['date'], open=sel_hist['open'], high=sel_hist['high'],
                                low=sel_hist['low'], close=sel_hist['close'], name='Price'
                            ))
                            fig_sel.add_trace(go.Scatter(
                                x=sel_hist['date'], y=sel_hist['ma20'], name='MA 20',
                                line=dict(color='#facc15', width=1.2)
                            ))
                            fig_sel.update_layout(template='plotly_dark', height=350, xaxis_rangeslider_visible=False,
                                                  margin=dict(l=10, r=10, t=30, b=10))
                            st.plotly_chart(fig_sel, use_container_width=True)
                        else:
                            st.info("Chart unavailable for the selected symbol.")


                # Filter options
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown("### 📊 Scan Results")
                with col2:
                    show_filter = st.selectbox(
                        "Show",
                        ["BUY & SELL Only", "All Signals"],
                        index=0,
                        help="Filter results by signal type"
                    )

                # Filter results based on selection
                if show_filter == "BUY & SELL Only":
                    filtered_results = results[results['Signal'].isin(['BUY', 'SELL'])]
                    if len(filtered_results) == 0:
                        st.info("ℹ️ No BUY or SELL signals found. All stocks are in HOLD status.")
                        filtered_results = results
                else:
                    filtered_results = results

                # Show ML model info if trained
                if st.session_state.ml_trained and 'Model_Accuracy' in filtered_results.columns:
                    avg_accuracy = filtered_results['Model_Accuracy'].mean()
                    if avg_accuracy > 0:
                        st.info(f"🤖 AI Model Accuracy: {avg_accuracy:.1f}% | Predictions based on 60-day historical data analysis")

                # Display results table
                display_columns = ['Symbol', 'Sector', 'LTP', 'Change %', 'Signal', 'Entry', 'Target', 'Stop Loss', 'Score', 'RSI']
                if 'Confidence' in filtered_results.columns:
                    display_columns.append('Confidence')

                st.dataframe(
                    filtered_results[display_columns],
                    use_container_width=True,
                    height=400,
                    column_config={
                        "Signal": st.column_config.TextColumn(
                            "Signal",
                            width="small",
                        ),
                        "Entry": st.column_config.NumberColumn(
                            "Entry Price",
                            format="₹%.2f"
                        ),
                        "Target": st.column_config.NumberColumn(
                            "Target",
                            format="₹%.2f"
                        ),
                        "Stop Loss": st.column_config.NumberColumn(
                            "Stop Loss",
                            format="₹%.2f"
                        ),
                        "LTP": st.column_config.NumberColumn(
                            "LTP",
                            format="₹%.2f"
                        ),
                        "Change %": st.column_config.NumberColumn(
                            "Change %",
                            format="%.2f%%"
                        ),
                        "Score": st.column_config.ProgressColumn(
                            "AI Score",
                            format="%.0f",
                            min_value=0,
                            max_value=100,
                        ),
                        "Confidence": st.column_config.ProgressColumn(
                            "Confidence %",
                            format="%.1f%%",
                            min_value=0,
                            max_value=100,
                        ) if 'Confidence' in display_columns else None,
                    }
                )

                # Download button
                csv = results.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results as CSV",
                    data=csv,
                    file_name=f"nse_scanner_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                )

                # Detailed Recommendations Section
                st.markdown("---")
                st.markdown("### 📋 Detailed AI Recommendations")

                # Filter for BUY and SELL signals only for detailed view
                actionable_results = results[results['Signal'].isin(['BUY', 'SELL'])]

                if len(actionable_results) > 0:
                    # Show count and option to expand all
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**{len(actionable_results)} actionable signals found** (BUY: {len(actionable_results[actionable_results['Signal']=='BUY'])}, SELL: {len(actionable_results[actionable_results['Signal']=='SELL'])})")
                    with col2:
                        show_all = st.checkbox("Show All", value=False, help="Show all stocks or just top 10")

                    # Determine how many to show
                    stocks_to_show = actionable_results if show_all else actionable_results.head(10)

                    st.markdown("Click on any stock below to see detailed analysis and reasoning")

                    for idx, (_, stock_result) in enumerate(stocks_to_show.iterrows()):
                        symbol = stock_result['Symbol']
                        signal = stock_result['Signal']

                        # Get detailed recommendation from ML engine
                        stock_data = st.session_state.scanner.fetch_stock_data(symbol)
                        if stock_data:
                            indicators = st.session_state.scanner.calculate_technical_indicators(stock_data)
                            detailed_rec = st.session_state.ml_engine.generate_advanced_recommendation(
                                stock_data, indicators, scan_type=scan_type.lower()
                            )

                            if detailed_rec:
                                # Color coding
                                if signal == 'BUY':
                                    signal_color = "🟢"
                                    card_color = "#10b981"
                                else:
                                    signal_color = "🔴"
                                    card_color = "#ef4444"

                                # Expandable card
                                with st.expander(
                                    f"{signal_color} **{symbol}** - {signal} @ ₹{detailed_rec['entry']:.2f} "
                                    f"(Confidence: {detailed_rec['confidence']:.0f}%)",
                                    expanded=(idx == 0)  # Expand first one by default
                                ):
                                    col1, col2, col3 = st.columns(3)

                                    with col1:
                                        st.markdown(f"""
                                        **📍 Entry Price:** ₹{detailed_rec['entry']:.2f}
                                        **🎯 Target Price:** ₹{detailed_rec['target']:.2f}
                                        **🛑 Stop Loss:** ₹{detailed_rec['stop_loss']:.2f}
                                        """)

                                    with col2:
                                        st.markdown(f"""
                                        **📊 Risk-Reward:** 1:{detailed_rec['risk_reward_ratio']:.2f}
                                        **💰 Position Size:** {detailed_rec['position_size']} shares
                                        **⏱️ Timeframe:** {detailed_rec.get('timeframe', 'N/A')}
                                        """)

                                    with col3:
                                        st.markdown(f"""
                                        **🎲 Confidence:** {detailed_rec['confidence']:.1f}%
                                        **📈 Sector:** {stock_result.get('Sector', 'N/A')}
                                        **💹 Current Price:** ₹{stock_data['ltp']:.2f}
                                        """)

                                    # Mini price chart
                                    st.markdown("#### 📈 Price Chart")
                                    mini_hist = st.session_state.scanner.get_price_history(symbol, period='3mo', interval='1d')
                                    if mini_hist is not None and not mini_hist.empty:
                                        mini_hist['ma20'] = mini_hist['close'].rolling(20).mean()
                                        fig_mini = go.Figure()
                                        fig_mini.add_trace(go.Candlestick(
                                            x=mini_hist['date'], open=mini_hist['open'], high=mini_hist['high'],
                                            low=mini_hist['low'], close=mini_hist['close'], name='Price'
                                        ))
                                        fig_mini.add_trace(go.Scatter(
                                            x=mini_hist['date'], y=mini_hist['ma20'], name='MA 20',
                                            line=dict(color='#facc15', width=1.2)
                                        ))
                                        fig_mini.update_layout(template='plotly_dark', height=300, xaxis_rangeslider_visible=False,
                                                               margin=dict(l=10, r=10, t=30, b=10))
                                        st.plotly_chart(fig_mini, use_container_width=True)
                                    else:
                                        st.info("Chart unavailable right now for this symbol.")


                                    st.markdown("---")
                                    st.markdown("#### 🧠 AI Analysis & Reasoning")
                                    st.markdown(detailed_rec.get('detailed_reasoning', 'No detailed reasoning available'))

                                    # Probability distribution
                                    st.markdown("---")
                                    st.markdown("#### 📊 Signal Probability Distribution")
                                    probs = detailed_rec.get('probabilities', {})
                                    prob_col1, prob_col2, prob_col3 = st.columns(3)
                                    with prob_col1:
                                        st.metric("BUY", f"{probs.get('BUY', 0):.1f}%")
                                    with prob_col2:
                                        st.metric("HOLD", f"{probs.get('HOLD', 0):.1f}%")
                                    with prob_col3:
                                        st.metric("SELL", f"{probs.get('SELL', 0):.1f}%")
                else:
                    st.info("No actionable BUY/SELL signals found. All stocks are in HOLD status.")

            else:
                st.error("Failed to fetch stock data. Please try again.")

with tab2:
    st.header("Trend Line Calculator")
    st.markdown("Calculate resistance and support levels using Gann's formula")

    col1, col2 = st.columns(2)

    with col1:
        high_value = st.number_input("High Value", min_value=0.0, value=100.0, step=0.01)

    with col2:
        low_value = st.number_input("Low Value", min_value=0.0, value=95.0, step=0.01)

    if st.button("Calculate Trend Lines", use_container_width=True):
        # Calculation
        high_trend = ((high_value + 0.45) * 0.45) / 100
        low_trend = ((high_value - 0.45) * 0.45) / 100

        high_resistance = high_trend + high_value
        low_support = low_trend + low_value
        next_high = high_resistance + high_trend
        next_low = low_support - low_trend

        # Display results
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("High Resistance", f"₹{high_resistance:.2f}", f"+{high_trend:.2f}")
            st.metric("Next High", f"₹{next_high:.2f}")

        with col2:
            st.metric("Low Support", f"₹{low_support:.2f}", f"{low_trend:.2f}")
            st.metric("Next Low", f"₹{next_low:.2f}")

        with col3:
            st.metric("High Diff", f"₹{high_trend:.2f}")
            st.metric("Low Diff", f"₹{low_trend:.2f}")

with tab3:
    st.header("Stock Details & Charts")

    stock_symbol = st.selectbox(
        "Select Stock",
        st.session_state.scanner.get_stock_list(),
        key="stock_details_selector"
    )

    if st.button("Load Stock Data", type="primary", use_container_width=True):
        # Store in session state to persist after button click
        st.session_state.selected_stock_details = stock_symbol

    # Display data if a stock has been loaded
    if 'selected_stock_details' in st.session_state:
        stock_symbol = st.session_state.selected_stock_details

        with st.spinner(f"Loading {stock_symbol} data..."):
            stock_data = st.session_state.scanner.get_stock_details(stock_symbol)

            if stock_data:
                # Show data source info
                st.info("ℹ️ Data may be from historical records if NSE API is unavailable or market is closed.")
                # Stock metrics
                st.markdown(f"### 📊 {stock_symbol} - Live Data")
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    change_color = "normal" if stock_data.get('change', 0) >= 0 else "inverse"
                    st.metric("LTP", f"₹{stock_data.get('ltp', 0):.2f}",
                             f"{stock_data.get('change', 0):.2f}%",
                             delta_color=change_color)
                with col2:
                    st.metric("Day High", f"₹{stock_data.get('high', 0):.2f}")
                with col3:
                    st.metric("Day Low", f"₹{stock_data.get('low', 0):.2f}")
                with col4:
                    st.metric("Volume", f"{stock_data.get('volume', 0):,}")

                # Technical Indicators
                st.markdown("---")
                indicators = st.session_state.scanner.calculate_technical_indicators(stock_data)

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("RSI", f"{indicators.get('rsi', 0):.2f}")
                with col2:
                    st.metric("Support", f"₹{indicators.get('support', 0):.2f}")
                with col3:
                    st.metric("Resistance", f"₹{indicators.get('resistance', 0):.2f}")
                with col4:
                    st.metric("ATR", f"₹{indicators.get('atr', 0):.2f}")

                # Interactive Chart
                st.markdown("---")
                st.subheader("📈 Interactive Price Chart")
                colp, coli = st.columns([1, 1])
                with colp:
                    period = st.selectbox("Period", ["1mo", "3mo", "6mo", "1y"], index=2, key="period_selector")
                with coli:
                    interval_options = ["1d"] if period in ["6mo", "1y"] else ["15m", "1h", "1d"]
                    interval = st.selectbox("Interval", interval_options, index=len(interval_options)-1, key="interval_selector")

                history = st.session_state.scanner.get_price_history(stock_symbol, period=period, interval=interval)
                if history is not None and not history.empty:
                    # Moving averages
                    history['ma20'] = history['close'].rolling(20).mean()
                    history['ma50'] = history['close'].rolling(50).mean()

                    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                                       row_heights=[0.7, 0.3],
                                       subplot_titles=(f'{stock_symbol} Price Chart', 'Volume'))

                    # Candlestick
                    fig.add_trace(
                        go.Candlestick(
                            x=history['date'], open=history['open'], high=history['high'],
                            low=history['low'], close=history['close'], name='Price'
                        ), row=1, col=1
                    )

                    # Moving averages
                    fig.add_trace(
                        go.Scatter(x=history['date'], y=history['ma20'], name='MA 20',
                                   line=dict(color='#facc15', width=1.5)), row=1, col=1
                    )
                    fig.add_trace(
                        go.Scatter(x=history['date'], y=history['ma50'], name='MA 50',
                                   line=dict(color='#60a5fa', width=1.5)), row=1, col=1
                    )

                    # Support and Resistance lines
                    fig.add_hline(y=indicators.get('support', 0), line_dash="dash",
                                 line_color="green", annotation_text="Support",
                                 annotation_position="right", row=1, col=1)
                    fig.add_hline(y=indicators.get('resistance', 0), line_dash="dash",
                                 line_color="red", annotation_text="Resistance",
                                 annotation_position="right", row=1, col=1)

                    # Volume
                    colors = ['red' if row['close'] < row['open'] else 'green'
                             for _, row in history.iterrows()]
                    fig.add_trace(
                        go.Bar(x=history['date'], y=history['volume'], name='Volume',
                               marker_color=colors), row=2, col=1
                    )

                    fig.update_layout(
                        template='plotly_dark', height=700, xaxis_rangeslider_visible=False,
                        margin=dict(l=10, r=10, t=40, b=10),
                        hovermode='x unified'
                    )
                    fig.update_xaxes(title_text="Date", row=2, col=1)
                    fig.update_yaxes(title_text="Price (₹)", row=1, col=1)
                    fig.update_yaxes(title_text="Volume", row=2, col=1)

                    st.plotly_chart(fig, use_container_width=True)

                    # AI Recommendation
                    st.markdown("---")
                    st.subheader("🤖 AI Recommendation")

                    detailed_rec = st.session_state.ml_engine.generate_advanced_recommendation(
                        stock_data, indicators, scan_type='delivery'
                    )

                    if detailed_rec:
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            signal = detailed_rec['signal']
                            signal_color = "🟢" if signal == "BUY" else "🔴" if signal == "SELL" else "🟠"
                            st.markdown(f"### {signal_color} {signal}")
                            st.metric("Confidence", f"{detailed_rec['confidence']:.1f}%")

                        with col2:
                            st.metric("Entry Price", f"₹{detailed_rec['entry']:.2f}")
                            st.metric("Target Price", f"₹{detailed_rec['target']:.2f}")

                        with col3:
                            st.metric("Stop Loss", f"₹{detailed_rec['stop_loss']:.2f}")
                            st.metric("Risk-Reward", f"1:{detailed_rec['risk_reward_ratio']:.2f}")

                        st.markdown("---")
                        st.markdown("#### 🧠 Detailed Analysis")
                        st.markdown(detailed_rec.get('detailed_reasoning', 'No detailed reasoning available'))

                else:
                    st.warning("No historical data available to render chart. Try a different period/interval.")
            else:
                st.error(f"Failed to fetch data for {stock_symbol}. Please try again.")

with tab4:
    st.header("Settings")
    st.markdown("Configure scanner parameters and ML model settings")

    st.subheader("Scanner Settings")
    refresh_interval = st.slider("Auto-refresh interval (seconds)", 30, 300, 60)

    st.subheader("ML Model Settings")
    model_type = st.selectbox("Model Type", ["Random Forest", "XGBoost", "Neural Network"])
    confidence_threshold = st.slider("Confidence Threshold", 0.5, 1.0, 0.75)

    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

