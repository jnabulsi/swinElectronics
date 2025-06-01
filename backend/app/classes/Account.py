from pydantic import BaseModel
from typing import Optional
from pathlib import Path
# import jwt
# import bcrypt
import json
from typing import List
import hashlib 
import os

ACCOUNTS_FILE = Path(__file__).parent.parent / "data" / "accounts.json"

class Account(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    password: str
    # isAdmin: bool

    # SIDENOTE: The secret key is stored hard coded due to the restraints of the project. 
    # IT IS NOT MEANT FOR PRODUCTION PURPOSES.
    # SECRET_KEY = "21580a29e8dcc93f039db42a74eda13e5e2b1a52b9ee9c57f5619b50d6a7d936"

    # Remembers where the json file is
class AccountService:
    def __init__(self, file_path: Path = ACCOUNTS_FILE):
        self.file_path = file_path

    def load_accounts(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_accounts(self, accounts):
        with open(self.file_path, "w") as f:
            json.dump(accounts, f, indent=2)

    def register(self, name, email, password):
        # check if user email already exists
        accounts = self.load_accounts()
        id = max([acc.get('id', 0) for acc in accounts], default=0) + 1

        new_acct = {
            "id": id,
            "name": name,
            "email": email,
            "password": password
        }
        
        accounts.append(new_acct)
        self.save_accounts(accounts)
        return new_acct
        
        # DO THIS LATER
        # for account in accounts:
        #     if( email == account['email'] ):
        #         raise ValueError

        # use encryption to salt and hash the pw


    # def hash_password(password: str, salt: bytes = None) -> (str, str):
    #     if salt is None:
    #         salt = os.urandom(16)
    #     pwd_hash = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    #     return pwd_hash, salt.hex()

    # def login(self, email, password):
    #     user = self.user_store.get(email)
    #     if not user or not bcrypt.checkpw(password.encode(), user["hashed_password"]):
    #         raise ValueError("Invalid credentials")
    #     payload = {
    #         "sub": email,
    #         "exp": datetime.utcnow() + timedelta(minutes=self.TOKEN_EXPIRATION_MINUTES)
    #     }
    #     token = jwt.encode(payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
    #     return token
    
    # def verify_token(self, token):
        # try:
        #     payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        #     return payload["sub"]
        # except jwt.ExpiredSignatureError:
        #     raise ValueError("Token expired")
        # except jwt.InvalidTokenError:
        #     raise ValueError("Invalid token")

