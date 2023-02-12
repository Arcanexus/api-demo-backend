# lambda-api-demo

## Summary
A simple set of Python scripts simulating a CRUD based API.

## Backend API
The backend has been built as a simple [AWS lambda](https://aws.amazon.com/fr/lambda/) function.

It manages the following operations :
| HTTP Method | Request Payload  | HTTP Return code  | Response |
|---|---|---|---|
|GET   | No  | 200   | Hello, world.  |
|POST   | Yes (json)  | 201  | ```{ 'Created': <payload> "} ```  |
|PUT   | Yes (json)  | 201  | ```{ 'Created': <payload> "} ```  |
|PATCH   | Yes (json)  | 202  | ```{ 'Modified': <payload> "} ```  |
|DELETE   | Yes (json)  | 204  | ```{ 'Deleted': <payload> "} ```  |

## Frontend webapp
The frontend is a Flask webapp.

To run the webapp :
1. (Optional) Create a Venv
2. Install prerequisites from **requirements.txt**
3. Run ```python app.py```
4. Browse [localhost:5000](http://localhost:5000) (change the URL depending on where you deployed the webapp)