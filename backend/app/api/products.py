from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.services.product_service import load_products, add_product
from typing import List

router = APIRouter()


@router.get("/products", response_model=List[Product])
def get_products():
    return load_products()


@router.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    products = load_products()
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.post("/products", response_model=Product)
def create_product(product: Product):
    return add_product(product)

