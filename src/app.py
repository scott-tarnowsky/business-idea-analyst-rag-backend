from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/chat", description="Chat with the RAG API through this endpoint")
def chat(message: str):
    return JSONResponse(content={"Your message": message}, status_code=200)
