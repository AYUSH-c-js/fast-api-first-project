from fastapi import APIRouter, HTTPException
from typing import List
from models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=Product)
async def create_product(product: Product):
    return await product.create()


@router.get("/", response_model=List[Product])
async def get_products():
    products = await Product.find_all().to_list()

    # IMPORTANT FIX FOR BEANIE v1
    for p in products:
        if p.owner:
            p.owner = await p.owner.fetch()

    return products


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(404, "Product not found")

    if product.owner:
        product.owner = await product.owner.fetch()

    return product


@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: str, new_data: Product):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(404, "Product not found")

    await product.set(new_data.dict())
    return product


@router.delete("/{product_id}")
async def delete_product(product_id: str):
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(404, "Product not found")

    await product.delete()
    return {"message": "Product deleted"}
