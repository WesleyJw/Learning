## Task 002: Building a Sentiment Analysis API

### Project Overview

Sentiment analysis is the process of examining a text to classify the emotional character of the message, which may be positive, negative, or neutral. In the era of Big Data, companies have access to vast amounts of information derived from social media comments, chats, and audio recordings transcripts. Consequently, sentiment analysis has evolved into a potent Business Intelligence tool, assisting companies in enhancing their services and products.

In this project, we have developed an application for sentiment analysis alongside an API facilitating interaction with our classifier. The application's primary functionality is to predict a given text's emotional tone. Utilizing the API allows users to create accounts, submit text for classification, and access the classification history associated with a user. The API is integrated with an SQLite3 database to store performed classifications.

---
### Business Requirements

- Create an app to text classification.  Use a pre-trained model from Hugging Face's transformers library for sentiment analysis.
- Create a RESTful API to text sentiment analysis. 
- Develop a method for creating users.
- Create a table in the database to store users and their passwords.
- Verify if the user exists and if the password is correct before returning a prediction.
- Build a method that allows authenticated users to view all their texts. 
- Establish a method to retrieve all texts from a user if the password is correct.

---

### Project Architecture

- `SAProject`: main directory.
  - `api`: a directory to api scripts.
    - `api.py`: Main FastAPI application.
    - `authentication.py` : Contains functions to user authentication.
    - `database.py`: Functions to database integrations, including insert, delete, update and connections.
    - `model.py`: Specifies Pydantic models representing the data structures for request and response.
  - `app`:  a directory to SA application.
    - `sentiment_analysis.py`: Sentiment analysis implementation using Hugging Face's transformers.
  - `pyproject.toml`: To project management, dependencies and configurations.
  - `poetry.lock`: To management versions of your project and dependencies (including sub-dependencies).

---
### API Routes/Endpoints

- `POST /create_user/`: To create a new user.
- `POST /sa_prediction/`: Submit a text for sentiment analysis.
- `GET /users`: Retrieve all users.
- `GET /user/`: Retrieve all attributes from a specific user.
- `GET /texts`: Retrieve all texts submitted to analyze by an user.

---
### Project Dependencies

- `poetry`: To project management.
- `pytorch`: To sentiment analysis.
- `transformers`: To use a pre-trained sentiment analysis model.
- `fastapi`: Build an API fast.
- `uvicorn`: To web server implementation. 
- `sqlite3`: To data storage.

We are using the `CPU` library version to install a clean version of the pytorch library. Adding the following config to poetry makes it possible to use the `CPU` version.

```bash
poetry source add -p explicit pytorch https://download.pytorch.org/whl/cpu
```

Installing dependencies with poetry:

```bash
poetry add --source pytorch torch torchvision

poetry add fastapi uvicorn transformers
```
---
### API Usage

#### Using cUrl commands. 

- Create a new user.

```bash
$ curl -X POST "http://localhost:8000/create_user/" -H "Content-Type: application/json" -H "Authorization: Bearer 123456" -d '{"name": "Silva", "type": "select"}'
$ {"name":"Silva","type":"select. Please, copy the user token: 8adb56c8b7dc86e07a9f2fa4a25c8bf7c0de4ffe"}
```

```bash
$ curl -X POST "http://localhost:8000/create_user/" -H "Content-Type: application/json" -H "Authorization: Bearer 8adb56c8b7dc86e07a9f2fa4a25c8bf7c0de4ffe" -d '{"name": "Joana", "type": "select"}'
$ {"detail":"Forbidden. You don't have permission to create users."}
```


