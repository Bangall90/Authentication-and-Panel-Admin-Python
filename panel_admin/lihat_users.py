from database import cursor

def lihat_user():
    cursor.execute("SELECT * FROM users")
    semua_user = cursor.fetchall()

    print("=" * 100)
    print(f"{'ID':<5}{'Username':<20}{'Password':<20}")
    print("=" * 100)

    for user in semua_user:
        id, username, password = user
        print(f"{id:<5}{username:<20}{password:<20}")
        print("-" * 100)