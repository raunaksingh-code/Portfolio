import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils.style import apply_custom_css

st.set_page_config(page_title="Data Analytics | Raunak Singh", page_icon="📈", layout="wide")
apply_custom_css()

st.markdown("<h1 style='color: #D4AF37;'>Strategic Data Analytics & Operations</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #8892b0; font-size: 1.1rem;'>Leveraging data to uncover non-linear patterns and drive operational efficiency.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #233554;'>", unsafe_allow_html=True)

# 1. Workforce Analytics
st.markdown("<h3>Workforce & Compensation Analytics</h3>", unsafe_allow_html=True)
col_wa1, col_wa2 = st.columns([1, 1.2])

with col_wa1:
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("**Objective:** Uncover actionable insights regarding salary expectations and labor market dynamics.")
    st.markdown("""
    - Analyzed an extensive dataset of **913,384** job seeker records.
    - Utilized Python (Pandas, Plotly, Scikit-Learn) to perform Exploratory Data Analysis, Clustering, and Regression modeling.
    - Identified non-linear relationships between skill composition, professional experience, and salary expectations to optimize recruitment strategies.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
with col_wa2:
    # Cluster / Density visualization
    np.random.seed(42)
    x = np.random.normal(5, 2, 500)
    y = x * 1.5 + np.random.normal(0, 2, 500)
    
    fig_scatter = go.Figure(data=go.Scatter(
        x=x, y=y, mode='markers',
        marker=dict(size=8, color=y, colorscale='Tealgrn', opacity=0.7, line=dict(width=0.5, color='#fff'))
    ))
    fig_scatter.update_layout(
        title=dict(text="Experience vs Salary Expectations (Data Model Preview)", font=dict(color='#ccd6f6', size=14)),
        height=300, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridcolor='#233554', title="Years of Experience", titlefont=dict(color='#8892b0')),
        yaxis=dict(showgrid=True, gridcolor='#233554', title="Expected Salary", titlefont=dict(color='#8892b0')),
        margin=dict(l=40, r=20, t=40, b=40)
    )
    st.plotly_chart(fig_scatter, use_container_width=True, config={'displayModeBar': False})

st.markdown("<br>", unsafe_allow_html=True)

# 2. Operations (Abhiyan Minerals)
st.markdown("<h3>Abhiyan Minerals: Operational Optimization</h3>", unsafe_allow_html=True)
col_op1, col_op2 = st.columns([1.2, 1])

with col_op1:
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("**Role:** Office Associate (July 2024 – May 2025)")
    st.markdown("""
    - Orchestrated **80+ auction operations**, ensuring stringent timeline adherence and seamless execution coordination.
    - Maintained flawless data integrity, validating and processing **500+ financial records** with 100% accuracy.
    - Designed critical MIS reports that drove executive decision-making.
    - Conducted process gap analysis to streamline workflows, reducing operational errors by 10%.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with col_op2:
    fig_op = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = 10,
        delta = {'reference': 0, 'position': "top", 'suffix': "%"},
        title = {'text': "Error Reduction Achieved", 'font': {'color': '#ccd6f6', 'size': 18}},
        number = {'suffix': "%", 'font': {'color': '#D4AF37'}},
        gauge = {
            'axis': {'range': [None, 20], 'tickwidth': 1, 'tickcolor': "#8892b0"},
            'bar': {'color': "#D4AF37"},
            'bgcolor': "rgba(0,0,0,0)",
            'steps': [
                {'range': [0, 10], 'color': "rgba(17, 43, 60, 0.5)"},
                {'range': [10, 20], 'color': "rgba(0, 90, 60, 0.4)"}
            ],
        }
    ))
    fig_op.update_layout(height=280, margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_op, use_container_width=True, config={'displayModeBar': False})
