from fastapi import FastAPI
from mangum import Mangum
import boto3
from boto3.dynamodb.conditions import Key, Attr
import os
from pydantic import BaseModel

app = FastAPI()

class foodItem(BaseModel):
    itemName: str
    quantity: str
    about_to_over: bool

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

@app.get("/")
async def root():
    return {"message": "Hello from Auroshis!!"}

@app.get("/get_query")
async def get_query_function(search: str = None):
    try:
        return get_query(search)
    except Exception:
        return "error occured"

@app.post("/put_query")
async def put_query_function(food:foodItem):
    try:
        return put_query(food_name=food.itemName, about_to_over=food.about_to_over, quantity=food.quantity)
    except Exception:
        return "error occured"
    

handler = Mangum(app=app)