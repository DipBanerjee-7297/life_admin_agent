# tests/test_agent.py
"""
Very small smoke test so the capstone has an automated check.

Run with:
    python -m tests.test_agent
"""

from life_admin.agent import interactive_life_admin_agent


def test_can_import_and_has_name():
    assert interactive_life_admin_agent.name == "interactive_life_admin_agent"
