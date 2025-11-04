# IMPORT FILE
# ════════════════════════════════════════════════════
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from autent import login, register
from menu import tamp_menu
from crud import read_char, create_char, update_char, hapus_char, daftar_request, request_char

# PROGRAM UTAMA
# ════════════════════════════════════════════════════
while True:
    jud_utama() 
    jud_sub("Selamat Datang")
    print("")
    pilih = tamp_menu("awal")

    # LOGIN
    # ════════════════════════════════════════════════════
    if pilih  == "1 │ LOGIN":
        jud_utama()
        jud_sub("Login Akun Anda")
        hasil_login = login()

        # MENU ADMIN
        # ════════════════════════════════════════════════════
        if hasil_login and hasil_login[0] == "menu admin":
            username = hasil_login[1]
            while True:
                jud_utama()
                jud_sub(f"Halo, Admin {username}") 
                pilih_admin = tamp_menu("admin")
                
                # READ
                if pilih_admin == "1 │ DAFTAR KARAKTER":
                    jud_utama()
                    jud_sub("Daftar Karakter Meta")
                    read_char()
                    print("")
                    print(("═"*40).center(70))
                    print("")
                    input("→ 「 Enter untuk kembali 」")
                # CREATE
                elif pilih_admin == "2 │ TAMBAH KARAKTER":
                    jud_utama()
                    jud_sub("Tambah Karakter Meta")
                    create_char()
                    input("→ 「 Enter untuk kembali 」")
                # UPDATE
                elif pilih_admin == "3 │ UPDATE KARAKTER":
                    jud_utama()
                    jud_sub("Update Karakter Meta") 
                    read_char()
                    update_char()
                    input("→ 「 Enter untuk kembali 」")
                # DELETE
                elif pilih_admin == "4 │ HAPUS KARAKTER":
                    jud_utama()
                    jud_sub("Hapus Karakter Meta") 
                    read_char()
                    hapus_char()
                    input("→ 「 Enter untuk kembali 」")
                # REQUEST
                elif pilih_admin == "5 │ DAFTAR REQUEST KARAKTER":
                    jud_utama()
                    jud_sub("Request Karakter Meta") 
                    daftar_request()
                    input("→ 「 Enter untuk kembali 」")

                # Logout Admin
                elif pilih_admin == "6 │ LOGOUT":
                    pesan_berhasil("Logout berhasil!")
                    input("→ 「 Enter untuk lanjut 」")
                    break
                else:
                    pesan_peringatan("Pilihan menu tidak ditemukan!", 15)
                    input("→ 「 Enter untuk kembali 」")

        # MENU PENGGUNA
        # ════════════════════════════════════════════════════
        elif hasil_login and hasil_login[0] == "menu pengguna":
            username = hasil_login[1]
            while True:
                jud_utama()
                jud_sub(f"Halo, {username}") 
                pilih_user = tamp_menu("pengguna")
                if pilih_user == "1 │ DAFTAR KARAKTER":
                    jud_utama()
                    jud_sub("Daftar Karakter Meta")
                    read_char()
                    print("")
                    print(("═"*40).center(70))
                    print("")
                    input("→ 「 Enter untuk kembali 」")
                elif pilih_user == "2 │ REQUEST KARAKTER":
                    jud_utama()
                    jud_sub("Request Karakter Meta")
                    request_char(username)
                    input("→ 「 Enter untuk kembali 」")
                elif pilih_user == "3 │ LOGOUT":
                    pesan_berhasil("Logout berhasil!")
                    input("→ 「 Enter untuk lanjut 」")
                    break
                else:
                    pesan_peringatan("Pilihan menu tidak ditemukan!", 15)
                    input("→ 「 Enter untuk kembali 」")

    # REGISTER
    # ════════════════════════════════════════════════════
    elif pilih == "2 │ REGISTER":
        jud_utama()
        jud_sub("Registrasi Akun Anda")
        register()

    # KELUAR PROGRAM
    # ════════════════════════════════════════════════════
    elif pilih == "3 │ KELUAR":
        jud_utama()
        jud_sub("Terima Kasih Telah Datang!")
        break

    # SALAH INPUT YANG AWAL
    # ════════════════════════════════════════════════════
    else:
        pesan_peringatan("Pilihan menu tidak ditemukan!", 15)
        input("→ 「 Enter untuk kembali 」")