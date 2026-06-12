from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_model import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tool, create_tool_node
from langgraph.prebuilt import ToolNode
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode




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


    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.

        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilities, and sets up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.
        """

        ## defining tool and tool node
        tools=get_tool()
        tool_node=create_tool_node(tools)

        ## define the llm
        llm = self.llm

        ## define the chatbot node
        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
        def tool_condition(state):
            """
            Route to tools if the last AI message contains tool calls,
            otherwise end the graph.
            """

            messages = state["messages"]
            last_message = messages[-1]

            if hasattr(last_message, "tool_calls") and last_message.tool_calls:
                return "tools"

            return END
        ## Add nodes

        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        ## define conditional and direct edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tool_condition)
        self.graph_builder.add_edge("tools","chatbot")





    def setup_graph(self,usecase):
        """
        Set up the graph based on the selected use case.
        """
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase=="Chatbot with web":
            self.chatbot_with_tools_build_graph()
            
        return self.graph_builder.compile()
        
