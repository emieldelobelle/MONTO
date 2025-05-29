import streamlit as st
from APP import UltimateQuantStrategy

def main():
    st.set_page_config(
        page_title="MONTO - Smart Money, Zero Stress",
        page_icon="💰",
        layout="wide"
    )
    
    st.title("MONTO")
    st.subheader("Your Monthly Money Multiplier")
    
    monthly_amount = st.number_input(
        "Monthly Investment Amount (€)",
        min_value=100,
        max_value=10000,
        value=1500
    )
    
    if st.button("Generate Investment Plan"):
        strategy = UltimateQuantStrategy()
        strategy.monthly_target = monthly_amount
        recommendation = strategy.generate_ultimate_recommendation()
        display_results(recommendation)

if __name__ == "__main__":
    main()
