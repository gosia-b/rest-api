# Overview
REST APIs allow you to interact with resources via HTTP requests.  
This API is for managing a database of users. It has only one endpoint - users.  
Here are listed all possible requests:

<img src="https://github.com/gosia-b/rest-api/blob/main/requests.png" width="40%">

Users for the database are taken from the API for generating random users: https://randomuser.me/

# Use
To serve the API, run main.py  

Then to send GET users requets either:
- type http://localhost:5000/users in your web browser
- in your terminal, execute curl http://localhost:5000/users
- python requests

# Reference
https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb
https://parzibyte.me/blog/en/2020/11/12/creating-api-rest-with-python-flask-sqlite3/
