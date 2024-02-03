import uvicorn
from fastapi import FastAPI, Header, HTTPException
from typing import List
from fastapi import FastAPI, Depends, HTTPException, Header, Request

from model import User, UserList, Text, Prediction
from database import db_connection, database_initialization
from app.sa_app import prediction
from authentication import user_auth
from api_tools import user_creation, get_user, history_insert

# Function to get the token from the Authorization header
def get_token(request: Request):
    try:
        authorization = request.headers.get("Authorization")
        # Extract the token from the Authorization header
        token_prefix, token = authorization.split()
        if token_prefix.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid User or token type. Must use Bearer token.")
        return token
    except:
        raise HTTPException(status_code=401, detail="Invalid Authorization header format.")

def authenticated_user(token):

    user_token = user_auth(password=str(token))
    if user_token is None:
        raise HTTPException(status_code=401, detail="Invalid user.")
    if str(token) != user_token[3]:
        raise HTTPException(status_code=401, detail="Access Denied")
    if user_token[2] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden. You don't have admin permission to manage users.")

def authenticated_user_predict(token):
    
    user_token = user_auth(password=str(token))
    if user_token is None:
        raise HTTPException(status_code=401, detail="Invalid user.")
    if str(token) != user_token[3]:
        raise HTTPException(status_code=401, detail="Access Denied")

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
        raise HTTPException(status_code=403, detail="Forbidden. You don't have admin permission to manage users.")
    token = user_creation(user)
    return {"name": user.name, "type": f"{user.type}. Please, copy the user token: {token.get('password')}"}

@app.get("/list_users", response_model=List[UserList])
async def list_users_route(token: str = Depends(get_token)):
    """List all users in database. You must have a admin authentication type.
    """
    authenticated_user(token)
    conn, cursor = db_connection()
    cursor.execute(
        "SELECT * FROM users;"
    )
    users = cursor.fetchall()
    users = [UserList(id=user[0], name=user[1], type=user[2]) for user in users]
    return users

@app.get("/get_user/{id_user}", response_model=UserList)
async def get_user_route(id_user: int, token: str = Depends(get_token)):
    """Get an users in database. You must have a admin authentication type.
    """
    authenticated_user(token)
    conn, cursor = db_connection()
    cursor.execute(
        "SELECT * FROM users WHERE id = ?;", (id_user, )
    )
    user = cursor.fetchone()
    user = UserList(id=user[0], name=user[1], type=user[2])
    return user

@app.delete("/delete_user/{id_user}")
async def delete_user_route(id_user: int, token: str = Depends(get_token)):
    """Delete an users in database. You must have a admin authentication type.
    
    Args:
        id_user (int): User id
    
    Returns: Success message
    """
    authenticated_user(token)
    conn, cursor = db_connection()
    cursor.execute(
        "DELETE FROM users WHERE id = ?;", (id_user, )
    )
    conn.commit()
    return {"message": f" User {id_user} deleted."}

@app.post("/sa_prediction/", response_model=Prediction)
def prediction_route(text: Text, token: str = Depends(get_token)):
    """Predict a sentiment analysis from a text.

    Args:
        text (str): Text to be classified
    Returns:
        Prediction: The sentiment analysis result with predicted classe and score
    """
    authenticated_user_predict(token)
    user = get_user(token)
    predict_class = prediction(text.text)
    history_insert(user[0], text.text, predict_class[0], predict_class[1])
    return Prediction(predict=predict_class[0], score=predict_class[1])

# Run app
if __name__ == "__main__":
    database_initialization()
    uvicorn.run(app, host="0.0.0.0", port=8000)