from fastapi import FastAPI
from  mangum import Mangum
from dynamo_db import query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Auroshis!!"}

@app.get("/dynamo_query")
async def query_function(search=None):
    try:
        return query(search)
    except Exception:
        return "error occured"


handler = Mangum(app=app)