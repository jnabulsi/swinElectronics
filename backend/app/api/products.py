from fastapi import APIRouter, HTTPException
from typing import List
from app.models.ProductModel import Product
from app.config import catalogService# shared service instance

router = APIRouter()

@router.get("/products", response_model=List[Product])
def get_products():
    return catalogService.load()

@router.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    products = catalogService.load()
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/products", response_model=Product)
def create_product(product: Product):
    return catalogService.add_product(product)

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_data: Product):
    updated = catalogService.update_product(product_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

