import streamlit as st
import plotly.graph_objects as go

def render():
    st.markdown("<h1>Strategic Capabilities & Impact</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.1rem; color: #4B5563; margin-bottom: 2rem;'>Delivering quantifiable results through process optimization, rigorous data analysis, and cross-functional leadership.</p>", unsafe_allow_html=True)
    
    # Impact Overview Chart
    st.markdown("<h3>Impact Highlights</h3>", unsafe_allow_html=True)
    
    col_chart, col_anim = st.columns([2, 1])
    
    with col_chart:
        # Bar chart showing quantifiable impact
        fig = go.Figure(data=[
            go.Bar(name='Target', x=['Data Accuracy', 'Error Reduction', 'Operations Managed', 'Dashboards Built'], y=[100, 10, 80, 5], marker_color='#005A3C')
        ])
        fig.update_layout(
            title=dict(text="Key Performance Metrics", font=dict(color="#ccd6f6")),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            height=300,
            margin=dict(l=0, r=0, t=30, b=0),
            yaxis=dict(showgrid=True, gridcolor="#233554", tickfont=dict(color="#8892b0")),
            xaxis=dict(tickfont=dict(color="#8892b0"))
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        
    with col_anim:
        # Gauge chart for Performance
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 100,
            title = {'text': "Execution Rate (%)", 'font': {'color': "#ccd6f6"}},
            number = {'font': {'color': "#D4AF37"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickfont': {'color': "#8892b0"}},
                'bar': {'color': "#005A3C"},
                'steps': [
                    {'range': [0, 50], 'color': "rgba(17, 43, 60, 0.4)"},
                    {'range': [50, 100], 'color': "rgba(17, 43, 60, 0.8)"}
                ],
            }
        ))
        fig_gauge.update_layout(height=250, margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_gauge, use_container_width=True, config={'displayModeBar': False})
        
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3>Professional Experience</h3>", unsafe_allow_html=True)
    
    # Quick Clean Experience
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("<h4>Quick Clean Private Limited</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; margin-top: -10px;'><em>Founder's Office Analyst Intern | April 2026 – June 2026</em></p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Financial Modeling", value="P&L Analysis")
    with col2:
        st.metric(label="Capex Efficiency", value="Optimized")
    with col3:
        st.metric(label="Dashboard Built", value="Marriott Intelligence")
        
    st.markdown("""
    - Evaluated site-level P&L and Capex efficiency for asset-intensive service operations.
    - Developed the **Marriott India Portfolio Brand Intelligence Dashboard**, transforming raw operational data into boardroom-ready strategic insights.
    - Built a robust Knowledge Centre to streamline organizational knowledge sharing and operational execution.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Abhiyan Minerals Experience (Associate)
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("<h4>Abhiyan Minerals</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; margin-top: -10px;'><em>Office Associate | July 2024 – May 2025</em></p>", unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric(label="Auctions Executed", value="80+", delta="~$X M Transacted")
    with col5:
        st.metric(label="Data Integrity", value="100%", delta="500+ Financial Records")
    with col6:
        st.metric(label="Process Efficiency", value="+10%", delta="Workflow Gaps Fixed")
        
    st.markdown("""
    - Orchestrated **80+ auction operations**, ensuring stringent timeline adherence and seamless execution coordination.
    - Maintained flawless data integrity, validating and processing **500+ records with 100% accuracy**.
    - Designed and generated critical MIS reports and structured management summaries that drove executive decision-making.
    - Conducted process gap analysis to streamline workflows, successfully reducing operational errors by 10%.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Abhiyan Minerals Experience (Trainee)
    st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
    st.markdown("<h4>Abhiyan Minerals</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; margin-top: -10px;'><em>Office Trainee Intern | April 2024 – June 2024</em></p>", unsafe_allow_html=True)
    st.markdown("Assisted in deep-dive process analytics. Strengthened financial compliance by verifying 100+ POs and facilitated communication channels.")
    st.markdown("</div>", unsafe_allow_html=True)
