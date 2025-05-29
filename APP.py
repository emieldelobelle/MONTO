import streamlit as st
import streamlit.components.v1 as components

def create_monto_website():
    html_content = """
    <style>
        /* Modern Design System */
        :root {
            --primary: #2C3E50;
            --secondary: #3498DB;
            --accent: #16A085;
            --warning: #F1C40F;
            --success: #27AE60;
            --background: #F9FAFB;
            --text: #2D3748;
            --gradient: linear-gradient(135deg, #2C3E50, #3498DB);
        }

        /* Core Styles */
        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background: var(--background);
            margin: 0;
            padding: 2rem;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 24px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        /* Header Section */
        .hero {
            background: var(--gradient);
            padding: 4rem 2rem;
            text-align: center;
            color: white;
        }

        .logo {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            animation: fadeIn 1s ease-out;
        }

        .tagline {
            font-size: 1.5rem;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }

        /* Feature Cards */
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            padding: 4rem 2rem;
            background: white;
        }

        .feature-card {
            padding: 2rem;
            border-radius: 16px;
            background: var(--background);
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        /* CTA Section */
        .cta {
            padding: 4rem 2rem;
            text-align: center;
            background: var(--gradient);
            color: white;
        }

        .cta-button {
            display: inline-block;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--primary);
            background: white;
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s ease;
            margin-top: 2rem;
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            body { padding: 1rem; }
            .logo { font-size: 2.5rem; }
            .features { grid-template-columns: 1fr; }
        }
    </style>

    <div class="container">
        <section class="hero">
            <div class="logo">MONTO Invest</div>
            <p class="tagline">
                Intelligente investeringsstrategie gebaseerd op data-gedreven beslissingen
            </p>
        </section>

        <section class="features">
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Smart Allocation</h3>
                <p>Optimale portefeuilleverdeling op basis van Fear & Greed indices en marktcondities.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🛡️</div>
                <h3>Risicobescherming</h3>
                <p>Geavanceerde risicobeheersing met Value at Risk en Kelly Criterion methodologie.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📈</div>
                <h3>Prestatieverbetering</h3>
                <p>2-5% extra rendement per jaar door slim in te spelen op marktomstandigheden.</p>
            </div>
        </section>

        <section class="cta">
            <h2>Klaar om slimmer te investeren?</h2>
            <p>Start vandaag nog met MONTO Invest en optimaliseer je beleggingsstrategie.</p>
            <a href="https://colab.research.google.com/drive/JOUW-COLAB-LINK" class="cta-button">
                Start Nu! 🚀
            </a>
        </section>
    </div>
    """
    
    # Render in Streamlit
    st.set_page_config(page_title="MONTO Invest", page_icon="📈", layout="wide")
    components.html(html_content, height=1000)

if __name__ == "__main__":
    create_monto_website()
