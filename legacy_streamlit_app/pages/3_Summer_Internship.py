import streamlit as st
import plotly.graph_objects as go
from utils.style import apply_custom_css

st.set_page_config(page_title="Summer Internship | Raunak Singh", page_icon="🏢", layout="wide")
apply_custom_css()

st.markdown("<h1 style='color: #D4AF37;'>Summer Internship 2026: Quick Clean</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #8892b0; font-size: 1.1rem;'>Role: Founder's Office Analyst Intern | April - June 2026</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #233554;'>", unsafe_allow_html=True)

# 1. BOO Capex
st.markdown("<h3>1. Financial Performance & Capex Efficiency</h3>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1.2])
with col1:
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("""
    - **Objective:** Evaluate site-level Profit & Loss and Capital Expenditure efficiency for on-premise laundry operations.
    - **Impact:** Provided robust financial decomposition identifying key cost drivers, enabling optimized payback periods for BOO (Build-Own-Operate) models.
    - **Outcome:** Strengthened investment rationale and cost-control strategies for the Founder's Office.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    fig_capex = go.Figure(go.Waterfall(
        name = "Capex Efficiency", orientation = "v",
        measure = ["relative", "relative", "relative", "total"],
        x = ["Equipment Setup", "Installation", "Working Capital", "Total Capex"],
        textposition = "outside",
        text = ["₹45L", "₹5L", "₹10L", "₹60L"],
        y = [45, 5, 10, 60],
        connector = {"line": {"color": "#8892b0", "dash": "dot"}},
        decreasing = {"marker": {"color": "#f25022"}},
        increasing = {"marker": {"color": "#005A3C"}},
        totals = {"marker": {"color": "#D4AF37"}}
    ))
    fig_capex.update_layout(
        title=dict(text="Illustrative BOO Model Capex Breakdown", font=dict(color='#ccd6f6', size=14)),
        height=300, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        yaxis=dict(showgrid=True, gridcolor='#233554', showticklabels=False),
        margin=dict(l=10, r=10, t=40, b=30)
    )
    st.plotly_chart(fig_capex, use_container_width=True, config={'displayModeBar': False})

st.markdown("<br>", unsafe_allow_html=True)

# 2. Marriott Dashboard
st.markdown("<h3>2. Marriott India Portfolio Brand Intelligence Dashboard</h3>", unsafe_allow_html=True)
col3, col4 = st.columns([1.2, 1])
with col4:
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("""
    - **Objective:** Transform raw operational data into a boardroom-ready strategic dashboard for the Marriott hospitality portfolio.
    - **Impact:** Consolidated KPIs across multiple Marriott properties, providing real-time visibility into machine utilization, sustainability, and revenue analytics.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div style='border: 1px solid #233554; padding: 20px; border-radius: 8px; background-color: rgba(17,34,64,0.3);'>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:#D4AF37; margin-top:0; margin-bottom: 20px;'>Marriott Intelligence Snapshot</h4>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("Avg Utilization", "87%", "+4.2%")
    m2.metric("Sustainability", "1.2 Tons CO₂", "Saved vs Last Mth")
    m3.metric("Uptime", "99.2%", "Optimal")
    
    fig_util = go.Figure()
    fig_util.add_trace(go.Scatter(x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], y=[78, 80, 82, 85, 84, 87], mode='lines+markers', line=dict(color='#00ffaa', width=3), marker=dict(size=8, color='#D4AF37')))
    fig_util.update_layout(
        title=dict(text="Portfolio Utilization Trend", font=dict(size=12, color='#8892b0')),
        height=150, margin=dict(l=10, r=10, t=30, b=10), 
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', 
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), xaxis=dict(showgrid=False, tickfont=dict(color='#8892b0'))
    )
    st.plotly_chart(fig_util, use_container_width=True, config={'displayModeBar': False})
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 3. Knowledge Centre
st.markdown("<h3>3. Internal Knowledge Centre Architecture</h3>", unsafe_allow_html=True)
col5, col6 = st.columns([1, 1.2])
with col5:
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("""
    - **Impact:** Built a centralized knowledge repository to integrate disparate data sources (Finance, Sales, Operations).
    - **Integration:** Leveraged Flask, Python, and an Internal AI Knowledge Assistant to reduce onboarding time and enable quick access to operational SOPs.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
with col6:
    fig_arch = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15, thickness = 20, line = dict(color = "rgba(0,0,0,0)", width = 0),
          label = ["SOP Data", "Finance Data", "Sales Data", "Backend (Python)", "AI Assistant", "Knowledge Centre Portal"],
          color = ["#112240", "#112240", "#112240", "#005A3C", "#009A68", "#D4AF37"]
        ),
        link = dict(
          source = [0, 1, 2, 3, 4, 3], target = [3, 3, 3, 5, 5, 4],
          value = [8, 4, 4, 10, 6, 4], color = ["rgba(136, 146, 176, 0.2)"] * 6
        )
    )])
    fig_arch.update_layout(
        title=dict(text="Data Flow & System Architecture", font=dict(color='#ccd6f6', size=14)),
        height=280, margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_arch, use_container_width=True, config={'displayModeBar': False})
