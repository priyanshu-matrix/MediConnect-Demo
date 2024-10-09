from fastapi import FastAPI
from utils.random_int import random_number

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "random_number": random_number()}
