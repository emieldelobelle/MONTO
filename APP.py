import streamlit as st
import streamlit.components.v1 as components

def create_monto_website():
    html_content = """
    <style>
        /* CSS Reset & Base Styles */
        :root {
            --primary: #2962ff;
            --accent: #00b0ff;
            --dark: #0a1931;
            --light: #ffffff;
            --gray: #f5f5f5;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        body {
            line-height: 1.6;
            color: var(--dark);
            overflow-x: hidden;
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            min-height: 100vh;
            padding: 8rem 2rem 4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: var(--light);
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.25rem;
            max-width: 600px;
            margin-bottom: 2rem;
        }

        .cta-button {
            background: var(--light);
            color: var(--primary);
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.3s ease;
        }

        .cta-button:hover {
            transform: translateY(-3px);
        }

        /* Header Styling */
        .header {
            background: var(--dark);
            color: var(--light);
            padding: 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, var(--accent), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .header p {
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto 1.5rem;
        }

        .colab-button {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--primary);
            color: var(--light);
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .colab-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(41, 98, 255, 0.3);
        }

        .colab-button img {
            height: 24px;
        }

        /* Features Section */
        .features {
            padding: 6rem 2rem;
            background: var(--light);
        }

        .features h2 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .feature-card {
            padding: 2rem;
            border-radius: 15px;
            background: var(--gray);
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-card h3 {
            color: var(--primary);
            margin-bottom: 1rem;
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
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
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

        /* Responsive Design */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }

            .nav {
                padding: 1rem;
            }

            .nav-links {
                display: none;
            }
        }
    </style>

    <!-- New Header Section -->
    <div class="header">
        <h1>MONTO Invest</h1>
        <p>Smart investing made simple. Use data-driven strategies to optimize your monthly investments in IWDA ETF and Bitcoin.</p>
        <a href="https://colab.research.google.com/drive/your-notebook-id" class="colab-button">
            <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
            Open Investment Calculator
        </a>
    </div>

    <!-- Quick Start Guide -->
    <section class="features" id="quickstart">
        <h2>Quick Start Guide</h2>
        <div class="feature-grid">
            <div class="feature-card">
                <h3>1. Set Your Budget</h3>
                <p>Enter your monthly investment amount (minimum €100)</p>
            </div>
            <div class="feature-card">
                <h3>2. Get Recommendations</h3>
                <p>Receive optimal allocation between IWDA ETF and Bitcoin</p>
            </div>
            <div class="feature-card">
                <h3>3. Execute Orders</h3>
                <p>Follow the detailed instructions for DEGIRO and Bitvavo</p>
            </div>
        </div>
    </section>

    <!-- Algorithm Section (keep existing) -->
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
    
    st.set_page_config(page_title="MONTO", page_icon="💰", layout="wide", initial_sidebar_state="collapsed")
    
    # Remove Streamlit styling
    st.markdown("""
        <style>
            .block-container { padding: 0 !important; max-width: 100% !important; }
            #MainMenu { visibility: hidden; }
            footer { visibility: hidden; }
            .stApp { background: var(--gray) !important; }
        </style>
    """, unsafe_allow_html=True)
    
    components.html(html_content, height=3000, scrolling=True)

if __name__ == "__main__":
    create_monto_website()
