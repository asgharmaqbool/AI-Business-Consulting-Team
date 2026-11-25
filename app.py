import os
import streamlit as st
from groq import Groq

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Business Decision Advisor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PREMIUM RESPONSIVE CSS
# =========================================================

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

.stApp {
    background: #08111F;
    color: #F1F5F9;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* ---------- HEADINGS ---------- */

h1, h2, h3, h4 {
    color: #F8FAFC !important;
    font-weight: 700 !important;
    letter-spacing: -0.4px;
}

h1 {
    font-size: 2.4rem !important;
}

h2 {
    font-size: 1.65rem !important;
}

h3 {
    font-size: 1.2rem !important;
}

p, li {
    color: #C4D0E0 !important;
}

/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101D30, #0A1424);
    border-right: 1px solid #24354D;
}

[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #EAF2FC !important;
}

[data-testid="stSidebar"] small {
    color: #A8B9D0 !important;
}

/* ---------- SIDEBAR NAVIGATION ---------- */

[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 8px;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    background: #14243A;
    border: 1px solid #243A57;
    border-radius: 12px;
    padding: 10px 12px;
    transition: all 0.2s ease;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background: #1B3352;
    border-color: #4B83C7;
}

/* ---------- HERO ---------- */

.hero-box {
    background: linear-gradient(
        120deg,
        #142943 0%,
        #173B67 55%,
        #102A49 100%
    );
    border: 1px solid #315A83;
    border-radius: 24px;
    padding: 35px 38px;
    margin-bottom: 26px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.18);
}

.hero-box h1 {
    font-size: 2.5rem !important;
    margin-bottom: 12px;
}

.hero-box p {
    color: #C9DAED !important;
    font-size: 1.05rem;
    line-height: 1.7;
}

/* ---------- CARDS ---------- */

.tool-card {
    background: linear-gradient(145deg, #14243A, #101C2E);
    border: 1px solid #283D59;
    border-radius: 18px;
    padding: 22px;
    min-height: 170px;
    margin-bottom: 12px;
    transition: transform 0.2s, border 0.2s;
}

.tool-card:hover {
    border-color: #5086C5;
    transform: translateY(-3px);
}

.tool-card h3 {
    margin-top: 0;
}

.tool-card p {
    font-size: 0.95rem;
    line-height: 1.55;
    color: #B8C9DD !important;
}

/* ---------- FORMS ---------- */

label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span {
    color: #E6EEF9 !important;
    font-weight: 600 !important;
}

/* Text fields, text areas and number inputs */

input,
textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {
    background-color: #F8FAFC !important;
    color: #111827 !important;
    caret-color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
    border-radius: 10px !important;
}

/* Placeholder text */

input::placeholder,
textarea::placeholder {
    color: #64748B !important;
    opacity: 1 !important;
    -webkit-text-fill-color: #64748B !important;
}

/* Text area */

textarea {
    min-height: 120px;
    border: 1px solid #D1D5DB !important;
}

/* Select boxes */

[data-baseweb="select"] > div {
    background-color: #F8FAFC !important;
    border-radius: 10px !important;
}

[data-baseweb="select"] span {
    color: #111827 !important;
}

/* Dropdown menu */

[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="popover"] *,
[data-baseweb="menu"] * {
    color: #111827 !important;
}

/* ---------- BUTTONS ---------- */

.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button {
    background: linear-gradient(135deg, #2878E5, #3B92FF) !important;
    color: #FFFFFF !important;
    border: 1px solid #4C96F8 !important;
    border-radius: 12px !important;
    min-height: 48px;
    padding: 10px 18px;
    font-weight: 700 !important;
    transition: all 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #3B92FF, #60A5FA) !important;
    border-color: #8BC0FF !important;
    transform: translateY(-1px);
}

/* ---------- METRICS ---------- */

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #172940, #122136);
    border: 1px solid #2A405D;
    border-radius: 16px;
    padding: 18px;
}

[data-testid="stMetricLabel"] {
    color: #AFC2D9 !important;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
}

/* ---------- ALERTS ---------- */

[data-testid="stAlert"] {
    border-radius: 12px;
}

/* ---------- DIVIDERS ---------- */

hr {
    border-color: #263B56 !important;
}

/* ---------- MOBILE RESPONSIVE ---------- */

@media (max-width: 768px) {

    .block-container {
        padding-top: 1.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        padding-bottom: 2rem;
    }

    h1 {
        font-size: 1.75rem !important;
    }

    h2 {
        font-size: 1.4rem !important;
    }

    h3 {
        font-size: 1.08rem !important;
    }

    .hero-box {
        padding: 22px 18px;
        border-radius: 18px;
    }

    .hero-box h1 {
        font-size: 1.8rem !important;
    }

    .hero-box p {
        font-size: 0.95rem;
    }

    .tool-card {
        padding: 17px;
        min-height: auto;
        border-radius: 14px;
    }

    input,
    textarea {
        font-size: 16px !important;
    }

    .stButton > button,
    .stFormSubmitButton > button,
    .stDownloadButton > button {
        width: 100%;
        min-height: 48px;
    }

}

/* ---------- SMALL MOBILE ---------- */

@media (max-width: 480px) {

    .block-container {
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }

    .hero-box {
        padding: 18px 15px;
    }

    .hero-box h1 {
        font-size: 1.55rem !important;
    }

    [data-testid="stSidebar"] {
        min-width: 260px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# AI CONNECTION
# =========================================================

def get_groq_client():

    api_key = None

    try:
        api_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        pass

    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        st.error("GROQ_API_KEY is missing from Streamlit Secrets.")
        return None

    return Groq(api_key=api_key)


def ask_ai(prompt, max_tokens=1200):

    client = get_groq_client()

    if client is None:
        return None

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are a professional business decision advisor.

Give practical, realistic and useful business advice.

Rules:
- Answer the user's actual question.
- Use simple language.
- Avoid unnecessary explanations.
- Do not repeat information.
- Do not invent statistics.
- Clearly label estimates and assumptions.
- Give actionable recommendations.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    except Exception as e:

        error = str(e).lower()

        if "rate_limit" in error or "rate limit" in error:
            st.warning("AI is temporarily busy. Please wait and try again.")
        else:
            st.error("We could not generate your result. Please try again.")

        return None


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div style="padding:10px 0 20px 0;">
        <div style="font-size:42px;">📈</div>
        <h2 style="margin-bottom:0;">AI Business</h2>
        <h3 style="color:#78AFFF !important;margin-top:5px;">
            Decision Advisor
        </h3>
        <p style="color:#A8B9D0 !important;">
            From business idea to smarter decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "💡 Idea Validator",
            "💰 Investment Calculator",
            "🔎 Market Opportunity",
            "📣 Marketing Builder",
            "📅 30-Day Launch Planner",
            "📄 Business Report"
        ],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("""
    <div style="
        background:linear-gradient(145deg,#172B46,#102035);
        border:1px solid #304967;
        padding:16px;
        border-radius:16px;
    ">
        <h3>🚀 Plan Smart</h3>
        <p>Grow Faster</p>
        <p style="font-size:13px;color:#B8C9DD;">
        Make smarter business decisions before investing.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("AI Business Decision Advisor · V2")


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero-box">
        <h1>Make Smarter Business Decisions</h1>
        <h3>Plan your business before you invest.</h3>
        <p>
        Validate your ideas, understand your investment,
        explore opportunities and create your business roadmap.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Explore Business Tools")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="tool-card">
            <h3>💡 Idea Validator</h3>
            <p>Is your business idea worth starting?</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="tool-card">
            <h3>💰 Investment Calculator</h3>
            <p>Calculate startup costs and potential profit.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="tool-card">
            <h3>🔎 Market Opportunity</h3>
            <p>Find customers, market gaps and opportunities.</p>
        </div>
        """, unsafe_allow_html=True)

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown("""
        <div class="tool-card">
            <h3>📣 Marketing Builder</h3>
            <p>Build a practical marketing strategy.</p>
        </div>
        """, unsafe_allow_html=True)

    with c5:
        st.markdown("""
        <div class="tool-card">
            <h3>📅 30-Day Launch Planner</h3>
            <p>Get a step-by-step startup roadmap.</p>
        </div>
        """, unsafe_allow_html=True)

    with c6:
        st.markdown("""
        <div class="tool-card">
            <h3>📄 Business Report</h3>
            <p>Get a complete business evaluation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("How it works")

    a, b, c = st.columns(3)

    with a:
        st.markdown("### ① Tell us your idea")
        st.caption("Describe the business you want to start.")

    with b:
        st.markdown("### ② Enter your budget")
        st.caption("Set your investment and business goals.")

    with c:
        st.markdown("### ③ Get your plan")
        st.caption("Receive recommendations and next steps.")


# =========================================================
# IDEA VALIDATOR
# =========================================================

elif page == "💡 Idea Validator":

    st.markdown("""
    <div class="hero-box">
        <h1>💡 Business Idea Validator</h1>
        <p>Evaluate your idea before investing your money.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("idea_form"):

        idea = st.text_area(
            "Describe your business idea",
            placeholder="Example: I want to start a biryani delivery business...",
            height=130
        )

        location = st.text_input(
            "Business location",
            placeholder="Example: Lahore, Pakistan"
        )

        budget = st.number_input(
            "Available investment (PKR)",
            min_value=0,
            value=300000,
            step=50000
        )

        experience = st.selectbox(
            "Business experience",
            ["Beginner", "Some experience", "Experienced"]
        )

        submit = st.form_submit_button("🚀 Evaluate My Idea")

    if submit:

        if not idea.strip():
            st.warning("Please describe your business idea.")

        else:

            prompt = f"""
Evaluate this business idea.

Idea: {idea}
Location: {location}
Budget: PKR {budget:,}
Experience: {experience}

Provide:
1. Verdict: Start / Test First / Avoid
2. Potential: Low / Medium / High
3. Main opportunity
4. Three major risks
5. Recommended approach
6. Three next actions

Be realistic, concise, and practical.
Do not invent market statistics.
"""

            with st.spinner("Evaluating your business idea..."):

                result = ask_ai(prompt, 1000)

            if result:
                st.markdown("---")
                st.subheader("Your Business Evaluation")
                st.markdown(result)


# =========================================================
# INVESTMENT CALCULATOR
# =========================================================

elif page == "💰 Investment Calculator":

    st.markdown("""
    <div class="hero-box">
        <h1>💰 Investment Calculator</h1>
        <p>Understand your startup capital, expenses and break-even.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        equipment = st.number_input(
            "Equipment & Setup (PKR)",
            min_value=0,
            value=100000,
            step=10000
        )

        stock = st.number_input(
            "Initial Stock (PKR)",
            min_value=0,
            value=50000,
            step=10000
        )

        startup_other = st.number_input(
            "Other Startup Costs (PKR)",
            min_value=0,
            value=25000,
            step=5000
        )

    with c2:

        rent = st.number_input(
            "Monthly Rent (PKR)",
            min_value=0,
            value=30000,
            step=5000
        )

        salaries = st.number_input(
            "Monthly Salaries (PKR)",
            min_value=0,
            value=40000,
            step=5000
        )

        monthly_other = st.number_input(
            "Other Monthly Expenses (PKR)",
            min_value=0,
            value=20000,
            step=5000
        )

    st.markdown("### Sales & Profit Assumptions")

    c1, c2 = st.columns(2)

    with c1:

        sales = st.number_input(
            "Expected Monthly Sales (PKR)",
            min_value=0,
            value=200000,
            step=25000
        )

        product_cost_percent = st.slider(
            "Product / Food Cost (%)",
            0, 100, 40
        )

    with c2:

        budget_available = st.number_input(
            "Available Budget (PKR)",
            min_value=0,
            value=300000,
            step=50000
        )

        reserve_months = st.number_input(
            "Reserve Months",
            min_value=0,
            max_value=24,
            value=3
        )

    startup_total = equipment + stock + startup_other
    fixed_monthly = rent + salaries + monthly_other
    variable_cost = sales * product_cost_percent / 100
    estimated_profit = sales - variable_cost - fixed_monthly

    margin = 1 - product_cost_percent / 100

    break_even = fixed_monthly / margin if margin > 0 else 0

    reserve = fixed_monthly * reserve_months
    recommended_capital = startup_total + reserve

    if st.button("🧮 Calculate My Business"):

        st.markdown("---")
        st.subheader("Your Financial Results")

        c1, c2, c3 = st.columns(3)

        c1.metric("Startup Cost", f"Rs. {startup_total:,.0f}")
        c2.metric("Monthly Expenses", f"Rs. {fixed_monthly:,.0f}")
        c3.metric("Estimated Profit", f"Rs. {estimated_profit:,.0f}")

        c1, c2 = st.columns(2)

        c1.metric("Break-even Sales", f"Rs. {break_even:,.0f}")
        c2.metric("Recommended Capital", f"Rs. {recommended_capital:,.0f}")

        if recommended_capital <= budget_available:
            st.success("Your budget covers the estimated startup and reserve.")
        else:
            st.warning(
                f"Estimated budget shortage: "
                f"Rs. {recommended_capital - budget_available:,.0f}"
            )

        if estimated_profit > 0:
            st.success("Your business shows potential operating profit based on these inputs.")
        else:
            st.error("Your business currently shows an estimated operating loss.")

        st.caption(
            "Results are estimates based on your inputs. Taxes, financing, "
            "unexpected costs and other expenses are not included unless entered."
        )


# =========================================================
# MARKET OPPORTUNITY
# =========================================================

elif page == "🔎 Market Opportunity":

    st.markdown("""
    <div class="hero-box">
        <h1>🔎 Market Opportunity</h1>
        <p>Discover customers, competition and potential opportunities.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("market_form"):

        business = st.text_input("Business idea")

        location = st.text_input("City / Market")

        customers = st.text_input("Target customers (optional)")

        submit = st.form_submit_button("🔎 Analyze Market")

    if submit:

        if not business.strip():
            st.warning("Please enter your business idea.")

        else:

            prompt = f"""
Analyze this business market.

Business: {business}
Location: {location}
Customers: {customers or "Identify target customers"}

Include:
- Target customers
- Customer needs
- Competition challenges
- Competitive advantages
- Three market opportunities
- Recommended positioning

Do not invent statistics or claim live market research.
"""

            with st.spinner("Analyzing market opportunity..."):

                result = ask_ai(prompt, 1200)

            if result:
                st.subheader("Market Opportunity Report")
                st.markdown(result)
                st.info("This analysis does not include verified live market data.")


# =========================================================
# MARKETING BUILDER
# =========================================================

elif page == "📣 Marketing Builder":

    st.markdown("""
    <div class="hero-box">
        <h1>📣 Marketing Builder</h1>
        <p>Find affordable ways to attract and retain customers.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("marketing_form"):

        business = st.text_input("Business idea or name")

        location = st.text_input("Business location")

        budget = st.number_input(
            "Monthly Marketing Budget (PKR)",
            min_value=0,
            value=20000,
            step=5000
        )

        customer = st.text_input("Target customers")

        submit = st.form_submit_button("📣 Build My Strategy")

    if submit:

        if not business.strip():
            st.warning("Please enter your business idea.")

        else:

            prompt = f"""
Create a practical marketing strategy.

Business: {business}
Location: {location}
Budget: PKR {budget:,}/month
Customers: {customer}

Include:
- Brand positioning
- Best marketing channels
- Five content ideas
- Three offers
- Customer acquisition
- Customer retention
- 7-day action plan

Keep everything affordable and practical.
"""

            with st.spinner("Building your marketing strategy..."):

                result = ask_ai(prompt, 1500)

            if result:
                st.subheader("Your Marketing Strategy")
                st.markdown(result)


# =========================================================
# 30-DAY LAUNCH PLANNER
# =========================================================

elif page == "📅 30-Day Launch Planner":

    st.markdown("""
    <div class="hero-box">
        <h1>📅 30-Day Launch Planner</h1>
        <p>Turn your idea into a step-by-step launch plan.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("launch_form"):

        business = st.text_input("Business idea")

        location = st.text_input("Location")

        budget = st.number_input(
            "Available Budget (PKR)",
            min_value=0,
            value=200000,
            step=50000
        )

        experience = st.selectbox(
            "Experience",
            ["Beginner", "Some experience", "Experienced"]
        )

        submit = st.form_submit_button("📅 Create My Launch Plan")

    if submit:

        if not business.strip():
            st.warning("Please enter your business idea.")

        else:

            prompt = f"""
Create a realistic 30-day launch plan.

Business: {business}
Location: {location}
Budget: PKR {budget:,}
Experience: {experience}

Divide it into:

Week 1: Research and validation
Week 2: Preparation and setup
Week 3: Product and marketing preparation
Week 4: Launch and improvement

Include clear weekly tasks, priorities, budget awareness,
and five final launch checkpoints.
"""

            with st.spinner("Creating your launch plan..."):

                result = ask_ai(prompt, 1800)

            if result:
                st.subheader("Your 30-Day Roadmap")
                st.markdown(result)


# =========================================================
# BUSINESS REPORT
# =========================================================

elif page == "📄 Business Report":

    st.markdown("""
    <div class="hero-box">
        <h1>📄 Business Decision Report</h1>
        <p>Get a complete evaluation from your five AI business consultants.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("report_form"):

        description = st.text_area(
            "Describe your business",
            height=150,
            placeholder="Business idea, location, customers, budget and goals..."
        )

        location = st.text_input("Business Location")

        budget = st.number_input(
            "Available Investment (PKR)",
            min_value=0,
            value=300000,
            step=50000
        )

        submit = st.form_submit_button("📄 Generate Business Report")

    if submit:

        if not description.strip():
            st.warning("Please describe your business.")

        else:

            complete_description = f"""
Business:
{description}

Location:
{location}

Available Investment:
PKR {budget:,}

Prepare a professional business evaluation.
Focus on feasibility, risks, finances, marketing and growth.
"""

            try:

                with st.spinner("Our five consultants are working..."):

                    from crew import create_consulting_crew

                    crew = create_consulting_crew(complete_description)

                    result = crew.kickoff()

                report_text = str(result)

                st.subheader("Your Business Decision Report")

                st.markdown(report_text)

                st.download_button(
                    "📥 Download Report",
                    report_text,
                    file_name="business_decision_report.txt",
                    mime="text/plain"
                )

            except Exception:

                st.error(
                    "We could not generate your report. "
                    "Please try again or check your deployment logs."
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div style="text-align:center;color:#8195AE;padding:10px;">
AI Business Decision Advisor · Make smarter decisions before investing.
</div>
""", unsafe_allow_html=True)
