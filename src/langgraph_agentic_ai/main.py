import streamlit as st
from src.langgraph_agentic_ai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    """
    loads and runs the langgraph AgenticAI application with streamlit UI
    This Function initializes the UI ,handles user input,configures the llm models,
    sets up the graph based on the selected use case ,and displays the output while 
    implementing exception handling and robustness.

    """
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the ui.")
        return 

    user_message = st.chat_input("Enter your message:")
   