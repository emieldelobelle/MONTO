import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import requests
import streamlit as st

class MontoStrategy:
    def __init__(self):
        self.monthly_target = 1500
        self.iwda_allocation = 0.67  # 67% IWDA
        self.btc_allocation = 0.33   # 33% BTC

    def get_market_data(self):
        """Fetch basic market data"""
        try:
            print("Fetching market data...")
            
            # Basic price data
            iwda = yf.Ticker("IWDA.AS")
            btc = yf.Ticker("BTC-USD")
            usd_eur = yf.Ticker("EURUSD=X")

            iwda_data = iwda.history(period="1mo")
            btc_data = btc.history(period="1mo")
            usd_eur_rate = 1 / usd_eur.history(period="1d")['Close'].iloc[-1]

            # Fear & Greed indices
            try:
                # Bitcoin Fear & Greed
                crypto_response = requests.get("https://api.alternative.me/fng/?limit=1")
                btc_fear_greed = float(crypto_response.json()['data'][0]['value'])
            except:
                btc_fear_greed = 50  # Neutral if API fails

            return {
                'iwda_price': iwda_data['Close'].iloc[-1],
                'btc_price': btc_data['Close'].iloc[-1],
                'usd_eur_rate': usd_eur_rate,
                'btc_fear_greed': btc_fear_greed
            }
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def calculate_allocation(self, data):
        """Calculate investment allocation"""
        if not data:
            return None

        # Bitcoin allocation based on fear & greed
        btc_fear_greed = data['btc_fear_greed']
        
        if btc_fear_greed <= 20:  # Extreme fear
            btc_multiplier = 2.0
            btc_max = 1000
            regime = "EXTREME_FEAR"
        elif btc_fear_greed >= 80:  # Extreme greed
            btc_multiplier = 0.2
            btc_max = 200
            regime = "EXTREME_GREED"
        else:  # Normal conditions
            btc_multiplier = 1.0
            btc_max = 500
            regime = "NEUTRAL"

        # Calculate amounts
        btc_amount = min(self.monthly_target * self.btc_allocation * btc_multiplier, btc_max)
        iwda_amount = self.monthly_target * self.iwda_allocation

        # Calculate IWDA shares
        iwda_shares = int(iwda_amount / data['iwda_price'])
        iwda_actual = iwda_shares * data['iwda_price']

        # Convert BTC price to EUR
        btc_eur = data['btc_price'] * data['usd_eur_rate']

        return {
            'regime': regime,
            'iwda_shares': iwda_shares,
            'iwda_amount': iwda_actual,
            'btc_amount': btc_amount,
            'total_investment': iwda_actual + btc_amount,
            'prices': {
                'iwda_eur': data['iwda_price'],
                'btc_eur': btc_eur
            }
        }

def run_streamlit_app():
    st.set_page_config(page_title="MONTO", page_icon="💰")
    st.title("MONTO Investment Planner")

    monthly_amount = st.number_input(
        "Monthly Investment Amount (€)",
        min_value=100,
        max_value=10000,
        value=1500
    )

    if st.button("Generate Plan", type="primary"):
        with st.spinner("Analyzing market conditions..."):
            strategy = MontoStrategy()
            strategy.monthly_target = monthly_amount
            
            data = strategy.get_market_data()
            if data:
                allocation = strategy.calculate_allocation(data)
                
                if allocation:
                    # Market Overview
                    st.header("📊 Market Overview")
                    st.metric("Bitcoin Fear & Greed", f"{data['btc_fear_greed']:.0f}/100")
                    st.metric("Market Regime", allocation['regime'])

                    # Investment Plan
                    st.header("💰 Investment Plan")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("IWDA ETF")
                        st.write(f"Buy {allocation['iwda_shares']} shares")
                        st.write(f"Total: €{allocation['iwda_amount']:,.2f}")
                        st.write(f"Price: €{allocation['prices']['iwda_eur']:.2f}")
                    
                    with col2:
                        st.subheader("Bitcoin")
                        st.write(f"Invest: €{allocation['btc_amount']:,.2f}")
                        st.write(f"Price: €{allocation['prices']['btc_eur']:,.2f}")

                    # Execution Tips
                    st.header("💡 Tips")
                    st.info("""
                    • Execute between 15-25th of the month
                    • Use limit orders when possible
                    • Best trading hours: 14:30-22:00 CET
                    """)
            else:
                st.error("Could not fetch market data. Please try again.")

if __name__ == "__main__":
    run_streamlit_app()
