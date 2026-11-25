
from crewai import Task


def create_business_analysis_task(agent, business_description):
    return Task(
        description=f"""
        Analyze the following business in detail:

        BUSINESS DESCRIPTION:
        {business_description}

        Identify:
        1. The business model
        2. Target customers
        3. Main products or services
        4. Current business challenges
        5. Strengths and weaknesses
        6. Opportunities for improvement
        7. Key business risks

        Provide a clear, professional and practical business analysis.
        """,
        expected_output="A detailed business analysis covering the business model, customers, strengths, weaknesses, challenges, opportunities, and risks.",
        agent=agent
    )


def create_market_research_task(agent, business_description):
    return Task(
        description=f"""
        Conduct market research based on this business:

        BUSINESS DESCRIPTION:
        {business_description}

        Analyze:
        1. Target market
        2. Ideal customer profile
        3. Customer needs
        4. Market trends
        5. Competitor landscape
        6. Competitive advantages
        7. Market opportunities

        Do not invent specific statistics. Clearly identify assumptions.
        """,
        expected_output="A professional market research report covering target customers, trends, competitors, market opportunities, and assumptions.",
        agent=agent
    )


def create_marketing_strategy_task(agent, business_description):
    return Task(
        description=f"""
        Create a marketing strategy for this business:

        BUSINESS DESCRIPTION:
        {business_description}

        Include:
        1. Brand positioning
        2. Marketing objectives
        3. Target audience
        4. Social media strategy
        5. Content marketing plan
        6. Customer acquisition strategy
        7. Marketing campaign ideas
        8. Customer retention strategy

        Focus on realistic and affordable marketing actions.
        """,
        expected_output="A practical marketing strategy with branding, social media, content, customer acquisition, campaigns, and retention recommendations.",
        agent=agent
    )


def create_financial_analysis_task(agent, business_description):
    return Task(
        description=f"""
        Analyze the financial aspects of this business:

        BUSINESS DESCRIPTION:
        {business_description}

        Evaluate:
        1. Potential revenue streams
        2. Main operating costs
        3. Pricing strategy
        4. Profitability opportunities
        5. Budget considerations
        6. Financial risks
        7. Cost-saving recommendations

        If financial data is missing, clearly state your assumptions.
        Do not invent actual financial figures.
        """,
        expected_output="A financial business assessment covering revenue streams, costs, pricing, profitability, budget, risks, and financial recommendations.",
        agent=agent
    )


def create_growth_strategy_task(agent, business_description):
    return Task(
        description=f"""
        Develop a growth strategy for this business:

        BUSINESS DESCRIPTION:
        {business_description}

        Include:
        1. Short-term growth opportunities
        2. Long-term growth opportunities
        3. Business expansion ideas
        4. Operational improvements
        5. Customer retention
        6. Scaling strategy
        7. A prioritized action plan

        Make your recommendations practical and achievable.
        """,
        expected_output="A business growth plan with prioritized short-term and long-term strategies, operational improvements, expansion opportunities, and action steps.",
        agent=agent
    )
