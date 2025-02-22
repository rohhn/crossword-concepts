import marimo

__generated_with = "0.10.17"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langgraph.graph import StateGraph, MessagesState, START, END
    from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, AnyMessage, RemoveMessage
    from langgraph.checkpoint.sqlite import SqliteSaver
    from langchain_core.vectorstores import InMemoryVectorStore
    from langchain.docstore.document import Document

    import sqlite3
    import polars as pl

    from io import BytesIO
    from PyPDF2 import PdfReader
    import logging
    from dotenv import load_dotenv

    logging.basicConfig(level=logging.INFO)
    load_dotenv("./.env")
    llm = ChatOpenAI()

    logging.info("env file loaded")
    return (
        AIMessage,
        AnyMessage,
        BytesIO,
        ChatOpenAI,
        Document,
        END,
        HumanMessage,
        InMemoryVectorStore,
        MessagesState,
        OpenAIEmbeddings,
        PdfReader,
        RemoveMessage,
        START,
        SqliteSaver,
        StateGraph,
        SystemMessage,
        llm,
        load_dotenv,
        logging,
        mo,
        pl,
        sqlite3,
    )


@app.cell
def _(llm):
    from typing import Optional

    from pydantic import BaseModel, Field


    # Pydantic
    class Joke(BaseModel):
        """Joke to tell user."""

        setup: str = Field(description="The setup of the joke")
        punchline: str = Field(description="The punchline to the joke")
        rating: Optional[int] = Field(
            default=None, description="How funny the joke is, from 1 to 10"
        )


    structured_llm = llm.with_structured_output(Joke)

    structured_llm.invoke("Tell me a joke about cats")
    return BaseModel, Field, Joke, Optional, structured_llm


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
