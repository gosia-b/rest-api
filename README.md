# Overview
An application programming interface (API) is defined as an interface that handles the interactions between two or more pieces of software - commonly between a client application and a database.

<img src="https://github.com/gosia-b/rest-api/blob/main/images/api.png" width="70%">

This REST API is for managing a database of users. It has two endpoints - `/users` and `/users/{user_id}`.  
Here are listed all HTTP methods that you can use:

<img src="https://github.com/gosia-b/rest-api/blob/main/images/methods.png" width="40%">

# How to use
This API is built using Flask - a web framework written in Python which allows to easily develop web applications.

<img src="https://github.com/gosia-b/rest-api/blob/main/images/flask.png" width="20%">

For the API to work, run `main.py` - you will have the Flask application running on local host, port 5000 (default port for Flask).  
When you have the API running, you can send HTTP requests. Here is how you can do it in 3 ways:

### 1. Web browser
In the web browser you can only make GET requests. For example, to return a user with `user_id = 1`, enter the following URL:
```
http://localhost:5000/users/1
```

### 2. curl
curl is a command line tool for transferring data. It supports about 22 protocols, including HTTP.  
Run the following command in your terminal to add a new user to the database:
```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "Colleen", "email": "colleen.brown@example.com", "address": "3904 First Street", "phone": "(908) 256-2784"}' \
    http://localhost:5000/users
```
(If you're on Windows - it won't work in PowerShell, you can use e.g. Git Bash instead)

### 3. Python requests library
```python
import requests

response = requests.get('http://localhost:5000/users/1')
print(response.text)
```

Notebook `use_api.ipynb` contains more examples of using the API with Python.

# Reference
- [Article 1](https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb)  
- [Article 2](https://parzibyte.me/blog/en/2020/11/12/creating-api-rest-with-python-flask-sqlite3/) with [code](https://github.com/parzibyte/api-rest-python-sqlite3/)
- Users for the database are taken from the [API](https://randomuser.me/) for generating random users
