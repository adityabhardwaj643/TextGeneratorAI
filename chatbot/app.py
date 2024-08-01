from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import gradio as gr
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="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"

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "{question}")
    ]
)

# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

def generate_response(text):
    return chain.invoke({"question": text})

iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text"
)

iface.launch()
