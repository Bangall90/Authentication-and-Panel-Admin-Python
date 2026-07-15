import hashlib
from database import cursor, conn

def registrasi_user():
    print("=" * 50)
    print("REGISTRASI AKUN ANDA")
    print("=" * 50)

    username = input("Silahkan Buat Username Anda: ").strip()
    password = input("Silahkan Buat Password Anda: ").strip()

    if username == "" or password == "":
        print("Username atau Password Tidak Boleh Kosong")
        return
    
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()


    if existing_user:
        print("Username sudah terdaftar, silahkan pakai username lain!")
        return

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    print("\nSelamat Akun Anda Selesai Dibuat!")

    print("-" * 50)

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
    conn.commit()