from pydantic import BaseModel

# Set the data model to API response

class User(BaseModel):
    """User creation to api usage. An user can be an admin or a select type. Admin users can create other users, but select users just can make text classifications. 

    Args:
        name (str): An user name
        type (str): the user type admin or select
    """

    name: str
    type: str

class UserList(BaseModel):
    """Parameters lists returned when a admin user get users list. 

    Args:
        id (int): The id_user, a value to identify an user in dataset
        name (str): An user name
        type (str): the user type admin or select
    """

    id: int
    name: str
    type: str

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
