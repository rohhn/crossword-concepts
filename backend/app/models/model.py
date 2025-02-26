from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import MessagesState
from ..utils import RespSchema, WordGuessSchema
import json
from langchain.evaluation import load_evaluator
from langchain_community.embeddings import HuggingFaceEmbeddings

class Model():
    def __init__(self, model="gpt-4o-mini-2024-07-18", prompt=None, tools=[]):
        self.llm = ChatOpenAI(model=model).with_structured_output(RespSchema)
        if tools:
            self.llm = self.llm.bind(tools=tools)
        self.system_msg = """
        You create crossword puzzle games to assist the user understand the concepts to a
        research topic. Study the topic in reference properly and create 15-30 questions
        and their corresponding one or two worded answers that would be fit for a crossword game.

        *DOs*
        + get question answer pairs that have answers with lots of common letters at differnt places (for making denser crosswords)

        *DONTs*
        + do not prepend question number to the returned questions.
        """
        if prompt:
            self.system_msg = prompt


    def invoke(self, state: MessagesState, config={}):
        messages = [
            SystemMessage(content=self.system_msg)
        ] + state['messages']
        resp = self.llm.invoke(messages, config)
        # INFO: ignore linting error `model_dump_json()`
        return {
            "messages": HumanMessage(content=resp.model_dump_json()) # pyright: ignore
        }


def context_llm(msg: str):
    prompt = """
    You are to develop conceptually challenging questions based on the document provided.
    The answers to guess should be guessable and one worded.
    A writable answer shoudlnt have hyphens, brackets, superscripts or subscripts.
    *the writable answer shouldn' t shouldn't be numbers or numbers written as words.*
    Give atleast 15 questions.
    """
    llm = ChatOpenAI(model='gpt-4o-mini-2024-07-18').with_structured_output(WordGuessSchema)
    resp = llm.invoke(prompt + msg).model_dump_json() # pyright: ignore
    return json.loads(resp)

def evaluator():
    embedding_model = HuggingFaceEmbeddings(model_name="TaylorAI/gte-tiny")
    hf_evaluator = load_evaluator("embedding_distance", embeddings=embedding_model) #pyright: ignore
    return hf_evaluator
