import streamlit as st
import plotly.graph_objects as go
from utils.style import apply_custom_css

# Configure the Streamlit page
st.set_page_config(
    page_title="Raunak Singh | Investment Banking Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global custom styling
apply_custom_css()

# Build the Home Page
st.markdown("<h1 style='text-align: center; color: #D4AF37 !important; margin-bottom: 0px;'>RAUNAK SINGH</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8892b0; font-size: 1.2rem; margin-top: 5px;'>Investment Banking & Corporate Finance</p>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #233554; margin-bottom: 10px;'>", unsafe_allow_html=True)

# Page Switch Navigation Buttons
st.markdown("<p style='text-align: center; color: #8892b0; font-size: 0.9rem; margin-bottom: 10px;'>Navigate Portfolio:</p>", unsafe_allow_html=True)
st.markdown("""
<style>
.nav-link-btn {
    display: block;
    width: 100%;
    padding: 0.6rem 0;
    margin: 0;
    text-align: center;
    background-color: #112240;
    color: #e6f1ff !important;
    text-decoration: none !important;
    border-radius: 6px;
    border: 1px solid #233554;
    font-weight: 500;
    transition: all 0.2s ease-in-out;
}
.nav-link-btn:hover {
    background-color: #233554;
    border-color: #D4AF37;
    color: #D4AF37 !important;
}
</style>
""", unsafe_allow_html=True)

nav1, nav2, nav3, nav4 = st.columns(4)
with nav1:
    st.markdown("<a href='Financial_Modeling' target='_self' class='nav-link-btn'>📊 Financial Modeling</a>", unsafe_allow_html=True)
with nav2:
    st.markdown("<a href='Data_Analytics' target='_self' class='nav-link-btn'>📈 Data Analytics</a>", unsafe_allow_html=True)
with nav3:
    st.markdown("<a href='Summer_Internship' target='_self' class='nav-link-btn'>🏢 Summer Internship</a>", unsafe_allow_html=True)
with nav4:
    st.markdown("<a href='Achievements' target='_self' class='nav-link-btn'>🏆 Achievements</a>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #233554; margin-top: 10px;'>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("<div class='impact-card' style='height: 100%;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top:0 !important;'>Executive Summary</h3>", unsafe_allow_html=True)
    st.markdown("""
    Intellectually curious management professional specializing in financial analysis and operations. Dedicated to driving actionable outcomes through structured analytics and robust financial modeling.
    
    **Core Value Proposition:**
    - **Financial Due Diligence:** Hands-on experience constructing 5-year financial blueprints and evaluating equity for large-cap FMCG companies.
    - **Analytical Rigor:** Proficient in modeling large-scale datasets (913K+ records) using Python.
    - **Operational Excellence:** Demonstrated ability to improve workflows, reducing operational errors by 10%.
    - **Strategic Execution:** Consistent top 1% performer in national strategic case competitions.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
with col2:
    st.markdown("<div class='impact-card' style='text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom: 0px; color: #D4AF37;'>1.5+ Years</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8892b0;'>Professional Experience</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom: 0px; color: #D4AF37;'>3</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8892b0;'>Distinct Analyst Roles</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom: 0px; color: #D4AF37;'>Top 1%</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8892b0;'>Competitive Rank</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3>Career Trajectory (2020 - 2027E)</h3>", unsafe_allow_html=True)
st.markdown("<p style='color: #8892b0; font-size: 1rem;'>Visualizing my academic milestones, professional roles, and target positioning.</p>", unsafe_allow_html=True)

# Advanced Career Timeline using Plotly
fig = go.Figure()

x_dates = ["2020", "2023", "2024", "2025", "2026", "2027E"]
y_vals = [1, 2, 3, 4, 5, 6.5]
labels = ["BBA Starts", "BBA Grad + Award", "Abhiyan Minerals<br>(Operations)", "PGDM Starts", "Dual Internships<br>(Finance/Data)", "Target: IB/CF Role"]

# Invisible trace to force axis ranges
fig.add_trace(go.Scatter(
    x=x_dates, y=y_vals, mode="markers", marker=dict(color="rgba(0,0,0,0)"),
    showlegend=False, hoverinfo="skip"
))

# Historical Line (solid)
fig.add_trace(go.Scatter(
    x=x_dates[:5], y=y_vals[:5], mode="lines+markers+text",
    text=labels[:5], textposition=["top right", "top left", "bottom right", "top left", "bottom right"],
    textfont=dict(size=13, color="#ccd6f6"),
    marker=dict(size=12, color="#005A3C", line=dict(width=2, color="#00ffaa")),
    line=dict(color="#005A3C", width=3, dash='solid'), cliponaxis=False
))

# Projected Line (dashed)
fig.add_trace(go.Scatter(
    x=x_dates[4:], y=y_vals[4:], mode="lines+markers+text",
    text=["", labels[5]], textposition=["top center", "bottom right"],
    textfont=dict(size=14, color="#D4AF37", weight="bold"),
    marker=dict(size=14, color="#D4AF37", symbol="star"),
    line=dict(color="#D4AF37", width=3, dash='dot'), cliponaxis=False
))

fig.update_layout(
    height=400, showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=True, gridcolor="#233554", gridwidth=1, zeroline=False, tickfont=dict(color="#8892b0", size=14), categoryorder="array", categoryarray=x_dates),
    yaxis=dict(showgrid=True, gridcolor="#233554", gridwidth=1, zeroline=False, showticklabels=False, range=[0, 8]),
    margin=dict(l=20, r=40, t=20, b=20)
)
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
