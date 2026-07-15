from auth.registrasi_users import registrasi_user
from auth.login_users import login_user
from auth.login_admin import login_admin
from panel_admin.dashboard_admin import menu_dashboard

batas_percobaan_login = 5

while True:
    print("=" * 50)
    print("SELAMAT DATANG DI RYUUO STORE")
    print("=" * 50)

    print("1. LOGIN \n2. REGISTER \n3. ADMIN \n4. KELUAR")
    pilihan = int(input("Silahkan Input 1/2/3/4 untuk Menjalankan Menu: "))

    print("-" * 50)

    if pilihan == 1:

        if batas_percobaan_login == 0:
            print("\nAnda tidak bisa lagi menjalankan sistem login silahkan keluar dari menu")
        else:
            while batas_percobaan_login > 0:
                berhasil = login_user()

                if berhasil:
                    print("\nlogin anda berhasil")
                    break
                else:
                    print("\nLogin anda gagal, silahkan coba lagi!")
                    batas_percobaan_login -= 1
                    print(f"\nPercobaan login anda sisa: {batas_percobaan_login}")

                if batas_percobaan_login == 0:
                    print("\nPercobaan login sudah habis!")

    elif pilihan == 2:
        registrasi_user()
    elif pilihan == 3:
        
        if batas_percobaan_login == 0:
            print("\nAnda tidak bisa lagi menjalankan sistem login silahkan keluar dari menu")
        else:
            while batas_percobaan_login > 0:
                berhasil = login_admin()

                if berhasil:
                    print(f"\nlogin anda berhasil")
                    menu_dashboard()
                    break
                else:
                    print("\nLogin anda gagal, silahkan coba lagi!")
                    batas_percobaan_login -= 1
                    print(f"\nPercobaan login anda sisa: {batas_percobaan_login}")

                if batas_percobaan_login == 0:
                    print("\nPercobaan login sudah habis!")

    elif pilihan == 4:
        break
    else:
        print("Input tidak valid")