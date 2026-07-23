import streamlit as st
import plotly.graph_objects as go

def render():
    st.markdown("<h1>Executive Summary</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.1rem; color: #4B5563; margin-bottom: 2rem;'>Intellectually curious management professional specializing in financial analysis and operations, dedicated to driving actionable outcomes through structured analytics.</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown("<div class='impact-card'>", unsafe_allow_html=True)
        st.markdown("<h3>Core Value Proposition</h3>", unsafe_allow_html=True)
        st.markdown("""
        - **Analytical Rigor:** Proficient in EDA, clustering, and regression modeling for large-scale datasets (913K+ records).
        - **Financial Due Diligence:** Hands-on experience constructing 5-year financial blueprints, analyzing 20+ KPIs for industry giants like HUL.
        - **Operational Excellence:** Demonstrated ability to improve workflows, leading to measurable error reductions (10%) and perfect data accuracy.
        - **Strategic Execution:** Proven track record in managing multiple complex projects, coordinating with cross-functional teams, and delivering actionable MIS insights.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Read resume if it exists, else provide dummy bytes for now
        try:
            with open("Raunak Singh_CV.pdf", "rb") as f:
                resume_bytes = f.read()
        except:
            resume_bytes = b"PDF not found"
            
        st.download_button(
            label="📄 Download 1-Page Resume",
            data=resume_bytes,
            file_name="Raunak_Singh_Resume.pdf",
            mime="application/pdf",
            type="primary"
        )
        
    with col2:
        st.markdown("<div class='impact-card' style='text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='margin-bottom: 0px;'>1+ Years</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280;'>Professional Experience</p>", unsafe_allow_html=True)
        st.markdown("<h2 style='margin-bottom: 0px;'>3</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280;'>Distinct Analyst Roles</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
            
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("<h3>Career Trajectory, 2020 - 2027E</h3>", unsafe_allow_html=True)
    
    # Advanced Career Timeline using Plotly
    fig = go.Figure()

    # Timeline points
    x_dates = ["2020", "2023", "2024", "2025", "2026", "2027E"]
    y_vals = [1, 2, 3, 4, 5, 6.5]
    labels = ["BBA begins", "BBA + award", "Abhiyan Minerals", "PGDM begins", "Dual internships", "IB Target"]

    # Invisible trace to force axis to include all categories
    fig.add_trace(go.Scatter(
        x=x_dates,
        y=y_vals,
        mode="markers",
        marker=dict(color="rgba(0,0,0,0)"),
        showlegend=False,
        hoverinfo="skip"
    ))

    # Historical Line (solid)
    fig.add_trace(go.Scatter(
        x=x_dates[:5],
        y=y_vals[:5],
        mode="lines+markers+text",
        text=labels[:5],
        textposition=["top right", "top left", "bottom right", "top left", "bottom right"],
        textfont=dict(size=12, color="#8892b0"),
        marker=dict(size=8, color="#00ffaa"),
        line=dict(color="#00ffaa", width=2, dash='solid'),
        cliponaxis=False
    ))

    # Projected Line (dashed)
    fig.add_trace(go.Scatter(
        x=x_dates[4:],
        y=y_vals[4:],
        mode="lines+markers+text",
        text=["", labels[5]],
        textposition=["top center", "bottom right"],
        textfont=dict(size=12, color="#00ffaa"),
        marker=dict(size=8, color="#00ffaa"),
        line=dict(color="#00ffaa", width=2, dash='dot'),
        cliponaxis=False
    ))
    
    # Target annotation
    fig.add_annotation(
        x="2027E", y=6.5,
        text="Target: Investment Banking →",
        showarrow=False,
        xshift=-80,
        yshift=20,
        font=dict(color="#00ffaa", size=13, weight="bold")
    )

    fig.update_layout(
        height=350,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=True, gridcolor="#233554", gridwidth=1, zeroline=False, tickfont=dict(color="#8892b0"), categoryorder="array", categoryarray=x_dates),
        yaxis=dict(showgrid=True, gridcolor="#233554", gridwidth=1, zeroline=False, showticklabels=False, range=[0, 8]),
        margin=dict(l=20, r=40, t=40, b=40)
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
