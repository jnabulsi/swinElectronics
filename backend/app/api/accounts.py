from fastapi import APIRouter, HTTPException, Body
from app.classes.Account import Account, AccountService 
from app.classes.User import UserService

router = APIRouter()
acct = AccountService()
user = UserService()

@router.post("/signup", response_model=Account)
def register_account(payload: dict = Body(...)): # instead of data: Account
    print("Payload received:", payload)
    # Extract Account fields
    name = payload["name"]
    email = payload["email"]
    password = payload["password"]

    # Extract User fields
    age = payload["age"]
    address = payload["address"]

    print("Name:", name)
    print("Email:", email)
    print("Age:", age)
    print("Address:", address)
    print("Pw:", password)

    try:
        new_account = acct.register(name, email, password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    user.create_user(name, email, age, address)
    
    return new_account

# @router.post("/login", response_model=Account)
# def login(payload: dict = Body(...)):
#     email = payload["email"]
#     password = payload["password"]