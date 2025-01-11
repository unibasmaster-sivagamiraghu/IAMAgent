from crewai import Agent
from langchain.tools import Tool
from config.settings import TEMPERATURE

class RoleMapperAgent:
    @staticmethod
    def create(iam_tools):
        return Agent(
            role='Role Mapping Specialist',
            goal='Map IT roles to business applications and create business roles',
            backstory="""You are an expert in role mapping and business role creation.
            You understand how to align IT roles with business functions.""",
            tools=[
                Tool(
                    name="map_to_it_role",
                    func=iam_tools.map_to_it_role,
                    description="Map groups to IT roles"
                ),
                Tool(
                    name="create_business_role",
                    func=iam_tools.create_business_role,
                    description="Create business roles"
                )
            ],
            temperature=TEMPERATURE,
            verbose=True
        )