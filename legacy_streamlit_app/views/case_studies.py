import streamlit as st

def render():
    st.markdown("<h1>Case Studies & Financial Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.1rem; color: #4B5563; margin-bottom: 2rem;'>In-depth research and financial modelling demonstrating analytical depth and strategic foresight.</p>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["HUL Blueprint", "Workforce Analytics", "Britannia DD", "Piramal Pitch"])
    
    with tab1:
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h3>5-Year Financial Blueprint - Hindustan Unilever Ltd</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Objective:** Assess the financial health and strategic positioning of HUL over a 5-year horizon.")
            st.markdown("**Impact:** Provided robust, evidence-based insights influencing strategic decision-making and investment thesis formulation.")
            st.markdown("[🔗 **View Full 5-Year Financial Model (Excel)**](#)", unsafe_allow_html=True)
        with col2:
            st.markdown("<div class='metric-card' style='margin-bottom:0px;'>", unsafe_allow_html=True)
            st.metric("KPIs Analyzed", "20+", delta="Against FMCG Peers")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Interactive DCF Model (Mini)
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h4>⚙️ Interactive DCF Sensitivity Analysis</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #8892b0; font-size: 0.9rem;'>Adjust the sliders below to see how changes in WACC and Terminal Growth Rate impact the estimated Enterprise Value (Illustrative).</p>", unsafe_allow_html=True)
        
        sl1, sl2, res = st.columns([1, 1, 1.5])
        with sl1:
            wacc = st.slider("WACC (%)", min_value=6.0, max_value=12.0, value=8.5, step=0.1)
        with sl2:
            tgr = st.slider("Terminal Growth (%)", min_value=1.0, max_value=5.0, value=3.5, step=0.1)
            
        # Dummy DCF Calculation for illustration
        # Let's assume Base Free Cash Flow is 10,000 Cr.
        # Terminal Value = FCF * (1 + g) / (WACC - g)
        fcf = 10000
        wacc_dec = wacc / 100.0
        tgr_dec = tgr / 100.0
        
        if wacc_dec <= tgr_dec:
            ev = "Invalid (WACC <= Growth)"
        else:
            tv = (fcf * (1 + tgr_dec)) / (wacc_dec - tgr_dec)
            pv_fcf = fcf * 3.5 # rough PV of 5 yr explicit period
            ev = f"₹{int((tv + pv_fcf) / 1000):,}k Cr"
            
        with res:
            st.markdown("<div class='metric-card' style='margin-bottom:0px; text-align: center;'>", unsafe_allow_html=True)
            st.metric("Implied Enterprise Value", ev, delta=f"WACC: {wacc}% | TGR: {tgr}%")
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
            
    with tab2:
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h3>Workforce & Compensation Insights</h3>", unsafe_allow_html=True)
        col3, col4 = st.columns(2)
        with col3:
            st.markdown("**Objective:** Uncover actionable insights regarding salary expectations and labor market dynamics.")
            st.markdown("**Impact:** Generated highly accurate, data-backed workforce insights suitable for HR strategy.")
        with col4:
            st.markdown("<div class='metric-card' style='margin-bottom:0px;'>", unsafe_allow_html=True)
            st.metric("Dataset Size", "913K+", delta="Job Seeker Records")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
            
    with tab3:
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h3>Britannia Industries Equity Due Diligence</h3>", unsafe_allow_html=True)
        col5, col6 = st.columns(2)
        with col5:
            st.markdown("**Objective:** Evaluate Britannia's equity valuation and strategic outlook following a major C-suite transition.")
            st.markdown("**Impact:** Delivered a sell-side style 'initiating coverage' report detailing fundamental strengths versus valuation concerns.")
            st.markdown("[🔗 **View Full Initiating Coverage Report (PDF)**](#)", unsafe_allow_html=True)
        with col6:
            st.markdown("<div class='metric-card' style='margin-bottom:0px;'>", unsafe_allow_html=True)
            st.metric("Q3 FY26 Revenue", "₹4,885 Cr", delta="43.3% Gross Margin")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
            
    with tab4:
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h3>Piramal Enterprises Investor Pitch Deck</h3>", unsafe_allow_html=True)
        col7, col8 = st.columns(2)
        with col7:
            st.markdown("**Objective:** Pitch Piramal's diversified conglomerate model to institutional investors.")
            st.markdown("**Impact:** Created a boardroom-ready presentation that clearly communicates complex financial metrics.")
            st.markdown("[🔗 **View Full Investor Pitch Deck (PDF)**](#)", unsafe_allow_html=True)
        with col8:
            st.markdown("<div class='metric-card' style='margin-bottom:0px;'>", unsafe_allow_html=True)
            st.metric("FY20-FY24 CAGR", "~9.5%", delta="Consistent Recovery")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
            
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3>Additional Projects</h3>", unsafe_allow_html=True)
    
    col9, col10 = st.columns(2)
    with col9:
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("**Cesim Global Challenge Simulation:** Executed strategic management decisions in a virtual global market.")
        st.markdown("<br>**PNB FY25-26 Financial Analysis:** Deep dive into the banking sector's asset quality and margins.", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col10:
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("**Nestlé India Annual Report Deep Dive:** Breakdown of Nestlé's supply chain efficiencies.")
        st.markdown("<br>**LakesConnect & GL Connect:** Conceptualized networking platforms for alumni.", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
