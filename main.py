# agentic_rag_chatbot/main.py

from mcp.coordinator import CoordinatorAgent
from ui.app import launch_ui

if __name__ == '__main__':
    coordinator = CoordinatorAgent()
    launch_ui(coordinator)
