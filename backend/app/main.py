from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import products_router, cart_router, orders_router, accounts_router, sales_router

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(orders_router, prefix="/api")
app.include_router(accounts_router, prefix="/api")
app.include_router(sales_router, prefix="/api")

