from fastapi import APIRouter, HTTPException
from app.services.AccountService import AccountService
from app.models.AccountModel import AccountOut, AccountIn, LoginIn
from app.config import acctService

router = APIRouter()

@router.post("/signup", response_model=AccountOut)
def register_account(data: AccountIn):
    try:
        new_account = acctService.register(data.name, data.email, data.password, data.address)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return new_account

@router.post("/login", response_model=AccountOut)
def login(data: LoginIn):
    try:
        account_found = acctService.login(data.email, data.password)
        return account_found
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
