import os
import streamlit as st
from groq import Groq

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Business Decision Advisor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0B1220;
    color: #F1F5F9;
}

[data-testid="stSidebar"] {
    background-color: #101B2D;
    border-right: 1px solid #263750;
}

h1, h2, h3 {
    color: #F8FAFC !important;
}

p, label, span {
    color: inherit;
}

div[data-testid="stMetric"] {
    background: #16243A;
    padding: 18px;
    border: 1px solid #293C57;
    border-radius: 14px;
}

div.stButton > button {
    background: linear-gradient(90deg, #2563EB, #3B82F6);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1rem;
    font-weight: 600;
}

div.stButton > button:hover {
    border: 1px solid #60A5FA;
    color: white;
}

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #2563EB, #3B82F6);
    color: white;
    border-radius: 10px;
    font-weight: bold;
}

.tool-card {
    background: #16243A;
    border: 1px solid #293C57;
    padding: 20px;
    border-radius: 16px;
    min-height: 150px;
}

.hero {
    background: linear-gradient(120deg, #142641, #1E3A65);
    border: 1px solid #31557D;
    padding: 30px;
    border-radius: 20px;
}

.small-note {
    color: #9CAFC8;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# GROQ CONNECTION
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
        st.error(
            "GROQ_API_KEY is missing. "
            "Please add your API key in Streamlit Secrets."
        )
        return None

    return Groq(api_key=api_key)


# =========================================================
# AI RESPONSE FUNCTION
# =========================================================

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
You are an experienced business decision advisor.

Your job is to provide practical, realistic and useful
business advice.

Rules:
- Answer exactly what the user needs.
- Use simple and easy language.
- Avoid unnecessary explanations.
- Do not repeat information.
- Never invent market statistics.
- Clearly label estimates and assumptions.
- Keep the response organized.
- Do not act like a generic chatbot.
- Focus on decisions and actions.
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

            st.warning(
                "The AI is temporarily busy. "
                "Please wait a little and try again."
            )

        else:

            st.error(
                "We could not generate your result. "
                "Please try again."
            )

        return None


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown("# 📈")
    st.markdown("## AI Business")
    st.markdown("### Decision Advisor")

    st.caption("From business idea to smarter decisions.")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "💡 Idea Validator",
            "💰 Investment Calculator",
            "🔎 Market Opportunity",
            "📣 Marketing Builder",
            "📅 30-Day Launch Planner",
            "📄 Business Report"
        ]
    )

    st.divider()

    st.markdown("### 🎯 Our Mission")
    st.caption(
        "Helping entrepreneurs make smarter decisions "
        "before investing their money."
    )

    st.divider()

    st.caption("Version 2.0 | Business Decision Advisor")


# =========================================================
# HOME DASHBOARD
# =========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>Make Smarter Business Decisions</h1>
        <h3>Before you invest your money.</h3>
        <p>
        Evaluate your business ideas, calculate your investment,
        understand your risks and create your action plan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🚀 Our Business Tools")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tool-card">
        <h3>💡 Idea Validator</h3>
        <p>Find out if your business idea is worth starting.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tool-card">
        <h3>💰 Investment Calculator</h3>
        <p>Calculate your costs, investment and break-even.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tool-card">
        <h3>🔎 Market Opportunity</h3>
        <p>Understand customers, competition and opportunities.</p>
        </div>
        """, unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class="tool-card">
        <h3>📣 Marketing Builder</h3>
        <p>Discover practical ways to attract customers.</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="tool-card">
        <h3>📅 30-Day Launch Planner</h3>
        <p>Follow a step-by-step business launch plan.</p>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class="tool-card">
        <h3>📄 Business Report</h3>
        <p>Get a complete professional business evaluation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.info(
        "👈 Choose a business tool from the sidebar "
        "to get started."
    )

    st.subheader("How It Works")

    step1, step2, step3 = st.columns(3)

    with step1:
        st.markdown("### ①")
        st.write("Tell us about your idea")

    with step2:
        st.markdown("### ②")
        st.write("Enter your budget and goals")

    with step3:
        st.markdown("### ③")
        st.write("Get your business decision and action plan")


# =========================================================
# IDEA VALIDATOR
# =========================================================

elif page == "💡 Idea Validator":

    st.title("💡 Business Idea Validator")

    st.write(
        "Find out whether your business idea is worth pursuing."
    )

    with st.form("idea_validator_form"):

        idea = st.text_area(
            "Describe your business idea",
            placeholder="Example: I want to start a burger business on Foodpanda...",
            height=120
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
            "Your business experience",
            ["Beginner", "Some experience", "Experienced"]
        )

        submitted = st.form_submit_button(
            "Evaluate My Idea",
            use_container_width=True
        )

    if submitted:

        if not idea.strip():

            st.warning("Please describe your business idea.")

        else:

            prompt = f"""
Evaluate the following business idea.

BUSINESS IDEA:
{idea}

LOCATION:
{location if location else "Not specified"}

AVAILABLE INVESTMENT:
PKR {budget:,}

BUSINESS EXPERIENCE:
{experience}

Provide your assessment in this exact structure:

1. VERDICT: Start / Test First / Avoid for Now
2. POTENTIAL: Low / Medium / High
3. MAIN OPPORTUNITY: One or two sentences
4. MAIN RISKS: Three important risks
5. RECOMMENDED APPROACH: Practical advice
6. NEXT 3 ACTIONS: Three actions the user should take

Be realistic.
Do not invent market statistics.
Consider the user's available investment.
Use simple language.
"""

            with st.spinner("Evaluating your business idea..."):

                result = ask_ai(prompt, max_tokens=1000)

            if result:

                st.divider()
                st.subheader("Your Business Evaluation")
                st.markdown(result)


# =========================================================
# INVESTMENT CALCULATOR
# =========================================================

elif page == "💰 Investment Calculator":

    st.title("💰 Business Investment Calculator")

    st.write(
        "Calculate your estimated startup investment, monthly costs "
        "and possible profitability."
    )

    col1, col2 = st.columns(2)

    with col1:

        startup_cost = st.number_input(
            "Equipment & Setup (PKR)",
            min_value=0,
            value=100000,
            step=10000
        )

        stock_cost = st.number_input(
            "Initial Stock / Inventory (PKR)",
            min_value=0,
            value=50000,
            step=10000
        )

        other_startup = st.number_input(
            "Other Startup Costs (PKR)",
            min_value=0,
            value=25000,
            step=5000
        )

    with col2:

        monthly_rent = st.number_input(
            "Monthly Rent (PKR)",
            min_value=0,
            value=30000,
            step=5000
        )

        monthly_salary = st.number_input(
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

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        monthly_sales = st.number_input(
            "Expected Monthly Sales (PKR)",
            min_value=0,
            value=200000,
            step=25000
        )

        cost_percentage = st.slider(
            "Product / Food Cost (%)",
            min_value=0,
            max_value=100,
            value=40
        )

    with col2:

        available_budget = st.number_input(
            "Your Available Budget (PKR)",
            min_value=0,
            value=300000,
            step=50000
        )

        reserve_months = st.number_input(
            "Working Capital Reserve (Months)",
            min_value=0,
            max_value=24,
            value=3
        )

    # Real calculations

    total_startup = (
        startup_cost
        + stock_cost
        + other_startup
    )

    monthly_fixed = (
        monthly_rent
        + monthly_salary
        + monthly_other
    )

    monthly_variable_cost = (
        monthly_sales * cost_percentage / 100
    )

    monthly_profit = (
        monthly_sales
        - monthly_variable_cost
        - monthly_fixed
    )

    contribution_margin = (
        1 - cost_percentage / 100
    )

    if contribution_margin > 0:

        break_even_sales = (
            monthly_fixed / contribution_margin
        )

    else:

        break_even_sales = 0

    reserve_needed = monthly_fixed * reserve_months

    total_needed = total_startup + reserve_needed

    st.divider()

    if st.button("Calculate My Business", use_container_width=True):

        st.subheader("📊 Your Financial Results")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Startup Cost",
            f"Rs. {total_startup:,.0f}"
        )

        col2.metric(
            "Monthly Expenses",
            f"Rs. {monthly_fixed:,.0f}"
        )

        col3.metric(
            "Estimated Monthly Profit",
            f"Rs. {monthly_profit:,.0f}"
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Break-even Sales",
            f"Rs. {break_even_sales:,.0f}/month"
        )

        col2.metric(
            "Total Recommended Capital",
            f"Rs. {total_needed:,.0f}"
        )

        st.divider()

        if total_needed <= available_budget:

            st.success(
                f"Your available budget covers the estimated startup "
                f"cost and {reserve_months} months of reserves."
            )

        else:

            shortage = total_needed - available_budget

            st.warning(
                f"Estimated budget shortfall: Rs. {shortage:,.0f}"
            )

        if monthly_profit > 0:

            st.success(
                "Your business shows a potential operating profit "
                "based on the numbers entered."
            )

        else:

            st.error(
                "Based on your inputs, the business is currently "
                "estimated to operate at a loss."
            )

        st.caption(
            "These calculations are estimates based on your inputs. "
            "They do not include taxes, financing costs, unexpected "
            "expenses, or other costs unless entered above."
        )


# =========================================================
# MARKET OPPORTUNITY
# =========================================================

elif page == "🔎 Market Opportunity":

    st.title("🔎 Market Opportunity Analyzer")

    st.write(
        "Explore your target customers, competition and potential opportunities."
    )

    with st.form("market_form"):

        business_type = st.text_input(
            "Business idea",
            placeholder="Example: Affordable burger delivery business"
        )

        market_location = st.text_input(
            "Target city or market",
            placeholder="Example: Lahore, Pakistan"
        )

        target_customer = st.text_input(
            "Target customer (optional)",
            placeholder="Example: Students and office workers"
        )

        market_submit = st.form_submit_button(
            "Analyze Market Opportunity",
            use_container_width=True
        )

    if market_submit:

        if not business_type.strip():

            st.warning("Please enter your business idea.")

        else:

            prompt = f"""
Analyze the business market opportunity.

BUSINESS:
{business_type}

LOCATION:
{market_location}

TARGET CUSTOMER:
{target_customer if target_customer else "Identify suitable customers"}

Provide:

1. Target customers
2. Customer problems and needs
3. Potential competitive advantages
4. Main competition challenges
5. Three market opportunities
6. Recommended positioning

Do not invent real market statistics or claim live market research.
Use realistic assumptions and simple language.
"""

            with st.spinner("Analyzing the opportunity..."):

                result = ask_ai(prompt, max_tokens=1200)

            if result:

                st.subheader("Market Opportunity Report")
                st.markdown(result)

                st.info(
                    "This report is AI-generated and does not use "
                    "live market data or verified competitor research."
                )


# =========================================================
# MARKETING BUILDER
# =========================================================

elif page == "📣 Marketing Builder":

    st.title("📣 Marketing Strategy Builder")

    st.write(
        "Create a practical marketing strategy for your business."
    )

    with st.form("marketing_form"):

        marketing_business = st.text_input(
            "Business name or idea"
        )

        marketing_location = st.text_input(
            "Business location"
        )

        marketing_budget = st.number_input(
            "Monthly Marketing Budget (PKR)",
            min_value=0,
            value=20000,
            step=5000
        )

        marketing_customer = st.text_input(
            "Target customers",
            placeholder="Example: Families, students, young professionals"
        )

        marketing_submit = st.form_submit_button(
            "Build My Marketing Strategy",
            use_container_width=True
        )

    if marketing_submit:

        if not marketing_business.strip():

            st.warning("Please enter your business idea.")

        else:

            prompt = f"""
Create a practical marketing strategy.

BUSINESS:
{marketing_business}

LOCATION:
{marketing_location}

MONTHLY MARKETING BUDGET:
PKR {marketing_budget:,}

TARGET CUSTOMERS:
{marketing_customer if marketing_customer else "Identify target customers"}

Include:

1. Brand positioning
2. Best marketing channels
3. Five content ideas
4. Three promotional offers
5. Customer acquisition ideas
6. Customer retention ideas
7. A 7-day marketing action plan

Keep the strategy affordable and practical.
Do not invent market statistics.
"""

            with st.spinner("Building your marketing strategy..."):

                result = ask_ai(prompt, max_tokens=1500)

            if result:

                st.subheader("Your Marketing Plan")
                st.markdown(result)


# =========================================================
# 30-DAY LAUNCH PLANNER
# =========================================================

elif page == "📅 30-Day Launch Planner":

    st.title("📅 30-Day Business Launch Planner")

    st.write(
        "Create a practical roadmap for launching your business "
        "within 30 days."
    )

    with st.form("launch_form"):

        launch_business = st.text_input(
            "Business idea",
            placeholder="Example: Home-based bakery"
        )

        launch_location = st.text_input(
            "Business location"
        )

        launch_budget = st.number_input(
            "Available investment (PKR)",
            min_value=0,
            value=200000,
            step=50000
        )

        launch_experience = st.selectbox(
            "Experience level",
            ["Beginner", "Some experience", "Experienced"]
        )

        launch_submit = st.form_submit_button(
            "Create My 30-Day Plan",
            use_container_width=True
        )

    if launch_submit:

        if not launch_business.strip():

            st.warning("Please enter your business idea.")

        else:

            prompt = f"""
Create a realistic 30-day launch plan.

BUSINESS:
{launch_business}

LOCATION:
{launch_location}

BUDGET:
PKR {launch_budget:,}

EXPERIENCE:
{launch_experience}

Organize the plan into four weeks:

WEEK 1: Research and validation
WEEK 2: Preparation and setup
WEEK 3: Product, operations and marketing preparation
WEEK 4: Launch and improvement

For each week:
- Give clear tasks.
- Focus on actions the user can actually complete.
- Respect the user's budget.
- Prioritize important tasks.
- Avoid unnecessary expenses.

End with 5 launch success checkpoints.
"""

            with st.spinner("Creating your launch roadmap..."):

                result = ask_ai(prompt, max_tokens=1800)

            if result:

                st.subheader("Your 30-Day Roadmap")
                st.markdown(result)


# =========================================================
# BUSINESS REPORT
# =========================================================

elif page == "📄 Business Report":

    st.title("📄 Business Decision Report")

    st.write(
        "Generate a structured report for a business idea "
        "using our five AI business consultants."
    )

    with st.form("business_report_form"):

        report_business = st.text_area(
            "Describe your business",
            placeholder="Describe your business idea, customers, location, budget, goals and concerns.",
            height=150
        )

        report_location = st.text_input(
            "Business location"
        )

        report_budget = st.number_input(
            "Available Investment (PKR)",
            min_value=0,
            value=300000,
            step=50000
        )

        report_submit = st.form_submit_button(
            "Generate Business Report",
            use_container_width=True
        )

    if report_submit:

        if not report_business.strip():

            st.warning("Please describe your business.")

        else:

            complete_description = f"""
BUSINESS DESCRIPTION:
{report_business}

LOCATION:
{report_location}

AVAILABLE INVESTMENT:
PKR {report_budget:,}

Prepare a professional business decision report.
Focus on realistic recommendations, risks, budget,
market opportunity, marketing and growth.
"""

            try:

                with st.spinner(
                    "Our five business consultants are working..."
                ):

                    from crew import create_consulting_crew

                    crew = create_consulting_crew(
                        complete_description
                    )

                    result = crew.kickoff()

                st.subheader("Your Business Decision Report")

                st.markdown(str(result))

                report_text = str(result)

                st.download_button(
                    label="📥 Download Business Report",
                    data=report_text,
                    file_name="business_decision_report.txt",
                    mime="text/plain",
                    use_container_width=True
                )

            except Exception:

                st.error(
                    "We could not generate the full business report. "
                    "Please try again later or use one of our other tools."
                )

                st.info(
                    "If the problem continues, check the Streamlit "
                    "deployment logs."
                )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Business Decision Advisor | Make smarter decisions before investing."
)
