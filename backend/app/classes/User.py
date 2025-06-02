from pydantic import BaseModel  
from pathlib import Path
import json

USERS_FILE = Path(__file__).parent.parent / "data" / "users.json"

class User(BaseModel):
    name: str
    email: str
    age: int
    address: str
    isAdmin: bool

class UserService:
    def __init__(self, file_path: Path = USERS_FILE):
        self.file_path = file_path

    def load_users(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def save_users(self, users):
        with open(self.file_path, "w") as f:
            json.dump(users, f, indent=2)

    def create_user(self, name, email, age, address):
        users = self.load_users()

        new_user = {
            "name": name,
            "email": email,
            "age": age,
            "address": address,
            "isAdmin": False
        }

        users.append(new_user)
        self.save_users(users)