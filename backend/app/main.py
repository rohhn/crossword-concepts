import json
from fastapi import FastAPI, UploadFile, Depends
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from fastapi.middleware.cors import CORSMiddleware

from .utils import base_reader
from .workflows import chain
load_dotenv(dotenv_path="./.env")

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


# TODO: deal with auth handling
def dummy():
    return True

@app.get("/")
def read_root():
    return { "hello": "world" }

@app.post("/upload")
async def upload_file(file: UploadFile, auth=Depends(dummy)):
    bytes = await file.read()
    doc = list(base_reader(bytes))
    print(doc[:2])
    return {"file": file.filename }

@app.post("/puzzle")
async def create_crossword(query: str):
    resp = chain().invoke({
        "messages": HumanMessage(content=query)
    })
    resp = resp["messages"][-1].content
    resp = json.loads(resp)
    return resp

# TODO:
# Storage & Auth
# GET puzzle/id
# DEL puzzle/id
