from fastapi import APIRouter, HTTPException
from typing import List
from app.classes.Product import Product
from app.classes.StoreCatalog import StoreCatalog

router = APIRouter()
catalog = StoreCatalog()

@router.get("/products", response_model=List[Product])
def get_products():
    return catalog.load()

@router.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    products = catalog.load()
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.post("/products", response_model=Product)
def create_product(product: Product):
    return catalog.add_product(product)

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_data: Product):
    updated = catalog.update_product(product_id, updated_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

