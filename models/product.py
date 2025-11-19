from beanie import Document, Link
from typing import Optional
from models.user import User

class Product(Document):
    title: str
    price: float
    description: Optional[str] = None
    owner: Link[User]   # Reference to User

    class Settings:
        name = "products"
