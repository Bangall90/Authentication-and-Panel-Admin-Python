# Authentication and Panel Admin Python
Aplikasi CLI (command-line) berbasis Python untuk sistem **registrasi & login user**, lengkap dengan **panel admin** untuk mengelola data user. Data disimpan menggunakan **SQLite**.

## Fitur

### Menu Utama
- **Login** — user login dengan username & password (maks. 5 kali percobaan)
- **Register** — pendaftaran akun user baru
- **Admin** — login admin untuk mengakses panel admin
- **Keluar** — keluar dari aplikasi

### Panel Admin
Setelah admin berhasil login, tersedia menu:
- **Lihat Semua User** — menampilkan seluruh data user
- **Cari User** — mencari user berdasarkan ID & username
- **Edit Password User** — mengubah password user berdasarkan ID
- **Hapus User** — menghapus user berdasarkan ID (dengan konfirmasi)
- **Keluar** — kembali ke menu utama

## Struktur Project

```
Authentication and Panel Admin Python/
├── main.py                      # Entry point aplikasi
├── database.py                  # Koneksi & inisialisasi database SQLite
├── users.db                     # File database SQLite (dibuat otomatis saat pertama dijalankan)
├── auth/
│   ├── login_users.py           # Login untuk user
│   ├── login_admin.py           # Login untuk admin
│   └── registrasi_users.py      # Registrasi akun user baru
└── panel_admin/
    ├── dashboard_admin.py       # Menu utama panel admin
    ├── lihat_users.py           # Menampilkan semua user
    ├── cari_users.py            # Mencari user
    ├── edit_password_users.py   # Edit password user
    └── hapus_users.py           # Hapus user
```

> **Catatan:** Berdasarkan statement import di `main.py` dan `dashboard_admin.py`, file-file auth harus berada dalam folder `auth/` dan file-file panel admin harus berada dalam folder `panel_admin/` (masing-masing dengan file `__init__.py` kosong agar dikenali sebagai package Python).

## Teknologi yang Digunakan

- **Python 3**
- **SQLite3** (`sqlite3` — bawaan Python)
- **hashlib** (SHA-256) untuk hashing password user

## Instalasi & Menjalankan

1. Pastikan Python 3 sudah terinstall.
2. Susun folder project sesuai struktur di atas, lalu tambahkan file `auth/__init__.py` dan `panel_admin/__init__.py` (boleh kosong).
3. Jalankan aplikasi dari root folder:

```bash
python main.py
```

4. Database `users.db` akan otomatis dibuat saat aplikasi pertama kali dijalankan.

## Cara Penggunaan

1. Pilih `2` untuk **REGISTER** dan buat akun baru (username & password).
2. Pilih `1` untuk **LOGIN** menggunakan akun yang sudah didaftarkan.
3. Pilih `3` untuk **ADMIN** dan masuk menggunakan salah satu akun admin berikut:

   | Username | Password       |
   |----------|----------------|
   | ryuuo    | admin123       |
   | budi     | budi01gaming   |

4. Setelah login admin berhasil, panel admin akan terbuka untuk mengelola data user.
5. Pilih `4` di menu utama untuk keluar dari aplikasi.

## Catatan Keamanan (untuk pengembangan lebih lanjut)

Beberapa hal yang bisa ditingkatkan bila project ini dikembangkan lebih serius:
- **Password admin** saat ini disimpan langsung sebagai *plain text* di dalam kode — sebaiknya dihash seperti password user, atau disimpan di file/environment variable terpisah, bukan hardcoded.
- Password admin di-*lowercase* saat pengecekan (`.lower()`), yang bisa membuat login admin case-insensitive secara tidak sengaja.
- Tidak ada validasi panjang/kompleksitas password saat registrasi user.
- Koneksi database (`conn`, `cursor`) dibuka secara global di `database.py`, sehingga ada baiknya ditutup dengan benar (`conn.close()`) saat aplikasi keluar.

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and even use this software for commercial purposes, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software.

This project is provided **"as is"**, without any warranty of any kind. See the `LICENSE` file for more details.

Project ini bebas digunakan dan dimodifikasi untuk keperluan belajar.
