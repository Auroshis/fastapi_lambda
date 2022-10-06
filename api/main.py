from fastapi import FastAPI
from  mangum import Mangum
from . import dynamo_db
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Auroshis!!"}

@app.get("/dynamo_query")
async def query_function(search=None):
    try:
        return dynamo_db.query(search)
    except Exception:
        return "error occured"


handler = Mangum(app=app)