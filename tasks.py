
from crewai import Task


def create_business_analysis_task(agent, business_description):
    return Task(
        description=f"""
        Understand the user's question:

        {business_description}

        Answer according to what the user actually asks.

        RULES:
        - If the question is simple, answer in ONE short sentence.
        - If the user asks for suggestions, give only relevant suggestions.
        - Do not create a business report unless requested.
        - Do not add unnecessary headings or explanations.
        - Keep the answer practical, clear, and easy to understand.
        - If the user asks for detailed analysis, provide detail accordingly.
        """,
        expected_output="A direct, relevant answer. For simple questions, maximum one short sentence.",
        agent=agent
    )


def create_market_research_task(agent, business_description):
    return Task(
        description=f"""
        User's question:

        {business_description}

        Provide market insight only if it is relevant to the question.

        RULES:
        - For simple questions, provide only one short sentence.
        - Do not repeat the business analysis.
        - Do not provide unnecessary market reports.
        - Do not invent statistics or facts.
        - Give detailed research only if the user requests it.
        """,
        expected_output="One short, relevant market insight unless detailed research is requested.",
        agent=agent
    )


def create_marketing_strategy_task(agent, business_description):
    return Task(
        description=f"""
        User's question:

        {business_description}

        Give marketing advice only when it is relevant.

        RULES:
        - Keep simple answers to one short sentence.
        - Give suggestions only when requested.
        - Avoid lengthy marketing strategies.
        - Do not repeat previous answers.
        - Provide a detailed strategy only when specifically requested.
        """,
        expected_output="A short and useful marketing suggestion unless a detailed strategy is requested.",
        agent=agent
    )


def create_financial_analysis_task(agent, business_description):
    return Task(
        description=f"""
        User's question:

        {business_description}

        Discuss costs, budgets, or profits only when relevant.

        RULES:
        - Keep simple answers short and direct.
        - Do not provide unnecessary financial calculations.
        - Never invent financial facts.
        - Clearly identify estimates when required.
        - Give a detailed financial analysis only when requested.
        """,
        expected_output="A concise financial answer relevant to the user's question.",
        agent=agent
    )


def create_growth_strategy_task(agent, business_description):
    return Task(
        description=f"""
        User's original question:

        {business_description}

        Review the previous consultants' findings and prepare the FINAL answer.

        IMPORTANT RULES:
        - Follow the user's requested answer length.
        - If the user asks a simple question, give ONLY ONE short sentence.
        - If the user asks for suggestions, give a few relevant suggestions.
        - If the user asks for a detailed business plan, provide a detailed plan.
        - Do not repeat the previous consultants' reports.
        - Do not use unnecessary headings.
        - Be practical, clear, and friendly.
        - Answer the actual question directly.
        """,
        expected_output="The final answer in the exact level of detail requested by the user. Simple questions must receive only one short sentence.",
        agent=agent
    )
