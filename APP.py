import streamlit as st
import streamlit.components.v1 as components

def create_monto_website():
    html_content = """
    <style>
        /* ... bestaande styles behouden ... */
        
        /* Smooth scroll behavior */
        html {
            scroll-behavior: smooth;
        }

        /* Navigation styling */
        .nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(10, 25, 49, 0.9);
            backdrop-filter: blur(10px);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-logo {
            color: var(--light);
            font-size: 1.5rem;
            font-weight: 800;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-link {
            color: var(--light);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .nav-link:hover {
            color: var(--accent);
        }

        /* Algorithm section styling */
        .algorithm {
            background: var(--dark);
            color: var(--light);
            padding: 6rem 2rem;
        }

        .algo-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }

        .algo-card {
            background: rgba(255,255,255,0.1);
            padding: 2rem;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        .metric-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-top: 3rem;
        }

        .metric-card {
            background: var(--light);
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            color: var(--dark);
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 800;
            color: var(--primary);
            margin: 0.5rem 0;
        }

        /* Performance section */
        .performance {
            background: var(--gray);
            padding: 6rem 2rem;
        }

        .chart-container {
            background: var(--light);
            padding: 2rem;
            border-radius: 20px;
            margin-top: 2rem;
        }
    </style>

    <nav class="nav">
        <a href="#top" class="nav-logo">MONTO</a>
        <div class="nav-links">
            <a href="#features" class="nav-link">Features</a>
            <a href="#algorithm" class="nav-link">Algorithm</a>
            <a href="#performance" class="nav-link">Performance</a>
            <a href="#start" class="nav-link">Get Started</a>
        </div>
    </nav>

    <div class="hero" id="top">
        <!-- ... bestaande hero content ... -->
    </div>

    <section class="algorithm" id="algorithm">
        <h2>The MONTO Algorithm</h2>
        <div class="algo-grid">
            <div class="algo-card">
                <h3>Fear & Greed Index</h3>
                <p>Analyses market sentiment using multiple indicators:</p>
                <ul>
                    <li>Market Volatility (VIX)</li>
                    <li>Market Momentum</li>
                    <li>Stock Price Strength</li>
                    <li>Market Volume</li>
                </ul>
            </div>
            <div class="algo-card">
                <h3>Kelly Criterion</h3>
                <p>Optimal position sizing based on:</p>
                <ul>
                    <li>Win Probability</li>
                    <li>Risk/Reward Ratio</li>
                    <li>Maximum 25% Risk Cap</li>
                    <li>Dynamic Adjustments</li>
                </ul>
            </div>
            <div class="algo-card">
                <h3>Value at Risk (VaR)</h3>
                <p>Risk management using:</p>
                <ul>
                    <li>95% Confidence Level</li>
                    <li>252-Day Lookback</li>
                    <li>Monte Carlo Simulation</li>
                    <li>Volatility Adjustment</li>
                </ul>
            </div>
        </div>

        <div class="metric-grid">
            <div class="metric-card">
                <h4>Monthly Target</h4>
                <div class="metric-value">€1,500</div>
                <p>Base Investment</p>
            </div>
            <div class="metric-card">
                <h4>IWDA Allocation</h4>
                <div class="metric-value">67%</div>
                <p>Of Monthly Target</p>
            </div>
            <div class="metric-card">
                <h4>BTC Allocation</h4>
                <div class="metric-value">33%</div>
                <p>Of Monthly Target</p>
            </div>
            <div class="metric-card">
                <h4>Expected Return</h4>
                <div class="metric-value">+2-5%</div>
                <p>Annual Outperformance</p>
            </div>
        </div>
    </section>

    <section class="features" id="features">
        <!-- ... bestaande features content ... -->
    </section>

    <section class="performance" id="performance">
        <h2>Strategy Performance</h2>
        <div class="algo-grid">
            <div class="algo-card">
                <h3>Market Conditions</h3>
                <p>Dynamic allocation based on:</p>
                <ul>
                    <li>Extreme Fear: 2.5x allocation</li>
                    <li>Fear: 1.8x allocation</li>
                    <li>Neutral: 1.0x allocation</li>
                    <li>Greed: 0.4x allocation</li>
                    <li>Extreme Greed: 0.2x allocation</li>
                </ul>
            </div>
            <div class="algo-card">
                <h3>Risk Management</h3>
                <p>Advanced protection features:</p>
                <ul>
                    <li>Position Size Limits</li>
                    <li>Volatility Adjustments</li>
                    <li>Market Regime Detection</li>
                    <li>Automatic Rebalancing</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="cta" id="start">
        <!-- ... bestaande CTA content ... -->
    </section>

    <script>
        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
    """
    
    st.set_page_config(page_title="MONTO", page_icon="📈", layout="wide", initial_sidebar_state="collapsed")
    
    # Remove default Streamlit styling
    st.markdown("""
        <style>
            .block-container { padding: 0; max-width: 100%; }
            #MainMenu { visibility: hidden; }
            footer { visibility: hidden; }
        </style>
    """, unsafe_allow_html=True)
    
    components.html(html_content, height=2000, scrolling=True)

if __name__ == "__main__":
    create_monto_website()
