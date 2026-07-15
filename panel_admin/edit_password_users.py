import hashlib
from database import cursor, conn

def edit_password_user():
    cari_id = input("\nSilahkan input ID user untuk mencari data yang ingin anda edit: ")

    cursor.execute("SELECT * FROM users WHERE id = ?", (cari_id,))
    hasil_pencarian = cursor.fetchall()

    if hasil_pencarian:
        print("ID user ditemukan")
        print("\n")
        print("=" * 100)
        print(f"{'ID':<5}{'Username':<20}{'Password':<20}")
        print("=" * 100)

        for user in hasil_pencarian:
            id, username, password = user
            print(f"{id:<5}{username:<20}{password:<20}")
            print("-" * 100)
        
        password = input("Silahkan Buat Password Baru Anda: ").strip()

        if password == "":
            print("Password Tidak Boleh Kosong")
            return
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (password_hash, cari_id))
        conn.commit()
        
        print("\nPassword berhasil diubah silahkan login kembali")
    else:
        print("ID user tidak ditemukan")
