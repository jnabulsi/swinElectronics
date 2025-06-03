from app.storage.JsonStore import read_json, write_json  

class AccountService:
    def __init__(self, file_path):
        self.file_path = file_path

    def register(self, name, email, password):
        accounts = read_json(self.file_path)
        if any(a["email"] == email for a in accounts):
            raise ValueError("Email already in use.")

        new_id = max((a.get("id", 0) for a in accounts), default=0) + 1
        account = {
            "id": new_id,
            "name": name,
            "email": email,
            "password": password,
            "isAdmin": False
        }
        accounts.append(account)
        write_json(self.file_path, accounts)
        return account

