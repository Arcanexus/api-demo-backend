import json

def lambda_handler(event, context):
  HTTPMethod = event['httpMethod']
    
  #CRUD (pour Create, Read, Update, Delete) 
  if HTTPMethod == "POST" or HTTPMethod == "PUT":
    body = json.loads(event['body'])
    return {
      'statusCode': 201,
      'created': json.dumps(body)
    }

  if HTTPMethod == "GET":
    return {
      'statusCode': 200,
      'Retrieved': "Hello, world."
    }

  if HTTPMethod == "PATCH":
    body = json.loads(event['body'])
    return {
      'statusCode': 202,
      'patched': json.dumps(body)
    }
  
  if HTTPMethod == "DELETE":
    body = json.loads(event['body'])
    return {
      'statusCode': 204,
      'patched': json.dumps(body)
    }