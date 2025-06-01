from fastapi import APIRouter, HTTPException
from typing import List
from app.classes.Product import Product
from app.classes.StoreCatalog import StoreCatalog
from pathlib import Path
from app.classes.Account import Account

router = APIRouter()
acct = Account()
# ACCOUNTS_FILE = Path(__file__).parent.parent / "data" / "accounts.json"

@router.post("/signup", response_model=Account)
def register_account(data: Account):
    new_account = acct.register(data.name, data.email, data.password)
    return new_account