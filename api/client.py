import requests
import streamlit as st

def ollama_response(input_text):
    response = requests.post(url='http://localhost:8080/essay/invoke',
    json = {'input':{'topic':input_text}})

    return response.json()['output']


st.title('Langserve API')
text_input = st.text_input('write the subject of story')

if text_input:
    st.write(ollama_response(text_input))
