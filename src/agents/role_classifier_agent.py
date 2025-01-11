from crewai import Agent
from langchain.tools import Tool
from config.settings import TEMPERATURE

class RoleClassifierAgent:
    @staticmethod
    def create(iam_tools):
        return Agent(
            role='Role Classification Specialist',
            goal='Accurately classify AD groups into IT roles',
            backstory="""You are an expert in role engineering and AD group classification.
            Your expertise helps organizations maintain clean and efficient role structures.""",
            tools=[
                Tool(
                    name="classify_ad_group",
                    func=iam_tools.classify_ad_group,
                    description="Classify AD groups based on patterns"
                )
            ],
            temperature=TEMPERATURE,
            verbose=True
        )