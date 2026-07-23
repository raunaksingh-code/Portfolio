import streamlit as st
import plotly.graph_objects as go
from utils.style import apply_custom_css

st.set_page_config(page_title="Financial Modeling | Raunak Singh", page_icon="📊", layout="wide")
apply_custom_css()

st.markdown("<h1 style='color: #D4AF37;'>Financial Modeling & Equity Research</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #8892b0; font-size: 1.1rem;'>Showcasing quantitative valuation and qualitative due diligence.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #233554;'>", unsafe_allow_html=True)

# 1. HUL DCF Model
st.markdown("<h3>Hindustan Unilever: 5-Year Financial Blueprint</h3>", unsafe_allow_html=True)
col_dcf1, col_dcf2 = st.columns([1, 1.5])
with col_dcf1:
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("**Objective:** Assess the financial health and strategic positioning of HUL over a 5-year horizon.")
    st.markdown("**Impact:** Modeled 20+ specific KPIs against FMCG peers to provide robust, evidence-based insights.")
    st.markdown("#### Interactive Valuation Parameters")
    wacc = st.slider("WACC (%)", min_value=7.0, max_value=12.0, value=8.5, step=0.1)
    tgr = st.slider("Terminal Growth Rate (%)", min_value=2.0, max_value=6.0, value=4.0, step=0.1)
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
            x = ["PV of Explicit FCF", "PV of Terminal Value", "Enterprise Value"],
            textposition = "outside",
            text = [f"₹{int(pv_fcf/1000)}k Cr", f"₹{int(tv/1000)}k Cr", f"₹{int(ev/1000)}k Cr"],
            y = [pv_fcf, tv, ev],
            connector = {"line": {"color": "#8892b0", "dash": "dot"}},
            decreasing = {"marker": {"color": "#f25022"}},
            increasing = {"marker": {"color": "#005A3C"}},
            totals = {"marker": {"color": "#D4AF37"}}
        ))
        fig_waterfall.update_layout(
            title=dict(text="Implied Enterprise Value Build-up", font=dict(color='#ccd6f6', size=16)),
            height=320, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            yaxis=dict(showgrid=True, gridcolor='#233554', showticklabels=False),
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_waterfall, use_container_width=True, config={'displayModeBar': False})
    else:
        st.error("WACC must be greater than Terminal Growth Rate for a valid DCF.")

st.markdown("<br>", unsafe_allow_html=True)

# 2. Britannia DD
st.markdown("<h3>Britannia Industries: Equity Due Diligence</h3>", unsafe_allow_html=True)
col_brit1, col_brit2 = st.columns([1.5, 1])
with col_brit1:
    st.markdown("<div class='impact-card' style='height: 100%;'>", unsafe_allow_html=True)
    st.markdown("**Initiating Coverage Report Analysis**")
    st.markdown("""
    - **Q3 FY26 Performance:** Analyzed a record-breaking quarter with Revenue at ₹4,885 Cr (+9.5% YoY) and Net Profit jumping 16.9% YoY to ₹680 Cr.
    - **Margin Expansion:** Investigated the drivers behind the 450 bps gross margin expansion (to 43.3%), citing stable commodity pricing and efficient cost management.
    - **Valuation Critique:** Assessed the stretched P/E multiple of ~58x. Evaluated the Bear case (FII selling pressure) vs the Bull case (Bel SA Cheese JV and rural market penetration).
    - **Leadership Transition:** Evaluated strategic shifts under the new MD & CEO, Rakshit Hargave.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
with col_brit2:
    st.markdown("<div class='metric-card' style='margin-bottom: 10px;'>", unsafe_allow_html=True)
    st.metric("Implied Upside", "~30%", "Analyst Target ₹7,150")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-card' style='margin-bottom: 10px;'>", unsafe_allow_html=True)
    st.metric("ROCE", "~60%", "Industry Leading")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric("P/E Ratio", "58x", "Premium Valuation")
    st.markdown("</div>", unsafe_allow_html=True)
