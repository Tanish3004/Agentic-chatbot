import streamlit as st
from src.langgraph_agentic_ai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_agentic_ai.llms.groqllm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder
from src.langgraph_agentic_ai.ui.streamlitui.display_result import DisplayResultStreamlit

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

    if user_message:
        try: 
            ## Configure The llm's
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: llm model could not be initialized ")
                return

            usecase=user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: no use case selected")
                return

            ## Graph Builder 

            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed - {e}")
                return

        except Exception as e:  
            st.error(f"Error: Graph set up failed - {e}")
            return