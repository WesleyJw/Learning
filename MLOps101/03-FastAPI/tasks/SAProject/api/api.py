import uvicorn
from fastapi import FastAPI, Header, HTTPException
from transformers import pipeline

from model import User, Text, Prediction
from database import db_connection, database_initialization
from app.sa_app import prediction
from authentication import user_auth, password_auth

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

@app.post("/create_user/", response_model=User)
def create_user(user: User, Authorization: str = Header(...)):
    """Create a new user to text sentiment analysis API.

    Args:
        name (str): User name. If name already exist in our database You can't create with this name.
        type (str): A user role. To a super user, the type is admin; to a user without privileges, the type is select.
        password (str): User password.
    """
    user_authenticated = user_auth(name=user.name)
    if Authorization.split(" ")[1] != f"{user_authenticated[3]}":
        raise HTTPException(status_code=401, detail="Access Denied")
    
    conn, cursor = db_connection()
    cursor.execute(
        "INSERT INTO users (name, type, password) VALUES (?, ?, ?)", (user.name, user.type, user.password)
    )
    conn.commit()
    return user

# Run app
if __name__ == "__main__":
    database_initialization()
    uvicorn.run(app, host="0.0.0.0", port=8000)