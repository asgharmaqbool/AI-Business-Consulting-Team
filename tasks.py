
from crewai import Task


def create_business_analysis_task(agent, business_description):
    return Task(
        description=f"""
        Analyze this business:

        {business_description}

        Identify:
        - Business model and main offerings
        - Target customers
        - Strengths and weaknesses
        - Main challenges and risks
        - Best opportunities

        Be specific, practical, and concise.
        Avoid repeating the business description.
        """,
        expected_output="A concise business analysis with key findings and recommendations, maximum 250 words.",
        agent=agent
    )


def create_market_research_task(agent, business_description):
    return Task(
        description="""
        Using the business analysis provided in context, analyze:
        - Target market and ideal customers
        - Customer needs and buying behavior
        - Market trends
        - Competitors and competitive advantages
        - Market opportunities

        Do not invent statistics or unsupported facts.
        State assumptions clearly.

        Focus on useful findings rather than repeating the business analysis.
        """,
        expected_output="Concise market research findings and opportunities, maximum 250 words.",
        agent=agent
    )


def create_marketing_strategy_task(agent, business_description):
    return Task(
        description="""
        Using the business analysis and market research provided in context,
        create a practical marketing strategy.

        Include:
        - Brand positioning
        - Ideal customer
        - Affordable marketing channels
        - Social media and content ideas
        - Customer acquisition
        - Customer retention
        - Three practical marketing actions

        Prioritize affordable, realistic ideas.
        Avoid repeating previous task outputs.
        """,
        expected_output="A practical marketing strategy with prioritized recommendations, maximum 250 words.",
        agent=agent
    )


def create_financial_analysis_task(agent, business_description):
    return Task(
        description="""
        Using the business analysis provided in context, evaluate:

        - Revenue opportunities
        - Main expenses
        - Pricing approach
        - Profitability
        - Budget priorities
        - Financial risks
        - Cost-saving ideas

        If financial information is unavailable, provide reasonable estimates
        only when clearly labeled as assumptions.
        Do not present assumptions as verified facts.
        """,
        expected_output="A concise financial assessment and practical recommendations, maximum 250 words.",
        agent=agent
    )


def create_growth_strategy_task(agent, business_description):
    return Task(
        description="""
        Use all previous consultant findings to create a business growth plan.

        Include:
        - Immediate priorities
        - Short-term growth opportunities
        - Long-term expansion ideas
        - Operational improvements
        - Customer retention
        - Three to five prioritized action steps

        Focus on realistic actions and avoid repeating previous reports.
        """,
        expected_output="A concise, prioritized business growth plan, maximum 250 words.",
        agent=agent
    )

