from google.adk.agents import Agent
from google.adk.tools import AgentTool

from life_admin.config import make_gemini
from life_admin.sub_agents import task_manager_agent, planner_agent

interactive_life_admin_agent = Agent(
    name="interactive_life_admin_agent",
    model=make_gemini("gemini-2.5-flash"),
    description="Top-level Life Admin Coordinator that helps users manage tasks and simple daily planning.",
    instruction="""
You are the main Life Admin Coordinator Agent.

Your job:
- Be a friendly assistant that helps the user offload 'life admin' tasks.
- Delegate to sub-agents when needed.
""",
    tools=[
        AgentTool(task_manager_agent, "Use this to add, list, or complete tasks."),
        AgentTool(planner_agent, "Use this to create a daily plan from existing tasks."),
    ],
)

root_agent = interactive_life_admin_agent
