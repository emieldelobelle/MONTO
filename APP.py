import streamlit as st
import streamlit.components.v1 as components

def create_monto_website():
    html_content = """
    <style>
        /* Modern Color Scheme */
        :root {
            --primary: #1E88E5;       /* Modern blue */
            --secondary: #6B48FF;     /* Rich purple */
            --accent: #00BFA5;        /* Teal */
            --dark: #1A1A1A;          /* Near black */
            --light: #FFFFFF;         /* Pure white */
            --background: #F5F7FA;    /* Light gray blue */
        }

        /* Base Layout */
        body {
            margin: 0;
            padding: 0;
            background: var(--background);
            font-family: 'Inter', sans-serif;
            color: var(--dark);
            overflow-x: hidden;
            width: 100%;
        }

        /* Logo Design */
        .logo-container {
            text-align: center;
            padding: 2rem;
        }

        .logo {
            font-size: 3rem;
            font-weight: 800;
            color: var(--primary);
            text-transform: uppercase;
            letter-spacing: 2px;
            position: relative;
            display: inline-block;
        }

        .logo::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            border-radius: 2px;
        }

        /* Hero Section with Video */
        .hero {
            position: relative;
            height: 70vh;
            width: 100%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .hero-video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: 1;
        }

        .hero-content {
            position: relative;
            z-index: 2;
            text-align: center;
            color: var(--light);
            padding: 2rem;
            background: rgba(0,0,0,0.5);
            border-radius: 20px;
            backdrop-filter: blur(10px);
        }

        /* Feature Cards */
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            padding: 4rem 2rem;
            background: var(--light);
        }

        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        /* AI Generated Images */
        .ai-visual {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 1rem;
        }

        /* CTA Section */
        .cta {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            padding: 4rem 2rem;
            text-align: center;
            color: var(--light);
        }

        .cta-button {
            display: inline-block;
            padding: 1rem 2rem;
            font-size: 1.2rem;
            color: var(--primary);
            background: var(--light);
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s ease;
            margin-top: 2rem;
            font-weight: 600;
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }
    </style>

    <div class="logo-container">
        <div class="logo">MONTO</div>
    </div>

    <div class="hero">
        <video class="hero-video" autoplay loop muted playsinline>
            <source src="https://assets.mixkit.co/videos/preview/mixkit-growing-line-graph-animation-14026-large.mp4" type="video/mp4">
        </video>
        <div class="hero-content">
            <h1>Intelligent Investing for Tomorrow</h1>
            <p>Data-driven investment decisions powered by advanced analytics</p>
        </div>
    </div>

    <div class="features">
        <div class="feature-card">
            <img src="https://oaidalleapiprodscus.blob.core.windows.net/private/org-YLGrXP7wv7kN8k5XvjhxYOpG/user-dQFKgPJjhXGYZSGmhJhvmJcB/img-gg8qAB2152sAoqFJHG5Vdzqp.png?st=2024-05-29T19%3A18%3A17Z&se=2024-05-29T21%3A18%3A17Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-29T19%3A18%3A17Z&ske=2024-05-29T21%3A18%3A17Z&sks=b&skv=2021-08-06&sig=abcdef123456" 
                 class="ai-visual" alt="Smart Analytics">
            <h3>Smart Analytics</h3>
            <p>Advanced algorithms analyze market sentiment and optimize your portfolio</p>
        </div>
        <div class="feature-card">
            <img src="https://oaidalleapiprodscus.blob.core.windows.net/private/org-YLGrXP7wv7kN8k5XvjhxYOpG/user-dQFKgPJjhXGYZSGmhJhvmJcB/img-QR8zBN9m52KAoqFJHG5VdzQp.png?st=2024-05-29T19%3A18%3A17Z&se=2024-05-29T21%3A18%3A17Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-29T19%3A18%3A17Z&ske=2024-05-29T21%3A18%3A17Z&sks=b&skv=2021-08-06&sig=abcdef123456" 
                 class="ai-visual" alt="Risk Management">
            <h3>Risk Management</h3>
            <p>Sophisticated risk assessment using Kelly Criterion and Value at Risk</p>
        </div>
        <div class="feature-card">
            <img src="https://oaidalleapiprodscus.blob.core.windows.net/private/org-YLGrXP7wv7kN8k5XvjhxYOpG/user-dQFKgPJjhXGYZSGmhJhvmJcB/img-KL9xBN9m52KAoqFJHG5VdzQp.png?st=2024-05-29T19%3A18%3A17Z&se=2024-05-29T21%3A18%3A17Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-05-29T19%3A18%3A17Z&ske=2024-05-29T21%3A18%3A17Z&sks=b&skv=2021-08-06&sig=abcdef123456" 
                 class="ai-visual" alt="Market Timing">
            <h3>Market Timing</h3>
            <p>Optimal entry points based on Fear & Greed indices and technical analysis</p>
        </div>
    </div>

    <div class="cta">
        <h2>Ready to Optimize Your Investments?</h2>
        <p>Start using MONTO Invest today and experience the power of data-driven investing</p>
        <a href="https://colab.research.google.com/drive/JOUW-COLAB-LINK" class="cta-button">
            Get Started Now 🚀
        </a>
    </div>
    """
    
    # Configure Streamlit page
    st.set_page_config(
        page_title="MONTO Invest",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Remove default margins
    st.markdown("""
        <style>
            .block-container {
                padding-top: 0;
                padding-bottom: 0;
                padding-left: 0;
                padding-right: 0;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Render the HTML content
    components.html(html_content, height=2000, scrolling=False)

if __name__ == "__main__":
    create_monto_website()
