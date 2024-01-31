import uvicorn
from fastapi import FastAPI, Header, HTTPException
from transformers import pipeline

from model import User, Text, Prediction
from database import connection, database_initialization

# Create FastAPI app
app = FastAPI(
    # Configure the docs and redoc URLs - to redirect /docs swagger to you home page
    docs_url="/",
    redoc_url=None,
)

@app.get("/")
def home():
    "Welcome to Text Sentiment Analysis API."
    return {"message": "Welcome to Text Sentiment Analysis API."}

# Run app
if __name__ == "__main__":
    database_initialization()
    uvicorn.run(app, host="0.0.0.0", port=8000)