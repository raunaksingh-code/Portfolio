import streamlit as st
import plotly.graph_objects as go

def render():
    st.markdown("<h1>Credentials & Market Readiness</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3>Education</h3>", unsafe_allow_html=True)
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h4>Great Lakes Institute of Management, Gurgaon</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280; margin-top: -10px;'><em>PGDM, Finance | 2025 – 2027</em></p>", unsafe_allow_html=True)
        st.markdown("Targeting Investment Banking and Corporate Finance. Secured 2nd Rank, Tariff War - Poster making competition (2025).")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h4>Indira Gandhi National Tribal University, Amarkantak</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280; margin-top: -10px;'><em>BBA | 2020 – 2023 | CGPA: 7.63/10</em></p>", unsafe_allow_html=True)
        st.markdown("Led placement initiatives for 150+ students. Organized fests and seminars engaging 200+ participants.")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3>Certifications</h3>", unsafe_allow_html=True)
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("- **HR Strategy Execution** - IIM Ahmedabad (6 months, 2025)")
        st.markdown("- **Business Negotiation (Silver Medalist)** - IIFT Delhi (6 months, 2025)")
        st.markdown("- **Green Belt Six Sigma** - Grant Thornton (2025)")
        st.markdown("- **NISM/SEBI & Ministry of Electronics & IT** Certifications")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<h3>Awards & Achievements</h3>", unsafe_allow_html=True)
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("- **2nd Rank** - IIM Bangalore Strategy Case Competition (2025)")
        st.markdown("- **Top 8 of 751 teams** - IIM Rohtak, Pitchers (2025)")
        st.markdown("- **Winner** - Business Idea Presentation Competition, IGNTU (2022)")
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<h3>Core Competencies Radar</h3>", unsafe_allow_html=True)
    
    # Skills Radar Chart
    categories = ['DCF Valuation', 'Relative Valuation', '3-Statement Modeling', 'Equity Due Diligence', 'Data Analysis & EDA', 'P&L Analysis', 'Risk Assessment', 'Stakeholder Management']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[95, 90, 90, 85, 95, 85, 80, 85],
        theta=categories,
        fill='toself',
        name='Proficiency',
        line_color='#005A3C',
        fillcolor='rgba(0, 90, 60, 0.4)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor="#233554", linecolor="#233554", tickfont=dict(color="#8892b0")),
            angularaxis=dict(gridcolor="#233554", linecolor="#233554", tickfont=dict(color="#ccd6f6"))
        ),
        showlegend=False,
        height=400,
        margin=dict(l=40, r=40, t=40, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
