from fastapi import FastAPI
from database import init_db
from routers.user_router import router as user_router
from routers.product_router import router as product_router

app = FastAPI(title="FastAPI + MongoDB Beanie Project")


@app.on_event("startup")
async def start():
    await init_db()


app.include_router(user_router)
app.include_router(product_router)

#chako  hiiiiiiii.   asfsfr SWDA
     

@app.get("/")
async def home():
    return {"message": "FastAPI + MongoDB + Beanie is working!"}
