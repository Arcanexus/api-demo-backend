# lambda-api-demo
[![deploy to lambda](https://github.com/Arcanexus/api-demo-backend/actions/workflows/main.yml/badge.svg)](https://github.com/Arcanexus/api-demo-backend/actions/workflows/main.yml)

## Summary
A simple set of Python scripts simulating a CRUD based API.

## Backend API
The backend has been built as a simple [AWS lambda](https://aws.amazon.com/fr/lambda/) function.

It manages the following operations :
| HTTP Method | Request Payload  | HTTP Return code  | Response |
|---|---|---|---|
|GET   | No  | 200   | Hello, world.  |
|POST   | Yes (json)  | 201  | ```{ "Result": "Created", "Values": <payload>} ```  |
|PUT   | Yes (json)  | 201  | ```{ "Result": "Created", "Values": <payload>} ```  |
|PATCH   | Yes (json)  | 202  | ```{ "Result": "Modified", "Values": <payload>} ```  |
|DELETE   | Yes (json)  | 204  |  |

