from app.storage.JsonStore import read_json, write_json  
from cryptography.fernet import Fernet

# This key is used to encrypt the password to be store in json. 
# This is not best practice, but due to the limitation of the project, it is stored in code.
KEY = b'_3eQ1g8--unoHtNozmK8XClXVv4UWzcghk-hGRJh0o8='

class AccountService:
    def __init__(self, file_path):
        self.file_path = file_path
        self.f = Fernet(KEY)

    def register(self, name, email, password, address):
        accounts = read_json(self.file_path)
        if any(a["email"] == email for a in accounts):
            raise ValueError("Email already in use.")

        new_id = max((a.get("id", 0) for a in accounts), default=0) + 1
        
        encrypted_bytes = self.f.encrypt(password.encode('utf-8'))

        encrypted_str = encrypted_bytes.decode('utf-8')
        account = {
            "id": new_id,
            "name": name,
            "email": email,
            "password": encrypted_str,
            "address": address,
            "isAdmin": False
        }
        accounts.append(account)
        write_json(self.file_path, accounts)
        return account
    
    def login(self, email, password):
        accounts = read_json(self.file_path)

        for a in accounts:
            if a["email"] == email:
                # get encrypted string pw and encode into bytes
                encrypted_password = a["password"]
                password_bytes = encrypted_password.encode('utf-8')
                
                # decrypt the stored password
                decoded_password_bytes = self.f.decrypt(password_bytes)
                
                # decode into string format
                decoded_password = decoded_password_bytes.decode('utf-8')
                
                # compare passwords
                if password == decoded_password:
                    return a    
                raise ValueError("Password incorrect.")
        raise ValueError("Email not found.")
