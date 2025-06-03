from pathlib import Path
from app.storage.JsonStore import read_json, write_json  
from app.models.UserModel import User

class UserService:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load_users(self):
        return read_json(self.file_path)

    def save_users(self, users):
        write_json(self.file_path, users)

    def create_user(self, name, email, age, address):
        users = self.load_users()

        new_user = User(
            name=name,
            email=email,
            age=age,
            address=address,
            isAdmin=False
        ).dict()

        users.append(new_user)
        self.save_users(users)

