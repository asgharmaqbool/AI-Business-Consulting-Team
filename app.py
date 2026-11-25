
import os
import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Business Consulting Team",
    page_icon="🧠",
    layout="wide"
)

# --------------------------------------------------
# API KEY CONFIGURATION
# --------------------------------------------------

def configure_api_key():
    try:
        if "GROQ_API_KEY" in st.secrets:
            os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    except Exception:
        pass

    return os.getenv("GROQ_API_KEY")


# --------------------------------------------------
# CUSTOM UI DESIGN
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f4f7fb;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #173b67;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #52657a;
    margin-bottom: 30px;
}

.agent-card {
    background: white;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #e1e8f0;
    text-align: center;
    box-shadow: 0 3px 10px rgba(0,0,0,0.04);
}

div.stButton > button {
    background-color: #1769aa;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 12px 25px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #124e82;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🧠 AI Business Consulting Team</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI-powered team of business experts '
    'for research, strategy, financial insights and business growth.</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# TEAM INTRODUCTION
# --------------------------------------------------

st.subheader("👥 Meet Your AI Consulting Team")

col1, col2, col3, col4, col5 = st.columns(5)

agents_info = [
    ("🧠", "Business Analyst", "Business analysis & planning"),
    ("🔎", "Market Researcher", "Markets & competitors"),
    ("📢", "Marketing Strategist", "Marketing & customers"),
    ("💰", "Financial Advisor", "Costs & profitability"),
    ("📈", "Growth Consultant", "Expansion & scaling")
]

columns = [col1, col2, col3, col4, col5]

for col, info in zip(columns, agents_info):
    with col:
        st.markdown(
            f"""
            <div class="agent-card">
                <h2>{info[0]}</h2>
                <h4>{info[1]}</h4>
                <p>{info[2]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()


# --------------------------------------------------
# BUSINESS INPUT
# --------------------------------------------------

st.subheader("🏢 Tell Us About Your Business")

st.write(
    "Describe your business, idea, product, service, or challenge. "
    "Our AI consulting team will analyze it and prepare a consulting report."
)

business_description = st.text_area(
    "Business Description",
    placeholder=(
        "Example: I want to start an online clothing business in Pakistan. "
        "My target customers are young adults. I have a small budget and "
        "want to sell through Instagram and my own website..."
    ),
    height=220,
    max_chars=10000
)

analyze_button = st.button(
    "🚀 Analyze My Business",
    use_container_width=True
)


# --------------------------------------------------
# AI ANALYSIS
# --------------------------------------------------

if analyze_button:

    if not business_description.strip():

        st.warning("Please enter your business description first.")

    else:

        api_key = configure_api_key()

        if not api_key:

            st.error(
                "Groq API key is missing. Please configure "
                "GROQ_API_KEY in your Streamlit Secrets."
            )

        else:

            try:

                with st.spinner(
                    "🤖 Your AI consulting team is working... "
                    "This may take several minutes."
                ):

                    from crew import create_consulting_crew

                    consulting_crew = create_consulting_crew(
                        business_description
                    )

                    result = consulting_crew.kickoff()

                st.success("🎉 Your business analysis is complete!")

                st.markdown("## 📊 Your Business Consulting Report")

                report = getattr(result, "raw", str(result))

                # Safely display the generated report
                with st.container(border=True):
                    st.markdown(report)

                # Download report
                st.download_button(
                    label="📥 Download Consulting Report",
                    data=str(report),
                    file_name="AI_Business_Consulting_Report.txt",
                    mime="text/plain"
                )

            except Exception as e:

                error_message = str(e).lower()

                if (
                    "rate_limit" in error_message
                    or "rate limit" in error_message
                    or "tokens per minute" in error_message
                    or "tpm" in error_message
                ):

                    st.warning(
                        "⏳ Our AI consultants are receiving too many "
                        "requests right now, or the request is too large. "
                        "Please wait a little and try again."
                    )

                elif "timeout" in error_message:

                    st.warning(
                        "⏳ The analysis took too long. "
                        "Please try again with a shorter business description."
                    )

                else:

                    st.error(
                        "We couldn't complete your business analysis. "
                        "Please try again in a few minutes."
                    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#64748b;">
        🤖 Powered by AI • Groq • CrewAI • Streamlit
        <br>
        AI Business Consulting Team
    </div>
    """,
    unsafe_allow_html=True
)
