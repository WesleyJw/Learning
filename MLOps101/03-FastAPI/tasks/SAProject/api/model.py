from pydantic import BaseModel

# Set the data model to API response

class User(BaseModel):
    """User creation to api usage. An user can be an admin or a select type. Admin users can create other users, but select users just can make text classifications. 

    Args:
        name (str): An user name
        type (str): the user type admin or select
        passwrod (str): A strong password to user authentication
    """
    
    name: str
    type: str
    password: str

class Text(BaseModel):
    """A text input to sentiment classification.

    Args:
        text (str): Any text to be classified.
    """
    
    text: str

class Prediction(BaseModel):
    """The text sentiment analysis classification into this classes: positive, negative and neutral. And, model accuracy to input text. 

    Args:
        predict (str): sentiment class
        score (float): model accuracy 
    """
    
    predict: str
    score: float
