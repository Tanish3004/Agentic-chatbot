from langgraph.graph import StateGraph
from src.langgraph_agentic_ai.state.state import State
from langgraph.graph import START,END
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):

        """
        this method initializes the chatbot node using the
        'basicChatbotNode' class and integrates it into  the graph .
        the chatbot node is set as both the entry and exit point of
          the graph
        """   
        self.basic_chatbot_node=BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usecase:str):
        """
        sets up the graph for the selcted use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        return self.graph_builder.compile()