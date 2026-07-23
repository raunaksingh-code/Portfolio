import streamlit as st
import plotly.graph_objects as go
from utils.style import apply_custom_css

st.set_page_config(page_title="Achievements | Raunak Singh", page_icon="🏆", layout="wide")
apply_custom_css()

st.markdown("<h1 style='color: #D4AF37;'>Elite Milestones & Case Competitions</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #8892b0; font-size: 1.1rem;'>Consistent top-percentile performance in national strategic pitches.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #233554;'>", unsafe_allow_html=True)

col7, col8 = st.columns([1.5, 1])
with col7:
    fig_funnel = go.Figure(go.Funnel(
        y = ["IIM Rohtak Pitchers (Total Teams)", "Top Finalists (IIM Rohtak)", "IIM B Strategy Case Rank", "Tariff War Competition Rank"],
        x = [751, 8, 2, 2],
        textinfo = "value",
        marker = {"color": ["#0a192f", "#112240", "#005A3C", "#D4AF37"],
                  "line": {"width": [1, 1, 2, 3], "color": ["#233554", "#233554", "#00ffaa", "#fff"]}}
    ))
    fig_funnel.update_layout(
        title=dict(text="Competitive Success Funnel", font=dict(color='#ccd6f6', size=16)),
        height=350, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig_funnel, use_container_width=True, config={'displayModeBar': False})
    
with col8:
    st.markdown("<div class='impact-card' style='height: 100%; display: flex; flex-direction: column; justify-content: center;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #D4AF37; text-align: center;'>🏆 Top 1% Achiever</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: #ccd6f6;'>
    Outperformed <b>740+</b> teams nationwide in high-stakes financial modeling and strategy pitches.<br><br>
    Secured <b>2nd Rank</b> across multiple IIM flagship competitions.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
