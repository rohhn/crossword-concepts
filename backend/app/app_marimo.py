import marimo

__generated_with = "0.10.17"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from dotenv import load_dotenv
    load_dotenv("./.env")
    from langgraph.graph import MessagesState
    from langchain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langchain.evaluation import load_evaluator, EmbeddingDistance
    from langchain_community.embeddings import HuggingFaceEmbeddings
    import json
    evaluator = load_evaluator(
        "embedding_distance", distance_metric=EmbeddingDistance.COSINE
    )

    embedding_model = HuggingFaceEmbeddings(model_name="TaylorAI/gte-tiny")
    hf_evaluator = load_evaluator("embedding_distance", embeddings=embedding_model)
    return (
        ChatOpenAI,
        EmbeddingDistance,
        HuggingFaceEmbeddings,
        HumanMessage,
        MessagesState,
        OpenAIEmbeddings,
        embedding_model,
        evaluator,
        hf_evaluator,
        json,
        load_dotenv,
        load_evaluator,
        mo,
    )


@app.cell
def _():
    li = ['dog', 'kitten', 'traffic', 'cow', 'animal', 'pet', 'tyson', 'game', 'china']
    return (li,)


@app.cell
def _(evaluator, hf_evaluator, li):
    for el in li:
        resp = evaluator.evaluate_strings(prediction=el, reference="cat")['score']
        resp2 = hf_evaluator.evaluate_strings(prediction=el, reference="cat")['score']
        print(f"{el}: {resp}, {resp2}, {(resp + resp2) / 2}")
    return el, resp, resp2


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
