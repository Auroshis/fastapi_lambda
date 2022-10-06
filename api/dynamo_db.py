from this import d
import boto3
from boto3.dynamodb.conditions import Key, Attr
import os

def query(value):
    
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                region_name=os.getenv("REGION"))

    table = dynamodb.Table('FoodItems')


    response = table.query(
            KeyConditionExpression=Key('itemName').eq(value)
        )
    
    return response['Items']
