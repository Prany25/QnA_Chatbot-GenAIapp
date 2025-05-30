import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="QnA Chatbot with Ollama"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system":"You are a helpful assistant. Respond to the queries with what you know"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=llm)
    output_parser=StrOutputParser()
    chain= prompt|llm|output_parser
    answer=chain.invoke({'question':question)
    return answer


