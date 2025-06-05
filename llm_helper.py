import streamlit as st
from langchain_groq import ChatGroq
import os

from pydantic.v1.schema import model_type_schema

api_key = st.secrets["OPENAI_API_KEY"]

llm = ChatGroq(groq_api_key=api_key, model_name = "llama-3.3-70b-versatile")

if __name__ == "__main__" :
    response = llm.invoke("what is main ingridients in samosa ")
    # print(response.content)
