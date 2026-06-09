from typing_extensions import TypedDict,List
from langgraph.graph.message import add_message
from typing import Annotated


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """

    messages: Annotated[List,add_message]