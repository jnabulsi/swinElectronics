from fastapi import APIRouter, HTTPException
from app.services.AccountService import AccountService
from app.services.UserService import UserService
from app.models.AccountModel import AccountOut, AccountIn
from app.config import acctService, userService

router = APIRouter()

@router.post("/signup", response_model=AccountOut)
def register_account(data: AccountIn):
    try:
        new_account = acctService.register(data.name, data.email, data.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    userService.create_user(
        name=data.name,
        email=data.email,
        age=data.age,
        address=data.address
    )

    return new_account

