import streamlit as st
import streamlit.components.v1 as components

def create_monto_website():
    html_content = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

        :root {
            --primary: #2B4FFE;          /* Electric Blue */
            --secondary: #6C63FF;        /* Purple */
            --accent: #00F7FF;           /* Cyan */
            --dark: #0A1931;             /* Deep Navy */
            --light: #FFFFFF;
            --gray: #F6F9FC;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

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

        .hero {
            position: relative;
            height: 100vh;
            width: 100%;
            overflow: hidden;
        }

        .hero video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.7);
        }

        .hero-content {
            position: relative;
            z-index: 2;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: var(--light);
            padding: 2rem;
            background: rgba(10, 25, 49, 0.4);
            backdrop-filter: blur(10px);
        }

        .hero-logo {
            font-size: 5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--accent), var(--primary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
            letter-spacing: 4px;
        }

        .hero-subtitle {
            font-size: 1.5rem;
            max-width: 800px;
            margin-bottom: 3rem;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            padding: 4rem;
            background: var(--gray);
        }

        .feature-card {
            position: relative;
            overflow: hidden;
            border-radius: 20px;
            background: var(--light);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-10px);
        }

        .feature-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
        }

        .feature-content {
            padding: 2rem;
        }

        .feature-title {
            font-size: 1.5rem;
            color: var(--dark);
            margin-bottom: 1rem;
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

        @media (max-width: 768px) {
            .hero-logo { font-size: 3rem; }
            .hero-subtitle { font-size: 1.2rem; }
            .features { padding: 2rem; }
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
        <video autoplay loop muted playsinline>
            <source src="https://cdn.coverr.co/videos/coverr-a-digital-world-2741/1080p.mp4" type="video/mp4">
        </video>
        <div class="hero-content">
            <h1 class="hero-logo">MONTO</h1>
            <p class="hero-subtitle">The Future of Intelligent Investing</p>
            <a href="#features" class="cta-button">Discover More</a>
        </div>
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
        <div class="features" id="features">
        <div class="feature-card">
            <img class="feature-image" 
                 src="https://images.unsplash.com/photo-1642543492481-44e81e3914a6?auto=format&fit=crop&w=1000" 
                 alt="AI Trading">
            <div class="feature-content">
                <h3 class="feature-title">AI-Powered Analysis</h3>
                <p>Advanced algorithms analyze market sentiment and optimize your portfolio in real-time.</p>
            </div>
        </div>

        <div class="feature-card">
            <img class="feature-image" 
                 src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1000" 
                 alt="Risk Management">
            <div class="feature-content">
                <h3 class="feature-title">Smart Risk Management</h3>
                <p>Kelly Criterion and Value at Risk calculations protect your investments.</p>
            </div>
        </div>

        <div class="feature-card">
            <img class="feature-image" 
                 src="https://images.unsplash.com/photo-1640340434855-6084b1f4901c?auto=format&fit=crop&w=1000" 
                 alt="Market Timing">
            <div class="feature-content">
                <h3 class="feature-title">Perfect Market Timing</h3>
                <p>Fear & Greed indices help you enter and exit positions at optimal moments.</p>
            </div>
        </div>
    </div>
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
        <h2>Ready to Transform Your Investment Strategy?</h2>
        <a href="https://colab.research.google.com/drive/JOUW-COLAB-LINK" class="cta-button">
            Start Investing Smarter →
        </a>
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
    
    st.set_page_config
