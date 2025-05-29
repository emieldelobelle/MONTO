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

        .cta {
            background: var(--dark);
            padding: 6rem 2rem;
            text-align: center;
            color: var(--light);
        }

        .cta-button {
            display: inline-block;
            padding: 1.5rem 3rem;
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--light);
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s ease;
            margin-top: 2rem;
            border: none;
            cursor: pointer;
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(43, 79, 254, 0.4);
        }

        @media (max-width: 768px) {
            .hero-logo { font-size: 3rem; }
            .hero-subtitle { font-size: 1.2rem; }
            .features { padding: 2rem; }
        }
    </style>

    <div class="hero">
        <video autoplay loop muted playsinline>
            <source src="https://cdn.coverr.co/videos/coverr-a-digital-world-2741/1080p.mp4" type="video/mp4">
        </video>
        <div class="hero-content">
            <h1 class="hero-logo">MONTO</h1>
            <p class="hero-subtitle">The Future of Intelligent Investing</p>
            <a href="#features" class="cta-button">Discover More</a>
        </div>
    </div>

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

    <div class="cta">
        <h2>Ready to Transform Your Investment Strategy?</h2>
        <a href="https://colab.research.google.com/drive/JOUW-COLAB-LINK" class="cta-button">
            Start Investing Smarter →
        </a>
    </div>
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
