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
    - `sql_queries.py`: SQL queries to select, insert, create, update and delete users and texts.
  - `app`:  a directory to SA application.
    - `sentiment_analysis.py`: Sentiment analysis implementation using Hugging Face's transformers.
  - `pyproject.toml`: To project management, dependencies and configurations.
  - `poetry.lock`: To management versions of your project and dependencies (including sub-dependencies).

---
### API Routes/Endpoints

- `GET /`: API root route with documentation.
- `POST /create_user/`: To create a new user.
- `POST /sa_prediction/`: Submit a text for sentiment analysis.
- `GET /list_users`: Retrieve all users.
- `GET /get_user/`: Retrieve all attributes from a specific user.
- `GET /get_history`: Retrieve all texts submitted to analyze by an user.
- `DELETE /delete_user/`: Delete user by id.

---
### Project Dependencies

- `poetry`: To project management.
- `pytorch`: To sentiment analysis.
- `transformers`: To use a pre-trained sentiment analysis model.
- `fastapi`: Build an API fast.
- `uvicorn`: To web server implementation. 
- `sqlite3`: To data storage.
- `hashlib`: To create a password hash.
- `random`: To generate a password random seed.

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

#### Creating new users

- Authenticated

```bash
$ curl -X POST "http://localhost:8000/create_user/" -H "Content-Type: application/json" -H "Authorization: Bearer 123456" -d '{"name": "Silva", "type": "select"}'
$ {"name":"Silva","type":"select. Please, copy the user token: 8adb56c8b7dc86e07a9f2fa4a25c8bf7c0de4ffe"}
```

- Not Authenticated

```bash
$ curl -X POST "http://localhost:8000/create_user/" -H "Content-Type: application/json" -H "Authorization: Bearer 8adb56c8b7dc86e07a9f2fa4a25c8bf7c0de4ffe" -d '{"name": "Joana", "type": "select"}'
$ {"detail":"Forbidden. You don't have permission to create users."}
```

#### List users:

- Authenticated

```bash
$ curl -X GET "http://localhost:8000/list_users" -H "Content-Type: application/json" -H "Authorization: Bearer b2702f817e7d6884237898610772171d1a6411dc" 
$ [
  {"id":1,"name":"Wesley","type":"admin"},
  {"id":4,"name":"Lima","type":"select"},
  {"id":16,"name":"Ana","type":"select"},
  {"id":17,"name":"Maria","type":"admin"}]
```

- Authenticated but without permissions to list users

```bash
$ curl -X GET "http://localhost:8000/list_users" -H "Content-Type: application/json" -H "Authorization: Bearer 8adb56c8b7dc86e07a9f2fa4a25c8bf7c0de4ffe" 
$ {"detail":"Forbidden. You don't have admin permission to manage users."}
```

- Not Authenticated or Invalid users

```bash
$ curl -X GET "http://localhost:8000/list_users" -H "Content-Type: application/json" -H "Authorization: Bearer 8adb56c8b7dc86e07a9f2fa4a25c8bf7c0de4" 
$ {"detail":"Invalid user."}
```
- Get a specific user by id

```bash
$ curl -X GET "http://localhost:8000/get_user/{1}" -H "Content-Type: application/json" -H "Authorization: Bearer b2702f817e7d6884237898610772171d1a6411dc" 
$ {"id":1,"name":"Wesley","type":"admin"}
```

#### Delete user

```bash
$ curl -X DELETE "http://localhost:8000/delete_user/{15}" -H "Content-Type: application/json" -H "Authorization: Bearer b2702f817e7d6884237898610772171d1a6411dc" 
$ {"message":" User 15 deleted."}
```

#### Make a sentiment analysis prediction

```bash
$ curl -X POST "http://localhost:8000/sa_prediction/" -H "Content-Type: application/json" -H "Authorization: Bearer 123456" -d '{"text": "I will married tonight."}'
$ {"predict":"POSITIVE","score":0.9992058873176575}
```

#### Get all sentiment analysis predictions by user

```bash
curl -X GET "http://localhost:8000/get_history/{1}" -H "Content-Type: application/json" -H "Authorization: Bearer 123456" 
$ [
  {"id":1,"id_user":1,"text":"I will married tonight.","predict":"POSITIVE","score":0.9992058873176575},
  {"id":2,"id_user":1,"text":"I take a bus to chicago and the bus broken","predict":"NEGATIVE","score":0.999517560005188}
  ]
```