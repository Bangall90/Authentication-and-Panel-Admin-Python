import hashlib
from database import cursor

def login_user():
    print("=" * 50)
    print("LOGIN AKUN ANDA")
    print("=" * 50)

    username = input("Silahkan Buat Username Anda: ").strip()
    password = input("Silahkan Buat Password Anda: ").strip()

    if username == "" or password == "":
        print("Username atau Password Tidak Boleh Kosong")
        return
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password_hash))
    users = cursor.fetchone()

    if users:
        return True
    else:
        return False