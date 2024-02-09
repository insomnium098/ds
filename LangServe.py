#!/usr/bin/env python

#!pip install langserve sse_starlette
#http://localhost:8000/chiste/playground/
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatAnthropic, ChatOpenAI
from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

OPENAI_API_KEY = ""

add_routes(
    app,
    ChatOpenAI(openai_api_key=OPENAI_API_KEY),
    path="/openai",
)

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
prompt = ChatPromptTemplate.from_template("Dime un chiste sobre {tema}")
add_routes(
    app,
    prompt | model,
    path="/chiste",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)