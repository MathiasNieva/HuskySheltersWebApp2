  
import json
import boto3
import os
from boto3.dynamodb.conditions import Key

pets_table = os.environ['PETS_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(pets_table)

def getAllPets(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    response = table.scan(
        FilterExpression = Key('SK').eq('Dog') | Key('SK').eq('Cat')
    )
    
    items = response['Items']
    print(items)
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin" : "*", # Required for CORS support to work
            "Access-Control-Allow-Credentials" : True # Required for cookies, authorization headers with HTTPS 
         },
        'body': json.dumps(items)
    }