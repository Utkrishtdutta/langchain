import uvicorn
from fastapi import FastAPI
from langserve import add_routes
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate

app = FastAPI(
    title='Langchain Server',
    version= 1.0,
    description= 'A simple api to connect LLMs'
)
llm = Ollama(model = "llama2")

prompt = ChatPromptTemplate.from_template('Write a essay about {topic} with 100 words')

add_routes(
    app,
    prompt|llm,
    path ='/essay'
)

if __name__ == '__main__':
    uvicorn.run(app,host='localhost',port='8080')
    