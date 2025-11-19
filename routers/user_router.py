from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
async def create_user(user: User):
    return await user.create()


@router.get("/", response_model=List[User])
async def get_users():
    return await User.find_all().to_list()


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: str, new_data: User):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(404, "User not found")

    await user.set(new_data.dict())
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(404, "User not found")

    await user.delete()
    return {"message": "User deleted"}
