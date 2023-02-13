import json

def lambda_handler(event, context):
  HTTPMethod = event['httpMethod']
    
  #CRUD (pour Create, Read, Update, Delete) 
  if HTTPMethod == "POST" or HTTPMethod == "PUT":
    try:
      body = json.loads(event['body'])
    except:
      return {
        'statusCode': 400,
        'body': "Bad request: the body must be in valid JSON format."
      }
    return {
      'statusCode': 201,
      'body': "{ 'Created': " + json.dumps(body) + "}"
    }

  if HTTPMethod == "GET":
    return {
      'statusCode': 200,
      'body': "Hello, world."
    }

  if HTTPMethod == "PATCH":
    try:
      body = json.loads(event['body'])
    except:
      return {
        'statusCode': 400,
        'body': "Bad request: the body must be in valid JSON format."
      }
    return {
      'statusCode': 202,
      'body': "{ 'Modified': " + json.dumps(body) + "}"
    }
  
  if HTTPMethod == "DELETE":
    try:
      body = json.loads(event['body'])
    except:
      return {
        'statusCode': 400,
        'body': "Bad request: the body must be in valid JSON format."
      }
    return {
      'statusCode': 204,
      'body': "{ 'Deleted': " + json.dumps(body) + "}"
    }