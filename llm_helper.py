from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

from pydantic.v1.schema import model_type_schema

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name = "llama3-8b-8192")

if __name__ == "__main__" :
    response = llm.invoke("what is main ingridients in samosa ")
    print(response.content)
