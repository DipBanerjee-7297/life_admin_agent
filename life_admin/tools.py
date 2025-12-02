# life_admin/tools.py

from __future__ import annotations

import datetime
from typing import List, Dict, Any

# Very simple in-memory "DB"
# Each task: { "id": int, "description": str, "due": "YYYY-MM-DD" | None,
#              "status": "open" | "done", "created_at": iso-string }
_TASKS: List[Dict[str, Any]] = []
_NEXT_ID = 1


def _next_id() -> int:
    global _NEXT_ID
    nid = _NEXT_ID
    _NEXT_ID += 1
    return nid


def add_task(description: str, due: str | None = None) -> Dict[str, Any]:
    """
    Add a new task to the in-memory list.

    Args:
        description: what the user needs to do
        due: optional due date as 'YYYY-MM-DD'

    Returns:
        dict with the created task and display text.
    """
    task = {
        "id": _next_id(),
        "description": description.strip(),
        "due": due,
        "status": "open",
        "created_at": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    _TASKS.append(task)
    
    # --- ADDED: Friendly confirmation text ---
    due_str = f" (due {task['due']})" if task['due'] else ""
    display_text = f"Task '{task['description']}' has been added with ID [{task['id']}] {due_str}."
    # ----------------------------------------
    
    return {
        "task": task,
        "display_text": display_text
    }


def list_tasks(status: str | None = None) -> Dict[str, Any]:
    """
    List tasks, optionally filtered by status ('open' or 'done').
    
    Returns:
        dict with task list and display text.
    """
    if status is None:
        tasks = list(_TASKS)
    else:
        status = status.lower()
        tasks = [t for t in _TASKS if t["status"].lower() == status]

    # Sort: open first, then by due date
    def sort_key(t):
        return (t["status"] != "open", t["due"] or "9999-12-31")

    tasks_sorted = sorted(tasks, key=sort_key)
    
    # --- ADDED: Generate a friendly display string ---
    display_list = []
    if tasks_sorted:
        display_list.append("Here is your current task list:")
        for t in tasks_sorted:
            due_str = f" (due {t['due']})" if t['due'] else ""
            status_str = f" - {t['status'].upper()}" if t['status'] != 'open' else ""
            # Format: [ID] Description (due YYYY-MM-DD) - STATUS
            display_list.append(f"• [{t['id']}] {t['description']}{due_str}{status_str}")
        
        display_text = "\n".join(display_list)
    else:
        display_text = f"You currently have no {status or 'open'} tasks. Time to relax, or maybe add a new task!"
    # ---------------------------------------------------
    
    return {
        "tasks": tasks_sorted,
        "display_text": display_text
    }


def complete_task(task_id: int) -> Dict[str, Any]:
    """
    Mark a task as done.
    
    Returns:
        dict with success status and display text.
    """
    for t in _TASKS:
        if t["id"] == task_id:
            t["status"] = "done"
            
            # --- ADDED: Friendly confirmation text ---
            return {
                "success": True, 
                "task": t, 
                "display_text": f"Task [{t['id']}] '{t['description']}' has been marked as done! 🎉"
            }
            # -------------------------------------------
            
    # --- ADDED: Friendly error text ---
    return {
        "success": False, 
        "error": f"No task found with id={task_id}",
        "display_text": f"Sorry, I couldn't find a task with ID {task_id} to mark as done."
    }
    # ----------------------------------


def generate_daily_plan(date: str | None = None) -> Dict[str, Any]:
    """
    Very simple planner: takes open tasks and suggests an ordered plan.

    Args:
        date: ISO date string (YYYY-MM-DD). If None, use today.

    Returns:
        dict with plan items and display text.
    """
    if date is None:
        date = datetime.date.today().isoformat()

    open_tasks = [t for t in _TASKS if t["status"] == "open"]

    # Prioritize by due date (closest first)
    def sort_key(t):
        return (t["due"] or "9999-12-31", t["created_at"])

    open_sorted = sorted(open_tasks, key=sort_key)

    plan_items = []
    for idx, t in enumerate(open_sorted, start=1):
        label = f"Step {idx}: {t['description']}"
        if t["due"]:
            label += f" (due {t['due']})"
        plan_items.append(label)

    # --- ADDED: Format the final plan string ---
    if plan_items:
        plan_text = f"Here is your focus plan for {date}:\n\n" + "\n".join(plan_items)
    else:
        plan_text = f"It looks like you have no open tasks scheduled for {date}! Take a well-deserved rest, or ask me to add a new task."
    # ---------------------------------------------

    return {
        "date": date,
        "plan": plan_items,
        "tasks_considered": [t["id"] for t in open_sorted],
        "display_text": plan_text
    }
