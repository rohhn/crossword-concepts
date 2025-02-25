import marimo

__generated_with = "0.10.17"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import logging
    from app.workflows import chain
    from dotenv import load_dotenv
    from langchain.evaluation import load_evaluator, EmbeddingDistance
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings

    logging.basicConfig(level=logging.INFO)
    load_dotenv("./app/.env")

    logging.info("env file loaded")
    return (
        ChatOpenAI,
        EmbeddingDistance,
        OpenAIEmbeddings,
        chain,
        load_dotenv,
        load_evaluator,
        logging,
        mo,
    )


@app.cell
def _(ChatOpenAI):
    llm = ChatOpenAI()
    llm.invoke("""
    create a wordle game from the attention is all you need paper. Return a LIST of LISTS only.
    """)
    return (llm,)


@app.cell
def _(EmbeddingDistance, load_evaluator):
    evaluator = load_evaluator("embedding_distance", distance_metric=EmbeddingDistance.COSINE)
    store = {}
    return evaluator, store


@app.cell
def _(mo):
    input = mo.ui.text().form()
    input
    return (input,)


@app.cell
def _(evaluator, input, store):

    import plotly.express as px

    score = evaluator.evaluate_strings(prediction=input.value, reference="cat")
    store[input.value] = 1- score["score"]
    sorted_items = sorted(store.items(), key=lambda item: item[1])
    keys = [k for k, v in sorted_items]
    values = [v for k, v in sorted_items]

    # Create a line plot with markers
    fig = px.line(x=keys, y=values, markers=True, title="Data Sorted by Value")
    fig.update_layout(xaxis_title="Key", yaxis_title="Value")

    fig.show()
    return fig, keys, px, score, sorted_items, values


@app.cell
def _(sorted_items):
    li = [y for _, y in sorted_items]
    import numpy as np
    li = np.array(li)
    return li, np


@app.cell
def _(li, np):
    min_el, max_el = np.min(li), np.max(li)
    (li - 100) / (100 - 0) * 100
    return max_el, min_el


@app.cell
def _(li, np):
    li.astype(np.uint8)
    return


@app.cell
def _(li):
    li
    return


@app.cell
def _():
    return


@app.cell
def _(ChatOpen):
    llm = ChatOpen
    return (llm,)


if __name__ == "__main__":
    app.run()
