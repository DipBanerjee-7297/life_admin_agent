# life_admin/agent.py

from google.adk.agents import Agent, RoutingAgent
from google.adk.tools import PassthroughTool

from life_admin.config import make_gemini
from life_admin.sub_agents.task_manager import task_manager_agent
from life_admin.sub_agents.planner import planner_agent


# 1) A passthrough tool so the orchestrator can speak normally
echo_tool = PassthroughTool(name="echo", description="Return a natural language response.")

# 2) Main Routing Agent
interactive_life_admin_agent = RoutingAgent(
    name="interactive_life_admin_agent",
    description="Top-level coordinator for life admin tasks.",
    model=make_gemini("gemini-2.5-flash"),

    # Orchestrator instructions
    instruction="""
You are the main Life Admin Agent.

Your job:
- Understand what the user wants.
- Route the request to the correct sub-agent:
    * task_manager_agent → for adding, listing, completing tasks
    * planner_agent → for creating a daily plan
- If the user is greeting or making small talk, respond normally using the echo tool.

Routing Logic Examples:
- "add", "create", "new task", "remind me to" → task_manager_agent
- "list tasks", "show tasks", "pending", "open tasks" → task_manager_agent
- "mark done", "finish task", "complete task" → task_manager_agent
- "plan my day", "give me a schedule", "daily plan" → planner_agent
- Greetings like "hello", "thanks", "who are you?" → respond normally with echo tool.

After sub-agent calls:
- Return the sub-agent's friendly final message directly to the user.
""",
    agents=[
        task_manager_agent,
        planner_agent,
    ],
    tools=[echo_tool],
)
