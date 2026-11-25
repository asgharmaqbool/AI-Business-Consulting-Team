
from crewai import Crew, Process

from agents import (
    create_business_analyst,
    create_market_researcher,
    create_marketing_strategist,
    create_financial_advisor,
    create_business_growth_consultant
)

from tasks import (
    create_business_analysis_task,
    create_market_research_task,
    create_marketing_strategy_task,
    create_financial_analysis_task,
    create_growth_strategy_task
)


def create_consulting_crew(business_description):

    # ------------------------------------------
    # CREATE THE FIVE SPECIALIST AGENTS
    # ------------------------------------------

    business_analyst = create_business_analyst()
    market_researcher = create_market_researcher()
    marketing_strategist = create_marketing_strategist()
    financial_advisor = create_financial_advisor()
    growth_consultant = create_business_growth_consultant()

    # ------------------------------------------
    # CREATE THE FIVE SPECIALIST TASKS
    # ------------------------------------------

    business_analysis_task = create_business_analysis_task(
        business_analyst,
        business_description
    )

    market_research_task = create_market_research_task(
        market_researcher,
        business_description
    )

    marketing_task = create_marketing_strategy_task(
        marketing_strategist,
        business_description
    )

    financial_task = create_financial_analysis_task(
        financial_advisor,
        business_description
    )

    growth_task = create_growth_strategy_task(
        growth_consultant,
        business_description
    )

    # ------------------------------------------
    # CONNECT TASK CONTEXT
    # ------------------------------------------

    # Market research uses the business analysis
    market_research_task.context = [
        business_analysis_task
    ]

    # Marketing uses business analysis and market research
    marketing_task.context = [
        business_analysis_task,
        market_research_task
    ]

    # Financial analysis uses the business analysis
    financial_task.context = [
        business_analysis_task
    ]

    # Growth consultant receives all previous findings
    growth_task.context = [
        business_analysis_task,
        market_research_task,
        marketing_task,
        financial_task
    ]

    # ------------------------------------------
    # ASSEMBLE THE CONSULTING TEAM
    # ------------------------------------------

    consulting_crew = Crew(
        agents=[
            business_analyst,
            market_researcher,
            marketing_strategist,
            financial_advisor,
            growth_consultant
        ],
        tasks=[
            business_analysis_task,
            market_research_task,
            marketing_task,
            financial_task,
            growth_task
        ],
        process=Process.sequential,
        verbose=True
    )

    return consulting_crew
