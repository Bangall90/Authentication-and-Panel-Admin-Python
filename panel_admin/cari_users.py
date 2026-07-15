from database import cursor

def cari_user():
    cari_id = input("Masukkan ID yang dicari: ").strip()
    cari_username = input("Masukkan Username yang dicari: ").strip()

    cursor.execute("SELECT * FROM users WHERE id = ? AND username = ?", (cari_id, cari_username))
    hasil_pencarian = cursor.fetchall()

    print("=" * 100)
    print(f"{'ID':<5}{'Username':<20}{'Password':<20}")
    print("=" * 100)

    if hasil_pencarian:
        for user in hasil_pencarian:
            id, username, password = user
            print(f"{id:<5}{username:<20}{password:<20}")
            print("-" * 100)
    else:
        print("Data tidak ditemukan")