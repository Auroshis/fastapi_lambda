import boto3
from boto3.dynamodb.conditions import Key, Attr
import os

def get_dyanmodb():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=os.getenv('DB_SECRET_ACCESS_KEY_ID'),
                                aws_secret_access_key=os.getenv('DB_SECRET_ACCESS_KEY'),
                                region_name=os.getenv("DB_DEFAULT_REGION"))
    return dynamodb

def get_query(value):
    """
    Method to filter based on 'itemName' attribute.
    """
    dynamodb = get_dyanmodb()
    table = dynamodb.Table('FoodItems')
    response = table.query(
            KeyConditionExpression=Key('itemName').eq(value)
        )
    
    return response['Items']

def put_query(food_name, about_to_over, quantity):
    """
    Method to put a single item into db
    """
    dynamodb = get_dyanmodb()
    table = dynamodb.Table('FoodItems')
    response = table.put_item(
            # Data to be inserted
            Item={
                'itemName': food_name,
                'about_to_over': about_to_over,
                'quantity': quantity
            }
        )
    return response