import uvicorn
from fastapi import FastAPI, Header, HTTPException

from model import User, Text, Prediction
from database import db_connection, database_initialization
from app.sa_app import prediction
from authentication import user_auth, password_auth
from api_tools import user_creation

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
    user_authenticated = user_auth(password=Authorization.split(" ")[1])
    if Authorization != f"Bearer {user_authenticated[3]}":
        raise HTTPException(status_code=401, detail="Access Denied")
    if user_authenticated[2] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden. You don't have permission to create users.")
    token = user_creation(user)
    return {"name": user.name, "type": f"{user.type}. Please, copy the user token: {token.get('password')}"}

# Run app
if __name__ == "__main__":
    database_initialization()
    uvicorn.run(app, host="0.0.0.0", port=8000)