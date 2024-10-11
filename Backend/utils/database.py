from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGODB_URL
from utils.extras import get_random_id
from utils.logger import Logger

logger = Logger(__name__)

logger.info("Connecting to MongoDB")
DB = AsyncIOMotorClient(MONGODB_URL)["MediConnect"]
logger.info("Connected to MongoDB")

SHOPDB = DB["SHOPDB"]
AUTHDB = DB["AUTHDB"]

# Auth Fucntions


async def new_auth(email: str, password: str) -> bool:
    auth = await AUTHDB.find_one({"email": email})
    if auth:
        # Email is already registered
        return False

    await AUTHDB.insert_one({"email": email, "password": password})
    return True


async def check_auth(email: str, password: str) -> bool:
    auth = await AUTHDB.find_one({"email": email})
    if auth:
        if auth["password"] == password:
            return True

    return False


# Shop Fucntions


async def add_shop(data):
    data["shop_id"] = get_random_id(6)
    await SHOPDB.insert_one(data)
