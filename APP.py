import streamlit as st
import sys
import os

# Voeg de huidige directory toe aan Python path
sys.path.append(os.path.dirname(__file__))

from APP import UltimateQuantStrategy

def main():
    st.set_page_config(
        page_title="MONTO - Smart Money, Zero Stress",
        page_icon="💰",
        layout="wide"
    )
    
    st.title("MONTO")
    st.subheader("Your Monthly Money Multiplier")
    
    try:
        monthly_amount = st.number_input(
            "Monthly Investment Amount (€)",
            min_value=100,
            max_value=10000,
            value=1500
        )
        
        if st.button("Generate Investment Plan"):
            with st.spinner("Analyzing market conditions..."):
                strategy = UltimateQuantStrategy()
                strategy.monthly_target = monthly_amount
                recommendation = strategy.generate_ultimate_recommendation()
                
                if recommendation:
                    display_results(recommendation)
                else:
                    st.error("Unable to fetch market data. Please try again.")
                    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def display_results(rec):
    # Market Conditions
    st.header("📊 Market Conditions")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("S&P500 Fear & Greed", 
                 f"{rec['market_regime']['sp500_fear_greed']}/100")
    with col2:
        st.metric("Bitcoin Fear & Greed", 
                 f"{rec['market_regime']['btc_fear_greed']}/100")

    # Investment Actions
    st.header("🎯 Investment Actions")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("IWDA ETF (DEGIRO)")
        st.write(f"Buy: {rec['allocation']['iwda_shares']} shares")
        st.write(f"Total: €{rec['allocation']['iwda_amount']:,}")
    with col2:
        st.subheader("Bitcoin (Bitvavo)")
        st.write(f"Invest: €{rec['allocation']['btc_amount']:,}")
        btc_eur = rec['current_prices']['btc'] * rec['market_regime']['usd_eur_rate']
        st.write(f"Current Price: €{btc_eur:,.0f}")

if __name__ == "__main__":
    main()
