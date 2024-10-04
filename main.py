import nest_asyncio
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

nest_asyncio.apply()
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_models import ChatOllama


app = FastAPI(
    title="Chatbot API",
    version="1.0",
    description="Chatbot API"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse('index.html')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
prompt = ChatPromptTemplate.from_template("Generate the answer to the {question} asked only in the following {language}")
add_routes(
    app,
    prompt|Ollama(model="mistral"),
    path="/chatbot"
)
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)