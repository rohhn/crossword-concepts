import json
from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from fastapi.middleware.cors import CORSMiddleware

from .utils import base_reader, SimilarityJSON
from .workflows import chain
from .models import context_llm, evaluator
load_dotenv(dotenv_path="./.env")
import os

# INFO: global vars
similarity_embeddings = evaluator(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

# INFO: server-end functions
app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return { "hello": "world" }

@app.post("/puzzle")
async def create_crossword(query: str):
    resp = chain().invoke({
        "messages": HumanMessage(content=query)
    })
    resp = resp["messages"][-1].content
    resp = json.loads(resp)
    return resp

@app.post("/upload")
async def upload_file(file: UploadFile):
    bytes = await file.read()
    doc = list(base_reader(bytes))
    resp = chain().invoke({
        "messages": HumanMessage(content=f"make game from this\n{str(doc)}")
    })["messages"][-1].content
    resp = json.loads(resp)
    return {"file": file.filename, "game": resp }


@app.post("/guess")
async def create_guess_game(file: UploadFile):
    bytes = await file.read()
    doc = list(base_reader(bytes))
    resp = context_llm(str(doc))
    return resp

@app.post("/play")
async def all_games(file: UploadFile):
    bytes = await file.read()
    doc = list(base_reader(bytes))
    doc = [d.page_content for d in doc]
    doc = '\n'.join(doc)
    resp = chain().invoke({
        "messages": HumanMessage(content=f"make game from this\n{doc}")
    })["messages"][-1].content
    resp = json.loads(resp)
    resp2 = context_llm(doc)
    return {"file": file.filename, "game": resp, "guess_game": resp2 }



@app.post("/similarity")
def check_similarity(req: SimilarityJSON):
    # resp = evaluate_model(target=target, prediction=prediction)
    resp = similarity_embeddings.evaluate_strings(reference=req.target, prediction=req.prediction) # pyright: ignore
    resp['score'] *= 100
    resp['score'] = "{:.2f}".format(resp["score"])
    resp['score'] = float(resp["score"])
    return resp

# TODO:
# Storage & Auth
# GET puzzle/id
# DEL puzzle/id
