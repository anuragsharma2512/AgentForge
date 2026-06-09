from src.langgraphagenticai.state import State


class BasicChatbotNode:
    """
    A basic chatbot node that generates responses based on user input.
    """
    def __init__(self, model):
        self.llm = model
    
    def process(self, state:State)->dict:
        """
        Process the user input and generate a response using the LLM.
        """
        return {"message":self.llm.invoke(state['messages'])}