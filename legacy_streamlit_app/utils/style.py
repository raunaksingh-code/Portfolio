import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        h1, h2, h3, h4 {
            font-weight: 600 !important;
            letter-spacing: -0.5px;
        }

        h1 { font-size: 2.5rem !important; margin-bottom: 1rem !important; }
        h3 { font-size: 1.5rem !important; margin-top: 1.5rem !important; color: #D4AF37 !important; }

        /* Custom Content Cards */
        .impact-card {
            background-color: #112240;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            margin-bottom: 1.5rem;
            border: 1px solid #233554;
            transition: transform 0.2s;
        }
        
        .impact-card:hover {
            transform: translateY(-2px);
            border-color: #D4AF37;
        }

        .metric-card {
            background-color: #112240;
            padding: 1.25rem;
            border-radius: 6px;
            border-left: 4px solid #005A3C;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px -1px rgba(0,0,0,0.05);
        }

        /* Metric text overrides */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            color: #D4AF37 !important;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
            color: #8892b0 !important;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Sidebar visible for multi-page navigation */
        [data-testid="stSidebar"] {
            background-color: #0a192f;
        }

        /* Link colors */
        a {
            color: #D4AF37 !important;
            text-decoration: none !important;
        }
        a:hover {
            text-decoration: underline !important;
        }
        </style>
    """, unsafe_allow_html=True)

def load_lottieurl(url: str):
    import requests
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
