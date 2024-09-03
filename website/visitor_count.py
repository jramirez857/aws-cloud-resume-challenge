import boto3
import json

print('Loading function')
dynamo = boto3.resource('dynamodb')


table = dynamo.Table('visitor_count')

def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''

    response = table.update_item(
        Key={"id": "1"},
        ExpressionAttributeNames = {
            "#c": "visitors"
        },
        UpdateExpression="set #c = #c + :val",
        ExpressionAttributeValues={
            ":val": 1
        },
        ReturnValues = "UPDATED_NEW"
        )
        
    response = table.get_item(
        Key={"id": "1"}
    )
    responseBody = response['Item']['visitors'].__str__()
    
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://joseramirez.cloud',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': responseBody
    }
