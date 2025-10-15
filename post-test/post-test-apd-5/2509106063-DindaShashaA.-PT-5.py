# DATA AWAL AKUN ADMIN & PENGGUNA DAN KARAKTER META
# ════════════════════════════════════════════════════
import os

akun = [
    ["Shasha", "444", "admin"]]

char_meta = [
    ["Mavuika", "Pyro", "Claymore", "Main DPS"],
    ["Neuvillette", "Hydro", "Catalyst", "Main DPS"],

    ["Furina", "Hydro", "Sword", "Sub DPS"],
    ["Xiangling", "Pyro", "Polearm", "Sub DPS"],

    ["Bennet", "Pyro", "Sword", "Support"],
    ["Kazuha", "Anemo", "Sword", "Support"]]


# PROGRAM UTAMA
# ════════════════════════════════════════════════════
while True:
    os.system('cls')
    print("═"*60)
    print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
    print("═"*60)
    print("")
    print("""1 |  Login
2 |  Register
3 |  Keluar""")
    print("")
    print(("═"*50).center(60))
    pilih = input("╰┈➤  Pilih menu: ")

    # LOGIN
    # ════════════════════════════════════════════════════
    if pilih == "1":
        os.system('cls')
        print("═"*60)
        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
        print("═"*60)
        print(("═"*40).center(60))
        print("Login Akun Anda".center(60))
        print(("═"*40).center(60))
        print("")
        username = input("Username: ")
        password = input("Password: ")

        user_ada = 0
        for user in akun:
            if user[0] == username and user[1] == password:
                user_ada = user
                break

        if user_ada:
            print("")
            print(("═"*20).center(60))
            print(f"Login berhasil! Selamat datang, {username}!".center(60))
            print(("═"*20).center(60))
            print("")
            input("→ 「 Enter untuk lanjut 」")

            # MENU ADMIN (CRUD)
            # ════════════════════════════════════════════════════
            if user_ada[2] == "admin":
                while True:
                    os.system('cls')
                    print("═"*60)
                    print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
                    print("═"*60)
                    print(("═" * 40).center(60))
                    print(f"Halo, Admin {username}".center(60))
                    print(("═" * 40).center(60))
                    print("")
                    print("""1 |  Daftar Karakter
2 |  Tambah Karakter
3 |  Update Karakter
4 |  Hapus Karakter
5 |  Logout""")
                    print("")
                    print(("═"*50).center(60))
                    pilih_admin = input("╰┈➤  Pilih menu: ")

                    # READ
                    if pilih_admin == "1":
                        os.system('cls')
                        print("═"*60)
                        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
                        print("═"*60)
                        print(("═" * 40).center(60))
                        print("Daftar Karakter Meta".center(60))
                        print(("═" * 40).center(60))
                        print("")
                        if len(char_meta) == 0:
                            print("")
                            print(("═"*20).center(60))
                            print("Data karakter belum ada.".center(60))
                            print(("═"*20).center(60))
                            print("")
                        else:
                            print("NO   NAMA            ELEMEN     SENJATA      PERAN")
                            print("──" * 28)
                            no = 1
                            for k in char_meta:
                                print(no,"| ", k[0], " "*(14 - len(k[0])), k[1], " "*(9 - len(k[1])), k[2], " "*(11 - len(k[2])), k[3])
                                no = no + 1
                            print("")
                            print(("═"*50).center(60))
                        input("→ 「 Enter untuk kembali 」")

                    # CREATE
                    elif pilih_admin == "2":
                        os.system('cls')
                        print("═"*60)
                        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
                        print("═"*60)
                        print(("═"*40).center(60))
                        print("Tambah Karakter Meta".center(60))
                        print(("═"*40).center(60))                        
                        print("")
                        nama = input("Nama Karakter: ")
                        elemen = input("Elemen (Pyro/Cryo/Electro/Hydro/Anemo/Geo/Dendro): ")
                        senjata = input("Jenis Senjata (Sword/Claymore/Polearm/Catalyst/Bow): ")
                        peran = input("Peran (Main DPS/Sub DPS/Support): ")

                        if nama == "" or elemen == "" or senjata == "" or peran == "":
                            print("")
                            print("──" * 12)
                            print("Semua kolom harus diisi!")
                            print("──" * 12)
                            print("")
                        else:
                            char_meta.append([nama, elemen, senjata, peran])
                            print("")
                            print(("═"*20).center(60))
                            print(f"Karakter {nama} berhasil ditambahkan!".center(60))
                            print(("═"*20).center(60))
                            print("")
                        input("→ 「 Enter untuk kembali 」")

                    # UPDATE
                    elif pilih_admin == "3":
                        os.system('cls')
                        print("═"*60)
                        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
                        print("═"*60)
                        print(("═"*40).center(60))
                        print("Update Karakter Meta".center(60))
                        print(("═"*40).center(60))
                        print("")
                        if len(char_meta) == 0:
                            print("")
                            print(("═"*20).center(60))
                            print("Data karakter belum ada.".center(60))
                            print(("═"*20).center(60))
                            print("")
                            input("→ 「 Enter untuk kembali 」")
                            continue
                        else:
                            print("NO   NAMA            ELEMEN     SENJATA      PERAN")
                            print("──" * 28)
                            no = 1
                            for k in char_meta:
                                print(no,"| ", k[0], " "*(14 - len(k[0])), k[1], " "*(9 - len(k[1])), k[2], " "*(11 - len(k[2])), k[3])
                                no = no + 1
                        print("")
                        print(("═"*50).center(60))

                        nomor = input("╰┈➤  Masukkan nomor karakter yang ingin diupdate: ")
                        print("")
                        if nomor.isdigit():
                            nomor = int(nomor)-1
                            if 0 <= nomor < len(char_meta):
                                nama_baru = input(f"Nama baru ({char_meta[nomor][0]}): ")
                                if nama_baru == "":
                                    nama = char_meta[nomor][0]
                                else:
                                    nama = nama_baru
                                elemen_baru = input(f"Elemen baru ({char_meta[nomor][1]}): ")
                                if elemen_baru == "":
                                    elemen = char_meta[nomor][1]
                                else:
                                    elemen = elemen_baru
                                senjata_baru = input(f"Senjata baru ({char_meta[nomor][2]}): ")
                                if senjata_baru == "":
                                    senjata = char_meta[nomor][2]
                                else:
                                    senjata = senjata_baru
                                peran_baru = input(f"Peran baru ({char_meta[nomor][3]}): ")
                                if peran_baru == "":
                                    peran = char_meta[nomor][3]
                                else:
                                    peran = peran_baru
                                char_meta[nomor] = [nama, elemen, senjata, peran]
                                print("")
                                print(("═"*20).center(60))
                                print("Data berhasil diperbarui!".center(60))
                                print(("═"*20).center(60))
                                print("")
                            else:
                                print("")
                                print("──" * 15)
                                print("Nomor karakter tidak ditemukan!")
                                print("──" * 15)
                                print("")
                        else:
                            print("")
                            print("──" * 17)
                            print("Input harus diisi dan berupa angka!")
                            print("──" * 17)
                            print("")
                        input("→ 「 Enter untuk kembali 」")

                    # DELETE
                    elif pilih_admin == "4":
                        os.system('cls')
                        print("═"*60)
                        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
                        print("═"*60)
                        print(("═"*40).center(60))
                        print("Hapus Karakter Meta".center(60))
                        print(("═"*40).center(60))
                        print("")
                        if len(char_meta) == 0:
                            print("")
                            print(("═"*20).center(60))
                            print("Data karakter belum ada.".center(60))
                            print(("═"*20).center(60))
                            print("")
                            input("→ 「 Enter untuk kembali 」")
                            continue
                        else:
                            print("NO   NAMA            ELEMEN     SENJATA      PERAN")
                            print("──" * 28)
                            no = 1
                            for k in char_meta:
                                print(no,"| ", k[0], " "*(14 - len(k[0])), k[1], " "*(9 - len(k[1])), k[2], " "*(11 - len(k[2])), k[3])
                                no = no + 1
                        print("")
                        print(("═"*50).center(60))

                        nomor = input("╰┈➤  Masukkan nomor karakter yang ingin dihapus: ")
                        print("")
                        if nomor.isdigit():
                            nomor = int(nomor) - 1
                            if 0 <= nomor < len(char_meta):
                                hapus = char_meta.pop(nomor)
                                print("")
                                print(("═"*20).center(60))
                                print(f"Karakter {hapus[0]} berhasil dihapus!".center(60))
                                print(("═"*20).center(60))
                                print("")
                            else:
                                print("")
                                print("──" * 15)
                                print("Nomor karakter tidak ditemukan!")
                                print("──" * 15)
                                print("")
                        else:
                            print("")
                            print("──" * 17)
                            print("Input harus diisi dan berupa angka!")
                            print("──" * 17)
                            print("")
                        input("→ 「 Enter untuk kembali 」")

                    # Logout admin
                    elif pilih_admin == "5":
                        print("")
                        print(("═"*20).center(60))
                        print("Logout berhasil!".center(60))
                        print(("═"*20).center(60))
                        print("")
                        input("→ (Enter untuk lanjut)")
                        break

                    else:
                        print("")
                        print("──" * 15)
                        print("Pilihan menu tidak tersedia!")
                        print("──" * 15)
                        print("")
                        input("→ (Enter untuk kembali)")

            # MENU PENGGUNA
            # ════════════════════════════════════════════════════
            else:
                while True:
                    os.system('cls')
                    print("═"*60)
                    print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
                    print("═"*60)
                    print(("═" * 40).center(60))
                    print(f"Halo, {username}".center(60))
                    print(("═" * 40).center(60))
                    print("")
                    print("1 |  Daftar Karakter Meta")
                    print("2 |  Logout")
                    print("")
                    print(("═"*50).center(60))
                    pilih_user = input("╰┈➤  Pilih menu: ")

                    if pilih_user == "1":
                        os.system('cls')
                        print("═"*60)
                        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
                        print("═"*60)
                        print(("═" * 40).center(60))
                        print(f"Daftar Karakter Meta".center(60))
                        print(("═" * 40).center(60))
                        print("")
                        if len(char_meta) == 0:
                            print("")
                            print(("═"*20).center(60))
                            print("Data karakter belum ada.".center(60))
                            print(("═"*20).center(60))
                            print("")
                        else:
                            print("NO   NAMA            ELEMEN     SENJATA      PERAN")
                            print("──" * 28)
                            no = 1
                            for k in char_meta:
                                print(no,"| ", k[0], " "*(14 - len(k[0])), k[1], " "*(9 - len(k[1])), k[2], " "*(11 - len(k[2])), k[3])
                                no = no + 1
                        print("")
                        print(("═"*50).center(60))
                        input("→ 「 Enter untuk kembali 」")

                    elif pilih_user == "2":
                        print("")
                        print(("═"*20).center(60))
                        print("Logout berhasil!".center(60))
                        print(("═"*20).center(60))
                        print("")
                        input("→ (Enter untuk lanjut)")
                        break

                    else:
                        print("")
                        print("──" * 15)
                        print("Pilihan menu tidak tersedia!")
                        print("──" * 15)
                        print("")
                        input("→ (Enter untuk kembali)")

        elif username == "" or password == "":
            print("")
            print("──" * 12)
            print("Semua kolom harus diisi!")
            print("──" * 12)
            print("")
            input("→ 「 Enter untuk kembali 」")

        else:
            print("")
            print("──" * 27)
            print("Username atau Password salah atau akun belum terdaftar!")
            print("──" * 27)
            print("")
            input("→ 「 Enter untuk kembali 」")

    # REGISTER
    # ════════════════════════════════════════════════════
    elif pilih == "2":
        os.system('cls')
        print("═"*60)
        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
        print("═"*60)
        print(("═" * 40).center(60))
        print("Registrasi Akun Anda".center(60))
        print(("═" * 40).center(60))
        print("")
        username = input("Buat Username: ")
        password = input("Buat Password: ")

        if username == "" or password == "":
            print("")
            print("──" * 12)
            print("Semua kolom harus diisi!")
            print("──" * 12)
            print("")
        else:
            user_ada = 0
            for user in akun:
                if user[0] == username:
                    user_ada = user
                    break
            if user_ada:
                print("")
                print("──" * 12)
                print("Username sudah ada!")
                print("──" * 12)
                print("")
            else:
                akun.append([username, password, "pengguna"])
                print("")
                print(("═"*20).center(60))
                print("Registrasi berhasil! Silakan login.".center(60))
                print(("═"*20).center(60))
                print("")
        input("→ 「 Enter untuk kembali 」")

    # KELUAR PROGRAM
    # ════════════════════════════════════════════════════
    elif pilih == "3":
        os.system('cls')
        print("═"*60)
        print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
        print("═"*60)
        print(("═" * 40).center(60))
        print("Terima Kasih Telah Datang!".center(60))
        print(("═" * 40).center(60))
        print("")
        break

    # SALAH INPUT YANG AWAL
    # ════════════════════════════════════════════════════
    else:
        print("")
        print("──" * 14)
        print("Pilihan menu tidak tersedia!")
        print("──" * 14)
        print("")
        input("→ 「 Enter untuk kembali 」")

