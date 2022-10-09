from fastapi import FastAPI
from  mangum import Mangum
import dynamo_db
from pydantic import BaseModel

app = FastAPI()

class foodItem(BaseModel):
    itemName: str
    quantity: str
    about_to_over: bool

@app.get("/")
async def root():
    return {"message": "Hello from Auroshis!!"}

@app.get("/get_query")
async def get_query_function(search: str = None):
    try:
        return dynamo_db.get_query(search)
    except Exception:
        return "error occured"

@app.post("/put_query")
async def put_query_function(food:foodItem):
    try:
        return dynamo_db.put_query(food_name=food.itemName, about_to_over=food.about_to_over, quantity=food.quantity)
    except Exception:
        return "error occured"
    

handler = Mangum(app=app)