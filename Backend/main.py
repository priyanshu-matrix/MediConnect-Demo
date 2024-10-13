from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import Literal

from utils import database
from utils.logger import Logger

app = FastAPI()
logger = Logger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        status, message = await database.new_auth(email, password)
    elif request_type == "check_auth":
        status, message = await database.check_auth(email, password)
    else:
        status, message = False, "Invalid Request Type"

    return {"status": status, "message": message}


@app.post("/api/shop")
async def api_auth(request: Request):
    data: dict = await request.json()
    logger.info(f"Shop Data: {data}")

    request_type: Literal["update_shop", "get_shop"] = data.get("request_type")
    email: str = data.get("email")
    shop_data: dict = data.get("shop_data")

    if request_type == "update_shop":
        await database.update_shop(email, shop_data)
        status, message = True, "Shop Data Updated Successfully"

    elif request_type == "get_shop":
        status, message = await database.get_shop(email)

    else:
        status, message = False, "Invalid Request Type"

    return {"status": status, "message": message}
