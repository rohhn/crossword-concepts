from langchain_core.messages import HumanMessage
from langgraph.graph import END, START, MessagesState, StateGraph
from ..utils import Crossword
from ..models import Model
import json
import re

"""
web ui format
[
    {
        "clue": "Black-and-white cookie",
        "answer": "OREO",
        "direction": "down",
        "x": 0,
        "y": 0
    }
]
"""

def llm_node(state: MessagesState, config={}):
    llm = Model()
    resp = llm.invoke(state, config=config)
    return resp

def build_crossword(state: MessagesState):
    last_msg = state["messages"][-1].content
    json_data = json.loads(last_msg) # pyright: ignore
    json_data["answers"] = map(lambda x: re.sub(r"[-()\[\]{}\.]", "", x), json_data["answers"])
    pairs = zip(json_data["answers"], json_data["questions"])
    crossword = Crossword(20, 20, '.', 1_000, pairs)
    crossword.compute_crossword(2)
    crossword.legend()

    data = {
        'solution': crossword.solution(),
        'legend': json.loads(crossword.legend()),
        'word_find': crossword.word_find(),
    }
    data = json.dumps(data, indent=2)

    return {
            "messages": HumanMessage(content=data)
    }

def chain():
    graph = StateGraph(MessagesState)
    graph.add_node("LLM", llm_node)
    graph.add_node("BUIDL", build_crossword)
    graph.add_edge(START, "LLM")
    graph.add_edge("LLM", "BUIDL")
    graph.add_edge("BUIDL", END)
    flow = graph.compile()
    return flow
