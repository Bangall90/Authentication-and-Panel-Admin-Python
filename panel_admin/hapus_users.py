from database import cursor, conn

def hapus_user():
    cari_id = input("\nSilahkan input ID user untuk mencari data yang ingin anda hapus: ")

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

        while True:
            konfirmasi = input("Apakah anda yakin ingin menghapus user ini? y/n :").lower()

            if konfirmasi == "y":
                cursor.execute("DELETE FROM users WHERE id = ?", (cari_id,))
                conn.commit()
                print("\nUser berhasil dihapus!")
                break

            elif konfirmasi == "n":
                print("Penghapusan akun dibatalkan")
                break
            else:
                print("Silahkan input (y/n) yang benar")