## Task 002: Building a Sentiment Analysis API

### Project Overview

Sentiment analysis is the process of examining a text to classify the emotional character of the message, which may be positive, negative, or neutral. In the era of Big Data, companies have access to vast amounts of information derived from social media comments, chats, and audio recordings transcripts. Consequently, sentiment analysis has evolved into a potent Business Intelligence tool, assisting companies in enhancing their services and products.

In this project, we have developed an application for sentiment analysis alongside an API facilitating interaction with our classifier. The application's primary functionality is to predict a given text's emotional tone. Utilizing the API allows users to create accounts, submit text for classification, and access the classification history associated with a user. The API is integrated with an SQLite3 database to store performed classifications.

---
### Business Requirements

- Build a method that allows authenticated users to view all their texts. 
- Create a second table in the database to store users and their passwords.
- Develop a method for creating users.
- Verify if the user exists and if the password is correct before returning a prediction.
- Establish a method to retrieve all texts from a user if the password is correct.

---

### Project Architecture

- `SAProject`: main directory.
  - `api`: a directory to api scripts.
    - `api.py`: Main FastAPI application.
    - `authentication.py` : Contains functions to user authentication.
    - `database.py`: Functions to database integrations, including insert, delete, update and connections.
    - `models.py`: Specifies Pydantic models representing the data structures for request and response.
  - `app`:  a directory to SA application.
    - `sentiment_analysis.py`: Sentiment analysis implementation using Hugging Face's transformers.
  - `pyproject.toml`: To project management, dependencies and configurations.

---
### API Routes/Endpoints

- `POST /create_user/`: To create a new user.
- `POST /sa_prediction/`: Submit a text for sentiment analysis.
- `GET /users`: Retrieve all users.
- `GET /user/`: Retrieve all attributes from a specific user.
- `GET /texts`: Retrieve all texts submitted to analyze by an user.