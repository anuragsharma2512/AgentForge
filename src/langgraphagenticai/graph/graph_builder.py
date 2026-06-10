from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_model import BasicChatbotNode



class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder= StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph with the following structure:"""


        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def setup_graph(self,usecase):
        """
        Set up the graph based on the selected use case.
        """
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
            
        return self.graph_builder.compile()
        
