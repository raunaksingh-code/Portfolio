import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def render():
    # Hero Section
    st.markdown("""
    <div style='text-align: center; padding: 1.5rem 0; margin-bottom: 2rem; border-bottom: 1px solid #233554;'>
        <h2 style='color: #D4AF37; font-size: 2.2rem; font-weight: 700; letter-spacing: 1px; margin-bottom: 10px; margin-top: -20px;'>INITIATING COVERAGE: STRATEGIC FINANCE & ANALYTICS</h2>
        <p style='color: #8892b0; font-size: 1.1rem; max-width: 800px; margin: 0 auto;'>
            A quantitative and qualitative deep dive into my professional track record across Equity Due Diligence, Financial Modeling, and Data Analytics. 
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Key Performance Indicators (KPIs)
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric("Valuation Models Built", "10+", "DCF & Relative")
    with k2:
        st.metric("Records Analyzed", "913K+", "HR & Ops Data")
    with k3:
        st.metric("Case Competitions", "Top 1%", "Out of 750+ Teams")
    with k4:
        st.metric("Target Roles", "IB / CF", "2026-2027")

    st.markdown("<br>", unsafe_allow_html=True)

    # Core Competencies & Britannia Coverage
    col_radar, col_brit = st.columns([1, 1.2])
    
    with col_radar:
        st.markdown("<h3 style='margin-top:0 !important;'>Core Competencies</h3>", unsafe_allow_html=True)
        categories = ['DCF Valuation', 'Equity Research', 'Data Analytics', 'Financial Accounting', 'Stakeholder Mgmt', 'Pitch Decks']
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=[95, 90, 85, 90, 80, 85],
            theta=categories,
            fill='toself',
            name='Proficiency',
            line_color='#D4AF37',
            fillcolor='rgba(212, 175, 55, 0.2)'
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=False, range=[0, 100]),
                angularaxis=dict(gridcolor="#233554", linecolor="#233554", tickfont=dict(color="#ccd6f6", size=11))
            ),
            showlegend=False,
            height=320,
            margin=dict(l=30, r=30, t=20, b=20),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_radar, use_container_width=True, config={'displayModeBar': False})

    with col_brit:
        st.markdown("<div class='impact-card' style='height: 90%;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top:0 !important; margin-bottom: 5px;'>Britannia Industries (NSE: BRITANNIA)</h3>", unsafe_allow_html=True)
        st.markdown("**Equity Due Diligence & Initiating Coverage Report**")
        st.markdown("""
        - **Thesis:** Analyzed Q3 FY26 financials (Revenue ₹4,885 Cr, +9.5% YoY) and leadership transition to evaluate a Buy/Sell case.
        - **Valuation Analysis:** Critiqued the stretched P/E of ~58x against industry peers, factoring in FII selling trends and competitive threats from ITC.
        - **Margin Drivers:** Deep dive into the 450 bps gross margin expansion and the Bel SA cheese JV's potential impact on long-term ROCE.
        """)
        
        # Mock Candlestick
        fig_candle = go.Figure(data=[go.Candlestick(
            x=['Q1', 'Q2', 'Q3', 'Q4'],
            open=[5000, 5100, 4800, 5200],
            high=[5200, 5300, 5200, 5600],
            low=[4900, 4700, 4750, 5100],
            close=[5100, 4800, 5200, 5500],
            increasing_line_color= '#005A3C', decreasing_line_color= '#f25022'
        )])
        fig_candle.update_layout(
            height=120, margin=dict(l=0, r=0, t=10, b=0),
            xaxis_rangeslider_visible=False,
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False)
        )
        st.plotly_chart(fig_candle, use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #233554;'>", unsafe_allow_html=True)

    # Financial Modeling Showcase
    st.markdown("<h3>Hindustan Unilever: 5-Year Financial Blueprint</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8892b0; font-size: 1rem;'>Interactive DCF Valuation Sensitivity Model. Adjust the WACC and Terminal Growth Rate to see the impact on Enterprise Value.</p>", unsafe_allow_html=True)
    
    col_dcf1, col_dcf2 = st.columns([1, 1.5])
    with col_dcf1:
        st.markdown("<br>", unsafe_allow_html=True)
        wacc = st.slider("WACC (%)", min_value=7.0, max_value=12.0, value=8.5, step=0.1)
        tgr = st.slider("Terminal Growth Rate (%)", min_value=2.0, max_value=6.0, value=4.0, step=0.1)
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("**Key Model Assumptions:**<br>- Base Free Cash Flow: ₹10,000 Cr<br>- Explicit Forecast Period: 5 Years<br>- Stable Commodity Pricing", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_dcf2:
        wacc_dec = wacc / 100.0
        tgr_dec = tgr / 100.0
        fcf_base = 10000
        
        if wacc_dec > tgr_dec:
            tv = (fcf_base * (1 + tgr_dec)) / (wacc_dec - tgr_dec)
            pv_fcf = fcf_base * 3.5 
            ev = tv + pv_fcf
            
            fig_waterfall = go.Figure(go.Waterfall(
                name = "DCF Valuation", orientation = "v",
                measure = ["relative", "relative", "total"],
                x = ["PV of Explicit FCF", "PV of Terminal Value", "Implied Enterprise Value"],
                textposition = "outside",
                text = [f"₹{int(pv_fcf/1000)}k", f"₹{int(tv/1000)}k", f"₹{int(ev/1000)}k"],
                y = [pv_fcf, tv, ev],
                connector = {"line": {"color": "#8892b0", "dash": "dot"}},
                decreasing = {"marker": {"color": "#f25022"}},
                increasing = {"marker": {"color": "#005A3C"}},
                totals = {"marker": {"color": "#D4AF37"}}
            ))
            fig_waterfall.update_layout(
                height=300,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                yaxis=dict(showgrid=True, gridcolor='#233554', showticklabels=False),
                margin=dict(l=20, r=20, t=20, b=20)
            )
            st.plotly_chart(fig_waterfall, use_container_width=True, config={'displayModeBar': False})
        else:
            st.error("WACC must be greater than Terminal Growth Rate to calculate a finite Terminal Value.")
            
    st.markdown("<hr style='border: 1px solid #233554;'>", unsafe_allow_html=True)
    
    # Data & Strategy
    st.markdown("<h3>Strategic Data & Case Competitions</h3>", unsafe_allow_html=True)
    c_data, c_comp = st.columns(2)
    
    with c_data:
        st.markdown("<div class='impact-card' style='height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<h4>Workforce Analytics & Labor Market Modeling</h4>", unsafe_allow_html=True)
        st.markdown("""
        Analyzed **913,384** job seeker records to uncover non-linear relationships between skill composition, experience, and salary expectations using Python (Pandas, Plotly, Scikit-Learn).
        """)
        # Area chart to represent big data distribution
        fig_area = go.Figure()
        x_dist = np.linspace(0, 20, 100)
        y_dist = np.exp(-(x_dist - 5)**2 / 10) * 10000
        fig_area.add_trace(go.Scatter(x=x_dist, y=y_dist, fill='tozeroy', mode='none', fillcolor='rgba(0, 90, 60, 0.5)'))
        fig_area.update_layout(
            height=120, margin=dict(l=0, r=0, t=10, b=0),
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, showticklabels=False), yaxis=dict(showgrid=False, showticklabels=False)
        )
        st.plotly_chart(fig_area, use_container_width=True, config={'displayModeBar': False})
        st.markdown("</div>", unsafe_allow_html=True)
        
    with c_comp:
        st.markdown("<div class='impact-card' style='height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<h4>National Strategy Competitions</h4>", unsafe_allow_html=True)
        st.markdown("""
        - 🏆 **2nd Rank** - IIM Bangalore Strategy Case Competition (2025)
        - 🏆 **Top 8 Finalist** (out of 751 teams) - IIM Rohtak, Pitchers (2025)
        - 🏆 **2nd Rank** - Tariff War Poster Making Competition (2025)
        - 🏆 **Winner** - Business Idea Presentation, IGNTU (2022)
        """)
        st.markdown("<br><p style='color: #8892b0; font-size:0.9rem;'>Consistent top 1% performance nationwide in high-stakes financial and strategic pitches.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
