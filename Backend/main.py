from fastapi import FastAPI, Request
from typing import Literal

from utils import database
from utils.logger import Logger

app = FastAPI()
logger = Logger(__name__)


@app.get("/")
async def root():
    return {"status": "Api Is Running"}


@app.post("/api/auth")
async def api_auth(request: Request):
    data: dict = await request.json()
    logger.info(f"Auth Data: {data}")

    request_type: Literal["new_auth", "check_auth"] = data.get("request_type")
    email: str = data.get("email")
    password: str = data.get("password")

    if request_type == "new_auth":
        result = await database.new_auth(email, password)
    elif request_type == "check_auth":
        result = await database.check_auth(email, password)
    else:
        result = False

    return {"status": result}
