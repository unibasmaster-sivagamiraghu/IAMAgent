from crewai import Task

class IAMTasks:
    @staticmethod
    def get_classification_task(agent):
        return Task(
            description="""Analyze and classify AD groups based on naming conventions,
            usage patterns, and group memberships""",
            agent=agent
        )

    @staticmethod
    def get_mapping_task(agent):
        return Task(
            description="""Map classified groups to IT roles and create appropriate
            business roles based on the mapping""",
            agent=agent
        )
