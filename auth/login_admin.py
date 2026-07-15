daftar_admin = {
    "ryuuo": "admin123",
    "budi": "budi01gaming"
}

def login_admin():
    username = input("Username Admin: ").strip().lower()
    password = input("Password Admin: ").strip().lower()

    if username in daftar_admin and daftar_admin[username] == password:
        return True
    else:
        return False