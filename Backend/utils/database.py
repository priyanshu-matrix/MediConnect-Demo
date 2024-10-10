from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv("config.env")

MONGODB_URL = os.getenv("MONGODB_URL")

db = AsyncIOMotorClient(MONGODB_URL)

testdb = db["testdb"]

async def test():
    await testdb.test.insert_one({"test": "test"})

import asyncio
asyncio.run(test())