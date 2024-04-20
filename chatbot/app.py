import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


st.title('An chatbot through Langchain and llama-2')

llm = Ollama(model='llama2')

prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are an assistent. Please help the student in writing essay.'),
        ('user','Question:{questions}')
    ]
)

input_text = st.text_input("Topic of essay")
output_panser = StrOutputParser()
chain = prompt|llm|output_panser

if input_text:
    chain.invoke({'questions':input_text})
