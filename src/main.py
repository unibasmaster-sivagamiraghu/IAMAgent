from crewai import Crew
from tools.iam_tools import IAMTools
from agents.role_classifier_agent import RoleClassifierAgent
from agents.role_mapper_agent import RoleMapperAgent
from tasks.iam_tasks import IAMTasks

def main():
    # Initialize tools
    iam_tools = IAMTools()

    # Create agents
    role_classifier = RoleClassifierAgent.create(iam_tools)
    role_mapper = RoleMapperAgent.create(iam_tools)

    # Create tasks
    classification_task = IAMTasks.get_classification_task(role_classifier)
    mapping_task = IAMTasks.get_mapping_task(role_mapper)

    # Create and run the crew
    iam_crew = Crew(
        agents=[role_classifier, role_mapper],
        tasks=[classification_task, mapping_task],
        verbose=2
    )

    # Execute the crew
    result = iam_crew.kickoff()
    return result

if __name__ == "__main__":
    main()