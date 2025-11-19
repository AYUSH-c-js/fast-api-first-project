from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from models.user import User
from models.product import Product


async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["fastapi_db"]

    await init_beanie(database=db, document_models=[User, Product])
