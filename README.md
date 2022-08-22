# Introduction
An application programming interface (API) is defined as an interface that handles the interactions between two or more pieces of software - commonly between a client application and a database.

The primary protocol for any web-based communication is HTTP.

HTTP is a request-response protocol, meaning that any interaction between two parties is composed of a request and a response. The client issues the request to the server, and then the server sends a response to the client, even if it can't fulfil the request.

<img src="https://github.com/gosia-b/rest-api/blob/main/images/api.png" width="80%">


A valid HTTP request has four components: an URL (Uniform Resource Locator), a method, a list of headers, and a body:

<img src="https://github.com/gosia-b/rest-api/blob/main/images/request.png" width="50%">

The response coming from the server is composed of a status code, a list of headers, and a body:
<img src="https://github.com/gosia-b/rest-api/blob/main/images/response.png" width="50%">


# Overview
REST APIs allow you to interact with resources via HTTP requests.  
This API is for managing a database of users. It has only one endpoint - users.  
Here are listed all possible requests:

<img src="https://github.com/gosia-b/rest-api/blob/main/images/requests.png" width="40%">

Users for the database are taken from the API for generating random users: https://randomuser.me/

# Use
To serve the API, run main.py  

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
