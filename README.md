Life Admin Agent

A lightweight multi-agent system built using Google ADK to help users manage everyday “life admin” tasks — such as chores, errands, reminders, and simple daily planning.

This project demonstrates:

Multi-agent delegation

Tool usage (FunctionTools)

Simple stateful task storage (in-memory DB)

Natural-language routing

A functional ADK app you can run locally

⭐ Features
🗂️ Task Manager Agent

Handles all task-related actions:

Add a new task

List open / completed tasks

Mark a task as done

Tools used:

add_task

list_tasks

complete_task

🧭 Planner Agent

Creates a simple daily plan using open tasks.

Orders tasks by due date

Produces a friendly day plan

Uses the generate_daily_plan tool

🤝 Interactive Coordinator Agent (Root Agent)

The top-level agent that:

Interprets user intent

Routes requests to the correct sub-agent

Responds in friendly natural language

This is the root agent for the ADK app.

📂 Project Structure
life_admin_agent/
│
├── app.py
├── README.md
├── .gitignore
│
├── life_admin/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── tools.py
│   ├── agent_utils.py
│   └── sub_agents/
│       ├── __init__.py
│       ├── planner.py
│       └── task_manager.py
│
└── tests/
    ├── __init__.py
    └── test_agent.py

🚀 How to Run the App Locally
1. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

2. Install dependencies
pip install -r requirements.txt

3. Add your API key

Create a .env file in the project root:

GOOGLE_API_KEY=your_key_here
GOOGLE_GENAI_USE_VERTEXAI=False

4. Start the ADK web interface
adk web .

5. Open in your browser
http://127.0.0.1:8000


You can now chat with your Life Admin Agent.

🧪 Running Tests
python -m tests.test_agent
