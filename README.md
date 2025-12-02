# Life Admin Agent

A lightweight multi-agent system built using **Google ADK** to help users manage everyday “life admin” tasks — such as chores, errands, reminders, and simple daily planning.

This project demonstrates:

- Multi-agent delegation  
- Tool usage (FunctionTools)  
- Simple stateful task storage (in-memory DB)  
- Natural-language routing  
- A functional ADK app you can run locally

---

## Features

### 🗂️ **Task Manager Agent**
Handles all task-related actions:

- Add a new task  
- List open / completed tasks  
- Mark a task as done  

Tools used:
- `add_task`
- `list_tasks`
- `complete_task`

---

### 🧭 **Planner Agent**
Creates a simple daily plan using open tasks.

- Orders tasks by due date  
- Produces a friendly daily plan message  
- Uses the `generate_daily_plan` tool

---

### 🤝 **Interactive Coordinator Agent (Root Agent)**
This is the main agent the user interacts with.

It:
- Understands user intent  
- Routes requests to the correct sub-agent  
- Returns friendly, natural-language responses  

This agent is the **root agent** for the ADK app.

---

## 📂 Project Structure

```plaintext
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
```


