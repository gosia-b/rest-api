# Overview
An application programming interface (API) is defined as an interface that handles the interactions between two or more pieces of software - commonly between a client application and a database.

<img src="https://github.com/gosia-b/rest-api/blob/main/images/api.png" width="70%">

This REST API is for managing a database of users. It has two endpoints - `/users` and `/users/{user_id}`.  
Here are listed all HTTP methods that you can use:

<img src="https://github.com/gosia-b/rest-api/blob/main/images/methods.png" width="40%">

Users for the database are taken from the [API](https://randomuser.me/) for generating random users.

# How to use
This API is built using Flask - a web framework written in Python which allows to easily develop web applications.

<img src="https://github.com/gosia-b/rest-api/blob/main/images/flask.png" width="20%">

For the API to work, run `main.py` - you will have the Flask application running on local host, port 5000 (default port for Flask).  
Here are 3 ways in which you can interact with the API:

### 1. web browser
You can make GET requests in your web browser by entering the URL, e.g. to return a user with `user_id = 1`:
```
http://localhost:5000/users/1
```
### 2. curl
### 3. Python requests library


Then to send GET users requets either:
- type http://localhost:5000/users in your web browser
- in your terminal, execute curl http://localhost:5000/users
- python requests

# Use API
https://linuxize.com/post/curl-post-request/

if you're on windows, don't run those commands in powershell because they won't work (why??) but something else like git bash

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"name": "Colleen", "email": "colleen.brown@example.com", "address": "3904 First Street", "phone": "(908) 256-2784"}' \
http://localhost:5000/users
```


# Reference
https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
https://parzibyte.me/blog/en/2020/11/12/creating-api-rest-with-python-flask-sqlite3/ with code: https://github.com/parzibyte/api-rest-python-sqlite3/
