from panel_admin.lihat_users import lihat_user
from panel_admin.cari_users import cari_user
from panel_admin.edit_password_users import edit_password_user
from panel_admin.hapus_users import hapus_user

def menu_dashboard():
    while True:
        print("\n")
        print("="*20, "PANEL ADMIN", "="*20)
        print("1. Lihat Semua User \n2. Cari User \n3. Edit Password User \n4. Hapus User \n5. Keluar")

        pilihan_menu_admin = int(input("Silahkan Silahkan Input 1/2/3/4/5 untuk Menjalankan Menu: "))

        if pilihan_menu_admin == 1:
            lihat_user()
        elif pilihan_menu_admin == 2:
            cari_user()
        elif pilihan_menu_admin == 3:
            edit_password_user()
        elif pilihan_menu_admin == 4:
            hapus_user()
        elif pilihan_menu_admin == 5:
            break
        else:
            print("Input tidak valid")