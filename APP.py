import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import warnings
from zoneinfo import ZoneInfo  # Add this with your other imports
warnings.filterwarnings('ignore')

class UltimateQuantStrategy:
    """
    MONTO 
    The Nuclear Option: Advanced Quantitative Strategy
    Combines the simplicity of the original 3-5 component system
    with cutting-edge mathematical optimization
    """

    def __init__(self):
        # Core strategy parameters (keeping your brilliant base)
        self.monthly_target = 1500
        self.component_size = 300
        self.iwda_components = 3.33  # 1000/300
        self.btc_components = 1.67   # 500/300
        self.max_buffer_months = 8

        # Advanced quantitative parameters
        self.lookback_window = 252  # 1 year
        self.vol_lookback = 21     # Volatility window
        self.confidence_level = 0.95

        # Market regime thresholds (mathematically optimized)
        self.regime_thresholds = {
            'extreme_fear': -2.0,    # 2 std dev below mean
            'fear': -1.0,            # 1 std dev below mean
            'neutral': 0.0,
            'greed': 1.0,            # 1 std dev above mean
            'extreme_greed': 2.0     # 2 std dev above mean
        }

        # Kelly Criterion parameters
        self.max_kelly_fraction = 0.25  # Never risk more than 25%

        # Load historical performance data
        self.performance_history = self.load_performance_data()

    def load_performance_data(self):
        """Load historical strategy performance for optimization"""
        try:
            with open('strategy_performance.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"monthly_returns": [], "strategy_stats": {}}

    def get_market_data_optimized(self):
        """Fetch market data including Fear & Greed indices"""
        try:
            # Get IWDA and Bitcoin data
            print("Fetching market prices...")
            iwda = yf.Ticker("IWDA.AS")  # IWDA on Amsterdam exchange
            btc = yf.Ticker("BTC-USD")
            vix = yf.Ticker("^VIX")
            usd_eur = yf.Ticker("EURUSD=X")

            # Get 2 years of data
            period = "2y"
            iwda_data = iwda.history(period=period)
            btc_data = btc.history(period=period)
            vix_data = vix.history(period=period)
            usd_eur_data = usd_eur.history(period="1d")

            import requests

            try:
                # CNN Fear & Greed for S&P 500
                print("Fetching S&P500 Fear & Greed Index...")
                cnn_url = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    'Accept': 'application/json'
                }
                cnn_response = requests.get(cnn_url, headers=headers)
                cnn_data = cnn_response.json()
                sp500_fear_greed = float(cnn_data['fear_and_greed']['score'])
                print(f"S&P500 Fear & Greed: {sp500_fear_greed:.1f}")

            except Exception as e:
                print(f"CNN API error: {e}, using fallback calculation")
                # Fallback calculation
                sp500_fear_greed = 50  # Neutral stance if API fails

            try:
                # Alternative.me Fear & Greed for Bitcoin
                print("Fetching Bitcoin Fear & Greed Index...")
                crypto_url = "https://api.alternative.me/fng/?limit=1"
                crypto_response = requests.get(crypto_url)
                crypto_data = crypto_response.json()

                # Extract value from the response
                btc_fear_greed = float(crypto_data['data'][0]['value'])
                print(f"Bitcoin Fear & Greed: {btc_fear_greed:.1f}")

            except Exception as e:
                print(f"Crypto API error: {e}, using fallback calculation")
                btc_fear_greed = 50  # Neutral stance if API fails

            # Get current USD/EUR rate (invert for correct conversion)
            usd_eur_rate = 1 / usd_eur_data['Close'].iloc[-1]
            print(f"USD/EUR Rate: {usd_eur_rate:.4f}")

            return {
                'iwda': iwda_data,
                'btc': btc_data,
                'vix': vix_data,
                'sp500_fear_greed': sp500_fear_greed,
                'btc_fear_greed': btc_fear_greed,
                'usd_eur_rate': usd_eur_rate,
                'fetch_time': datetime.now()
            }

        except Exception as e:
            print(f"Critical data fetch error: {str(e)}")
            return None

    def calculate_statistical_regime(self, data):
        """
        Use actual Fear & Greed indices and handle USD/EUR conversion
        """
        # Get Fear & Greed scores (0-100 scale)
        sp500_fear_greed = data['sp500_fear_greed']
        btc_fear_greed = data['btc_fear_greed']

        # Convert to z-scores (-3 to +3 scale approximately)
        # 50 is neutral, 25 is fear, 75 is greed
        sp500_zscore = (sp500_fear_greed - 50) / 25
        btc_zscore = (btc_fear_greed - 50) / 25

        # Get USD/EUR conversion for amount calculations
        usd_eur_rate = data['usd_eur_rate']

        # Calculate other metrics
        iwda_prices = data['iwda']['Close']
        btc_prices = data['btc']['Close']
        vix_prices = data['vix']['Close']

        # Price metrics vs moving averages
        iwda_current = iwda_prices.iloc[-1]
        iwda_ma200 = iwda_prices.rolling(200).mean().iloc[-1]

        btc_current = btc_prices.iloc[-1]
        btc_ma200 = btc_prices.rolling(200).mean().iloc[-1]

        # VIX metrics
        vix_current = vix_prices.iloc[-1]
        vix_mean = vix_prices.rolling(252).mean().iloc[-1]
        vix_std = vix_prices.rolling(252).std().iloc[-1]
        vix_zscore = (vix_current - vix_mean) / vix_std

        # Composite score using actual fear & greed indices
        composite_score = (-sp500_zscore - btc_zscore + vix_zscore) / 3

        return {
            'composite_score': composite_score,
            'sp500_fear_greed': sp500_fear_greed,
            'btc_fear_greed': btc_fear_greed,
            'vix_zscore': vix_zscore,
            'iwda_vs_ma200': (iwda_current / iwda_ma200 - 1) * 100,
            'btc_vs_ma200': (btc_current / btc_ma200 - 1) * 100,
            'vix_level': vix_current,
            'usd_eur_rate': usd_eur_rate
        }

    def calculate_kelly_criterion(self, data):
        """Kelly Criterion met numpy ipv scipy"""
        iwda_returns = data['iwda']['Close'].pct_change().dropna()
        btc_returns = data['btc']['Close'].pct_change().dropna()

        # Calculate historical statistics using numpy
        iwda_mean = iwda_returns.mean() * 252
        iwda_std = iwda_returns.std() * np.sqrt(252)
        iwda_sharpe = iwda_mean / iwda_std if iwda_std > 0 else 0

        btc_mean = btc_returns.mean() * 252
        btc_std = btc_returns.std() * np.sqrt(252)
        btc_sharpe = btc_mean / btc_std if btc_std > 0 else 0

        # Simplified Kelly calculation
        iwda_kelly = max(0, min(iwda_sharpe / iwda_std if iwda_std > 0 else 0, self.max_kelly_fraction))
        btc_kelly = max(0, min(btc_sharpe / btc_std if btc_std > 0 else 0, self.max_kelly_fraction))

        return {
            'iwda_kelly': iwda_kelly,
            'btc_kelly': btc_kelly,
            'iwda_sharpe': iwda_sharpe,
            'btc_sharpe': btc_sharpe
        }

    def calculate_value_at_risk(self, data, confidence_level=0.95):
        """
        Value at Risk: Maximum expected loss at given confidence level
        Used to size positions appropriately
        """
        iwda_returns = data['iwda']['Close'].pct_change().dropna().tail(252)
        btc_returns = data['btc']['Close'].pct_change().dropna().tail(252)

        # Calculate VaR
        iwda_var = np.percentile(iwda_returns, (1 - confidence_level) * 100)
        btc_var = np.percentile(btc_returns, (1 - confidence_level) * 100)

        return {
            'iwda_var': iwda_var,
            'btc_var': btc_var,
            'iwda_vol': iwda_returns.std() * np.sqrt(252),
            'btc_vol': btc_returns.std() * np.sqrt(252)
        }

    def optimize_portfolio_allocation(self, regime_data, kelly_data, var_data, data):
        # Base allocation (keep IWDA stable, vary BTC more aggressively)
        btc_fear_greed = regime_data['btc_fear_greed']
        sp500_greed = regime_data['sp500_fear_greed'] > 65

        # Default allocations (67% IWDA, 33% BTC)
        iwda_allocation = 0.67
        btc_allocation = 0.33

        # Bitcoin-specific multipliers based on crypto fear & greed
        if btc_fear_greed <= 20:  # Extreme fear in crypto
            btc_multiplier = 2.5
            btc_max = 1000
            regime = "CRYPTO_EXTREME_FEAR"
            print("💡 CRYPTO OPPORTUNITY: Extreme fear signals potential buying opportunity")
        elif btc_fear_greed <= 35:  # Fear
            btc_multiplier = 1.8
            btc_max = 750
            regime = "CRYPTO_FEAR"
        elif btc_fear_greed >= 80:  # Extreme greed
            btc_multiplier = 0.2
            btc_max = 200
            regime = "CRYPTO_EXTREME_GREED"
            print("🚨 CRYPTO WARNING: Consider taking profits on existing positions")
        elif btc_fear_greed >= 65:  # Greed
            btc_multiplier = 0.4
            btc_max = 300
            regime = "CRYPTO_GREED"
        else:  # Neutral
            btc_multiplier = 1.0
            btc_max = 500
            regime = "CRYPTO_NEUTRAL"

        # IWDA optimalisatie op basis van meerdere factoren
        iwda_signals = {
            'sp500_fear': regime_data['sp500_fear_greed'] <= 35,
            'vix_high': regime_data['vix_level'] > 25,
            'price_vs_ma': regime_data['iwda_vs_ma200'] < -5,  # 5% onder MA200
        }

        # Tel aantal bearish signalen
        bearish_signals = sum(iwda_signals.values())

        # IWDA allocatie aanpassen
        if bearish_signals >= 2:  # Meerdere bear signalen
            iwda_multiplier = 1.2
            iwda_message = "💡 IWDA OPPORTUNITY: Multiple bearish signals - increasing allocation"
        elif sp500_greed:
            iwda_multiplier = 0.8
            iwda_message = "⚠️ IWDA CAUTION: Market showing greed - reducing exposure"
        else:
            iwda_multiplier = 1.0
            iwda_message = None

        # Calculate investments
        iwda_target = self.monthly_target * iwda_multiplier * iwda_allocation
        btc_target = min(self.monthly_target * btc_multiplier * btc_allocation, btc_max)

        # Calculate actual IWDA shares
        iwda_price_eur = data['iwda']['Close'].iloc[-1]
        iwda_shares = int(iwda_target / iwda_price_eur)
        iwda_amount = iwda_shares * iwda_price_eur

        if iwda_message:
            print(iwda_message)

        return {
            'iwda_amount': int(iwda_amount),
            'iwda_shares': iwda_shares,
            'iwda_signals': iwda_signals,
            'btc_amount': int(btc_target),
            'total_investment': int(iwda_amount + btc_target),
            'regime': regime,
            'btc_fear_greed_level': btc_fear_greed,
            'component_count': 2,
            'kelly_optimization': {
                'iwda_weight': iwda_allocation,
                'btc_weight': btc_allocation,
                'iwda_kelly': kelly_data['iwda_kelly'],
                'btc_kelly': kelly_data['btc_kelly']
            }
        }

    def calculate_expected_returns(self, allocation, var_data):
        """Calculate expected returns and risk metrics"""
        # Portfolio expected return (simplified)
        portfolio_weights = np.array([allocation['kelly_optimization']['iwda_weight'],
                                    allocation['kelly_optimization']['btc_weight']])

        # Expected annual returns (historical averages)
        expected_returns = np.array([0.08, 0.15])  # 8% IWDA, 15% BTC historical

        portfolio_return = np.dot(portfolio_weights, expected_returns)

        # Portfolio risk (simplified - assumes some correlation)
        portfolio_risk = np.sqrt(
            (portfolio_weights[0] ** 2) * (var_data['iwda_vol'] ** 2) +
            (portfolio_weights[1] ** 2) * (var_data['btc_vol'] ** 2) +
            2 * portfolio_weights[0] * portfolio_weights[1] *
            var_data['iwda_vol'] * var_data['btc_vol'] * 0.3  # Assume 30% correlation
        )

        sharpe_ratio = portfolio_return / portfolio_risk if portfolio_risk > 0 else 0

        return {
            'expected_annual_return': portfolio_return,
            'expected_annual_risk': portfolio_risk,
            'sharpe_ratio': sharpe_ratio
        }

    def generate_ultimate_recommendation(self):
        """Generate the ultimate quantitative recommendation"""
        print("🧮 ULTIMATE QUANTITATIVE ANALYSIS INITIATED...")
        print("📊 Fetching market data...")

        # Get market data
        data = self.get_market_data_optimized()
        if not data:
            return None

        print("📈 Calculating statistical regime...")
        regime_data = self.calculate_statistical_regime(data)

        print("🎯 Applying Kelly Criterion optimization...")
        kelly_data = self.calculate_kelly_criterion(data)

        print("⚠️  Computing Value at Risk...")
        var_data = self.calculate_value_at_risk(data)

        print("🚀 Optimizing portfolio allocation...")
        allocation = self.optimize_portfolio_allocation(regime_data, kelly_data, var_data, data)  # Add data parameter

        print("💰 Calculating expected returns...")
        performance = self.calculate_expected_returns(allocation, var_data)

        # Compile comprehensive recommendation
        recommendation = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'market_regime': {
                'regime': allocation['regime'],
                'composite_score': regime_data['composite_score'],
                'sp500_fear_greed': data['sp500_fear_greed'],
                'btc_fear_greed': data['btc_fear_greed'],
                'btc_fear_greed_level': data['btc_fear_greed'],  # Add this line
                'usd_eur_rate': data['usd_eur_rate'],
                'iwda_vs_ma200': regime_data['iwda_vs_ma200'],
                'btc_vs_ma200': regime_data['btc_vs_ma200'],
                'vix_level': regime_data['vix_level']
            },
            'allocation': allocation,
            'risk_metrics': {
                'iwda_var_95': var_data['iwda_var'],
                'btc_var_95': var_data['btc_var'],
                'iwda_volatility': var_data['iwda_vol'],
                'btc_volatility': var_data['btc_vol']
            },
            'performance_forecast': performance,
            'current_prices': {
                'iwda_proxy': data['iwda']['Close'].iloc[-1],
                'btc': data['btc']['Close'].iloc[-1],
                'vix': data['vix']['Close'].iloc[-1]
            }
        }

        return recommendation

    def convert_to_brussels_time(self, timestamp):
        """Convert timestamp to Brussels time (CET/CEST)"""
        from datetime import datetime
        from zoneinfo import ZoneInfo
        
        # Convert string timestamp to datetime object
        dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        
        # Convert to Brussels time
        brussels_time = dt.astimezone(ZoneInfo("Europe/Brussels"))
        return brussels_time.strftime('%Y-%m-%d %H:%M:%S %Z')

    def display_ultimate_analysis(self, rec):
        """Display clear investment instructions"""
        print("\n" + "="*80)
        print("💰 MONTHLY INVESTMENT RECOMMENDATION")
        print("="*80)

        # Current market conditions with Brussels time
        brussels_time = self.convert_to_brussels_time(rec['timestamp'])
        print(f"\n📊 MARKET CONDITIONS ({brussels_time}):")
        print(f"• Market Regime: {rec['market_regime']['regime']}")
        print(f"• S&P500 Fear & Greed: {rec['market_regime']['sp500_fear_greed']}/100")
        print(f"• Bitcoin Fear & Greed: {rec['market_regime']['btc_fear_greed']}/100")
        print(f"• USD/EUR Rate: {rec['market_regime']['usd_eur_rate']:.4f}")

        # Clear investment instructions
        print(f"\n🎯 INVESTMENT ACTIONS REQUIRED:")
        print(f"1. IWDA ETF (DEGIRO):")
        print(f"   → Buy: {rec['allocation']['iwda_shares']} shares")
        print(f"   → Total Investment: €{rec['allocation']['iwda_amount']:,}")
        print(f"   → Current Price: €{rec['current_prices']['iwda_proxy']:.2f}")

        print(f"\n2. Bitcoin (Bitvavo):")
        print(f"   → Invest: €{rec['allocation']['btc_amount']:,}")
        print(f"   → Current Price: ${rec['current_prices']['btc']:,.0f}")
        print(f"   → EUR Price: €{rec['current_prices']['btc'] * rec['market_regime']['usd_eur_rate']:,.0f}")

        print(f"\n💡 EXECUTION INSTRUCTIONS:")
        print(f"• Total to Invest This Month: €{rec['allocation']['total_investment']:,}")
        print(f"• Number of Components: {rec['allocation']['component_count']}")
        print(f"• Execute Between: 15-25th of the month")
        print(f"• Use Limit Orders at Current Prices")

        # Enhanced Risk Assessment
        print(f"\n⚠️  RISK ASSESSMENT:")
        print(f"• Portfolio Risk Level: {rec['market_regime']['regime']}")
        print(f"• Value at Risk (95% confidence):")
        print(f"  - IWDA: {rec['risk_metrics']['iwda_var_95']*100:.1f}% daily")
        print(f"  - Bitcoin: {rec['risk_metrics']['btc_var_95']*100:.1f}% daily")
        print(f"• Annual Volatility:")
        print(f"  - IWDA: {rec['risk_metrics']['iwda_volatility']*100:.1f}%")
        print(f"  - Bitcoin: {rec['risk_metrics']['btc_volatility']*100:.1f}%")
        print(f"• Portfolio Metrics:")
        print(f"  - Expected Return: {rec['performance_forecast']['expected_annual_return']*100:.1f}%")
        print(f"  - Expected Risk: {rec['performance_forecast']['expected_annual_risk']*100:.1f}%")
        print(f"  - Sharpe Ratio: {rec['performance_forecast']['sharpe_ratio']:.2f}")

        # Market Specific Warnings
        if rec['market_regime']['regime'] == "EXTREME_GREED":
            print("\n🚨 RISK WARNINGS:")
            print("  • Markets showing extreme greed - high risk of correction")
            print("  • Using defensive allocation with reduced exposure")
            print("  • Consider splitting purchases over multiple weeks")
        elif rec['market_regime']['regime'] == "GREED":
            print("\n🚨 RISK WARNINGS:")
            print("  • Markets showing greed - elevated risk levels")
            print("  • Bitcoin capped at €500 for risk management")
            print("  • Consider using limit orders below market price")
        elif rec['market_regime']['regime'] == "EXTREME_FEAR":
            print("\n💡 OPPORTUNITY ALERT:")
            print("  • Markets in extreme fear - potential buying opportunity")
            print("  • Still maintain position sizing discipline")
            print("  • Consider gradual scaling in over several days")

        # Add Bitcoin-specific advice
        btc_advice = self.get_btc_position_advice(rec['market_regime']['btc_fear_greed'])  # Changed this line
        if btc_advice:
            print("\n🔷 BITCOIN POSITION ADVICE:")
            for msg in btc_advice['message']:
                print(f"  {msg}")

        # Add after current market conditions
        if rec['allocation']['iwda_signals']['sp500_fear'] or \
           rec['allocation']['iwda_signals']['vix_high'] or \
           rec['allocation']['iwda_signals']['price_vs_ma']:
            print("\n📈 IWDA MARKET SIGNALS:")
            if rec['allocation']['iwda_signals']['sp500_fear']:
                print("  • S&P500 showing fear - potential buying opportunity")
            if rec['allocation']['iwda_signals']['vix_high']:
                print("  • VIX elevated - market uncertainty high")
            if rec['allocation']['iwda_signals']['price_vs_ma']:
                print("  • IWDA trading below 200-day moving average")

        # Add after risk assessment section
        print("\n📍 SUGGESTED ORDER PLACEMENT:")
        entry_points = self.analyze_optimal_entry_points(
            {
                'btc': rec['current_prices']['btc'],
                'iwda': rec['current_prices']['iwda_proxy']
            }, 
            rec['allocation']
        )

        print("\nIWDA Orders:")
        for order in entry_points['iwda_orders']:
            print(f"  • {order['type']} Order: {order['size']}% @ €{order['price']:.2f} " 
                  f"({order['confidence']} confidence)")
        
        print("\nBitcoin Orders:")
        for order in entry_points['btc_orders']:
            eur_price = order['price'] * rec['market_regime']['usd_eur_rate']
            print(f"  • {order['type']} Order: {order['size']}% @ €{eur_price:.0f} " 
                  f"({order['confidence']} confidence)")

        print("\n💡 ORDER EXECUTION TIPS:")
        print("  • Use Good-til-Cancelled (GTC) for limit orders")
        print("  • Place orders during high liquidity hours (14:30-22:00 CET)")
        print("  • Monitor order fills and adjust if needed after 48 hours")
        print("  • Consider cancelling unfilled orders after 5 trading days")

        print("\n" + "="*80)
        return rec

    def get_btc_position_advice(self, btc_fear_greed):
        """Generate Bitcoin-specific position advice"""
        if btc_fear_greed >= 80:
            return {
                'action': 'TAKE_PROFIT',
                'message': [
                    "🚨 BITCOIN EXTREME GREED ALERT:",
                    "• Consider taking partial profits (20-30%) on existing positions",
                    "• Set trailing stop losses on remaining position",
                    "• Minimal new investment recommended"
                ]
            }
        elif btc_fear_greed <= 20:
            return {
                'action': 'ACCUMULATE',
                'message': [
                    "💰 BITCOIN OPPORTUNITY ALERT:",
                    "• Significant fear presents buying opportunity",
                    "• Consider scaling in over several days",
                    "• Increased position size recommended"
                ]
            }
        return None

    def analyze_optimal_entry_points(self, prices, allocation):
        """Analyze optimal entry points based on liquidity zones and market structure"""
        btc_current = prices['btc']  # Now expecting a simple price value
        iwda_current = prices['iwda']  # Now expecting a simple price value
        
        def calculate_zones(current_price, volatility_factor=0.02):
            """Calculate price zones based on current price and volatility"""
            return {
                'support_1': current_price * (1 - volatility_factor),
                'support_2': current_price * (1 - volatility_factor * 2),
                'resistance_1': current_price * (1 + volatility_factor),
                'resistance_2': current_price * (1 + volatility_factor * 2)
            }
        
        btc_zones = calculate_zones(btc_current, 0.03)  # Higher volatility for BTC
        iwda_zones = calculate_zones(iwda_current, 0.01)  # Lower volatility for IWDA
        
        def get_order_strategy(current_price, zones, asset_type):
            # Base order distribution
            if asset_type == 'BTC':
                chunks = 4 if allocation['regime'] in ['CRYPTO_EXTREME_FEAR', 'CRYPTO_FEAR'] else 2
            else:
                chunks = 3 if allocation['iwda_signals']['sp500_fear'] else 2
                
            orders = []
            
            # Market order at current price
            market_order = {
                'price': round(current_price, 2),
                'size': round(100/chunks, 1),
                'type': 'Market',
                'confidence': 'High'
            }
            
            # Limit order at first support
            support_1_order = {
                'price': round(zones['support_1'], 2),
                'size': round(100/chunks, 1),
                'type': 'Limit',
                'confidence': 'High'
            }
            
            # Limit order at second support
            support_2_order = {
                'price': round(zones['support_2'], 2),
                'size': round(100/chunks, 1),
                'type': 'Limit',
                'confidence': 'Medium'
            }
            
            orders.extend([market_order, support_1_order, support_2_order])
            return orders

        return {
            'btc_orders': get_order_strategy(btc_current, btc_zones, 'BTC'),
            'iwda_orders': get_order_strategy(iwda_current, iwda_zones, 'IWDA'),
            'btc_zones': btc_zones,
            'iwda_zones': iwda_zones
        }

    def calculate_adaptive_volatility(self, data, window=21):
        """Dynamische volatiliteit op basis van recente marktcondities"""
        atr = self.calculate_atr(data, window)
        return {
            'btc_vol': max(0.03, min(0.05, atr['btc'])),  # 3-5% range
            'iwda_vol': max(0.01, min(0.02, atr['iwda']))  # 1-2% range
        }

    def optimize_execution_timing(self, data):
        """Bepaal beste uitvoeringstijden op basis van volume"""
        return {
            'best_hours': ['14:30-16:30', '20:00-22:00'],
            'avoid_hours': ['12:00-14:00', '22:00-06:00'],
            'volume_threshold': 'Wacht met grote orders tot volume > gemiddeld'
        }

# Ultimate usage
def run_streamlit_interface():
    import streamlit as st
    
    st.set_page_config(page_title="MONTO - Smart Money, Zero Stress", page_icon="💰", layout="wide")
    
    # Header
    st.title("MONTO")
    st.subheader("Your Monthly Money Multiplier")
    
    # Sidebar input
    with st.sidebar:
        monthly_amount = st.number_input(
            "Monthly Investment Amount (€)",
            min_value=100,
            max_value=10000,
            value=1500,
            step=100
        )
    
    if st.button("Generate Investment Plan", type="primary"):
        with st.spinner("Analyzing market conditions..."):
            strategy = UltimateQuantStrategy()
            strategy.monthly_target = monthly_amount
            recommendation = strategy.generate_ultimate_recommendation()
            
            if recommendation:
                # Market Overview
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("S&P500 Fear & Greed", 
                             f"{recommendation['market_regime']['sp500_fear_greed']}/100")
                with col2:
                    st.metric("Bitcoin Fear & Greed", 
                             f"{recommendation['market_regime']['btc_fear_greed']}/100")
                with col3:
                    st.metric("Market Regime", recommendation['market_regime']['regime'])
                
                # Investment Actions
                st.header("🎯 Investment Actions")
                
                # IWDA Box
                with st.expander("IWDA ETF Investment Plan", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Shares to Buy", recommendation['allocation']['iwda_shares'])
                        st.metric("Total Investment", f"€{recommendation['allocation']['iwda_amount']:,}")
                    with col2:
                        st.metric("Current Price", f"€{recommendation['current_prices']['iwda_proxy']:.2f}")
                        for order in recommendation['allocation']['iwda_orders']:
                            st.write(f"• {order['type']} Order: {order['size']}% @ €{order['price']:.2f}")
                
                # Bitcoin Box
                with st.expander("Bitcoin Investment Plan", expanded=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Amount to Invest", f"€{recommendation['allocation']['btc_amount']:,}")
                        btc_eur = recommendation['current_prices']['btc'] * recommendation['market_regime']['usd_eur_rate']
                        st.metric("Current Price (EUR)", f"€{btc_eur:,.0f}")
                    with col2:
                        st.metric("Market Sentiment", recommendation['allocation']['regime'])
                        for order in recommendation['allocation']['btc_orders']:
                            eur_price = order['price'] * recommendation['market_regime']['usd_eur_rate']
                            st.write(f"• {order['type']} Order: {order['size']}% @ €{eur_price:.0f}")
                
                # Risk Assessment
                st.header("⚠️ Risk Assessment")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Expected Annual Return", 
                             f"{recommendation['performance_forecast']['expected_annual_return']*100:.1f}%")
                    st.metric("Sharpe Ratio", 
                             f"{recommendation['performance_forecast']['sharpe_ratio']:.2f}")
                with col2:
                    st.metric("IWDA Volatility", 
                             f"{recommendation['risk_metrics']['iwda_volatility']*100:.1f}%")
                    st.metric("BTC Volatility", 
                             f"{recommendation['risk_metrics']['btc_volatility']*100:.1f}%")
                
                # Execution Tips
                st.header("💡 Execution Tips")
                st.info("""
                • Execute between 15-25th of the month
                • Use limit orders at suggested prices
                • Best trading hours: 14:30-22:00 CET
                • Monitor and adjust after 48 hours
                """)

# Update de main block
if __name__ == "__main__":
    import sys
    try:
        if "--streamlit" in sys.argv:
            run_streamlit_interface()
        else:
            print("🚀 Initializing Ultimate Quantitative Strategy...")
            quant_strategy = UltimateQuantStrategy()
            recommendation = quant_strategy.generate_ultimate_recommendation()
            if recommendation:
                quant_strategy.display_ultimate_analysis(recommendation)
    except Exception as e:
        print(f"Error: {str(e)}")
