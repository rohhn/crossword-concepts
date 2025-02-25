import marimo

__generated_with = "0.10.17"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from dotenv import load_dotenv
    load_dotenv("./.env")
    from utils.FileReader import base_reader
    from models import Model
    from workflows import chain
    from langgraph.graph import MessagesState
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI
    import json
    return (
        ChatOpenAI,
        HumanMessage,
        MessagesState,
        Model,
        base_reader,
        chain,
        json,
        load_dotenv,
        mo,
    )


@app.cell
def _(chain, mo):
    mo.mermaid((workflow:=chain()).get_graph().draw_mermaid())
    return (workflow,)


@app.cell
def _(HumanMessage, workflow):
    resp = workflow.invoke({
        "messages": [ HumanMessage(content="puzzle for attention is all you need paper")]
    })
    return (resp,)


@app.cell
def _(resp):
    resp
    return


@app.cell
def _(json, resp):
    sol = json.loads(resp["messages"][-1].content)
    sol["solution"].splitlines()
    return (sol,)


@app.cell
def _(sol):
    sol["legend"]
    return


@app.cell
def _(sol):
    sol["word_find"]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
