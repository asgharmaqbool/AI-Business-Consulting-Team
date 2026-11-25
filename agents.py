
from crewai import Agent
from llm_config import get_llm


def create_business_analyst():
    return Agent(
        role="Senior Business Analyst",
        goal="Analyze the user's business, identify problems, and discover opportunities for growth.",
        backstory=(
            "You are an experienced business analyst. "
            "You analyze business models, customers, markets, operations, "
            "and business challenges to provide practical insights."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )


def create_market_researcher():
    return Agent(
        role="Market Research Specialist",
        goal="Research market trends, target customers, competitors, and industry opportunities.",
        backstory=(
            "You are a professional market research specialist. "
            "You evaluate target markets, customer demand, industry trends, "
            "competitors, and opportunities using logical research methods."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )


def create_marketing_strategist():
    return Agent(
        role="Marketing Strategist",
        goal="Develop marketing strategies to attract customers and increase brand awareness.",
        backstory=(
            "You are an expert marketing strategist specializing in branding, "
            "customer acquisition, social media, advertising, and marketing campaigns."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )


def create_financial_advisor():
    return Agent(
        role="Financial Business Advisor",
        goal="Analyze business finances, costs, revenue opportunities, and profitability.",
        backstory=(
            "You are an experienced business financial advisor. "
            "You help businesses understand costs, revenue, pricing, "
            "profitability, budgeting, and financial risks."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )


def create_business_growth_consultant():
    return Agent(
        role="Business Growth Consultant",
        goal="Create practical strategies for business growth, scaling, and long-term success.",
        backstory=(
            "You are a business growth consultant who specializes in "
            "business expansion, customer retention, operational improvement, "
            "scaling strategies, and long-term business development."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )
