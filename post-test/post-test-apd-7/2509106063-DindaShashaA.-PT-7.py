# DATA AWAL AKUN ADMIN & PENGGUNA DAN KARAKTER META
# ════════════════════════════════════════════════════
import os
akun = {
    "1" : {"us" : "admin", "pw" : "admin123", "st" : "admin"}}
char_meta = {
    "1": {"nama": "Mavuika", "elemen": "Pyro", "senjata": "Claymore", "peran": "Main DPS"},
    "2": {"nama": "Neuvillette", "elemen": "Hydro", "senjata": "Catalyst", "peran": "Main DPS"},
    "3": {"nama": "Furina", "elemen": "Hydro", "senjata": "Sword", "peran": "Sub DPS"},
    "4": {"nama": "Xiangling", "elemen": "Pyro", "senjata": "Polearm", "peran": "Sub DPS"},
    "5": {"nama": "Bennet", "elemen": "Pyro", "senjata": "Sword", "peran": "Support"},
    "6": {"nama": "Kazuha", "elemen": "Anemo", "senjata": "Sword", "peran": "Support"}}
valid_esp = {
    "elemen" : ("Pyro", "Cryo", "Electro", "Hydro", "Anemo", "Geo", "Dendro"),
    "senjata" : ("Sword", "Claymore", "Polearm", "Catalyst", "Bow"),
    "peran" : ("Main DPS", "Sub DPS", "Support")}

# FUNGSI & PROSEDUR PROGRAM
# ════════════════════════════════════════════════════
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def jud_utama(): 
    clear()
    print("═"*60)
    print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(60))
    print("═"*60)

def jud_sub(judul):
    print(("═"*40).center(60))
    print(judul.center(60))
    print(("═"*40).center(60))
    print("")

def inp_menu():
    print("")
    print(("═"*50).center(60))
    menu = input("╰┈➤  Pilih menu: ")
    return menu

def inp_nochar():
    print("")
    print(("═"*50).center(60))
    menu = input("╰┈➤  Masukkan nomor karakter yang ingin diupdate: ")
    print("")
    return menu

def pesan_berhasil(pesan):
    print("")
    print(("═"*20).center(60))
    print(pesan.center(60))
    print(("═"*20).center(60))
    print("")

def pesan_peringatan(pesan, jumlah):
    print("")
    print("──" * jumlah)
    print(pesan)
    print("──" * jumlah)
    print("")

def login():
    username = input("Username: ")
    password = input("Password: ")
    try:
        if username == "" or password == "":
            raise ValueError ("Semua kolom harus diisi!")
        for nomor, user in akun.items():
            if user["us"] == username and user["pw"] == password:
                pesan_berhasil(f"Login berhasil! Selamat datang, {username}!")
                input("→ 「 Enter untuk lanjut 」")
                if user["st"] == "admin":
                    return ("menu admin", username)
                return ("menu pengguna", username)
        pesan_peringatan("Username atau Password salah atau akun belum terdaftar!", 27)
        input("→ 「 Enter untuk kembali 」")
        return None
    except ValueError as e:
        pesan_peringatan(str(e), 12)
        input("→ 「 Enter untuk kembali 」")
        return None
    
def register():
    username = input("Username: ")
    password = input("Password: ")
    try:
        if username == "" or password == "":
            raise ValueError ("Semua kolom harus diisi!")
        for nomor, user in akun.items():
            if user["us"] == username:
                raise ValueError ("User sudah ada!")
        akun.update({
            str(len(akun)+1): {
                "us": username,
                "pw": password,
                "st": "pengguna"}
        })
        pesan_berhasil("Registrasi berhasil! Silakan login.") 
        return True
    except ValueError as e:
        pesan_peringatan(str(e), 12)
        return None
    
def valid(pesan, kategori, update = False):
    input_val = input(pesan)
    if input_val == "":
        if update:
            return None
        print("──────Kolom harus diisi!──────")
        return None
    pilihan = valid_esp[kategori]
    if input_val not in pilihan:
        print("──────Sesuaikan besar kecil pilihan yang tersedia!──────")
        return "Gagal"
    return input_val

def no_char(jenis):
    no_char = inp_nochar()
    if not no_char.isdigit():  
        pesan_peringatan("Input harus berupa angka!", 15)
        return None
    no_char = int(no_char)
    if not (1 <= no_char <= len(char_meta)):
        pesan_peringatan("Nomor karakter tidak ditemukan!", 15)
        return None
    nomor = list(char_meta.keys())[no_char - 1]
    if jenis == "update": 
        data = char_meta[nomor]
        return data, nomor
    elif jenis == "hapus":
        hapus = char_meta.pop(nomor)
        return hapus, nomor
    
def inp_update(jenis, data):
    pesan_dict = {
        "elemen": "Elemen baru (Pyro/Cryo/Electro/Hydro/Anemo/Geo/Dendro): ",
        "senjata": "Senjata baru (Sword/Claymore/Polearm/Catalyst/Bow): ",
        "peran": "Peran baru (Main DPS/Sub DPS/Support): "}
    if jenis == "nama":
        baru = input("Nama baru: ")
        if baru == "":
            return data["nama"], False
        return baru, True
    pesan = pesan_dict[jenis]
    baru = valid(pesan, jenis, update = True)
    if baru is None:
        return data[jenis], False
    if baru == "Gagal":
        return data[jenis], "Gagal"
    return baru, True

def read_char():
    global char_meta
    if len(char_meta) == 0:
        pesan_berhasil("Data karakter belum ada.")
    else:
        print("NO   NAMA            ELEMEN     SENJATA      PERAN")
        print("──" * 28)
        no = 1
        for nomor, k in char_meta.items():
            print(no,"| ", k["nama"], " "*(14 - len(k["nama"])), k["elemen"], " "*(9 - len(k["elemen"])), k["senjata"], " "*(11 - len(k["senjata"])), k["peran"])
            no = no + 1

def create_char():
    global char_meta
    nama = input("Nama Karakter: ")
    if nama == "":
        print("──────Kolom harus diisi!──────")
    elemen = valid("Elemen (Pyro/Cryo/Electro/Hydro/Anemo/Geo/Dendro): ", "elemen")
    senjata = valid("Senjata (Sword/Claymore/Polearm/Catalyst/Bow): ", "senjata")
    peran = valid("Peran (Main DPS/Sub DPS/Support): ", "peran")
    if nama == "" or elemen in (None, "Gagal") or senjata in (None, "Gagal") or peran in (None, "Gagal"):
        pesan_peringatan("Pastikan semua kolom diisi dengan benar dan sesuai.", 26)
        return None
    char_meta.update({
        str(len(char_meta)+1): {"nama": nama, "elemen": elemen, "senjata": senjata, "peran": peran}})
    pesan_berhasil(f"Karakter {nama} berhasil ditambahkan!")

def update_char():
    hasil = no_char("update")
    if hasil:
        data, nomor = hasil
        print(f"Nama:", data["nama"])
        print(f"Elemen:", data["elemen"])
        print(f"Senjata:", data["senjata"])
        print(f"Peran:", data["peran"])
        print("")
        nama, s1 = inp_update("nama", data)
        elemen, s2 = inp_update("elemen", data) 
        senjata, s3 = inp_update("senjata", data)
        peran, s4 = inp_update("peran", data)
        status = [s1, s2, s3, s4]
        if "Gagal" in status:
            pesan_peringatan("Pastikan semua kolom diisi dengan benar dan sesuai.", 26)
        elif all(s == False for s in status):
            pesan_peringatan("Tidak ada data yang diubah!", 20)
        else:
            char_meta[nomor] = {"nama": nama, "elemen": elemen, "senjata": senjata, "peran": peran}
            pesan_berhasil("Data Berhasil Diperbarui.")

def hapus_char():
    hasil = no_char("hapus")
    if hasil:
        hapus, nomor = hasil
        pesan_berhasil(f"Karakter {hapus['nama']} berhasil dihapus!")

# PROGRAM UTAMA
# ════════════════════════════════════════════════════
while True:
    jud_utama()
    print("")
    print("1 |  Login")
    print("2 |  Register")
    print("3 |  Keluar")
    pilih = inp_menu()

    # LOGIN
    # ════════════════════════════════════════════════════
    if pilih  == "1":
        jud_utama()
        jud_sub("Login Akun Anda")
        hasil_login = login()
        if hasil_login and hasil_login[0] == "menu admin":
            username = hasil_login[1]
            while True:
                jud_utama()
                jud_sub(f"Halo, Admin {username}") 
                print("1 |  Daftar Karakter")
                print("2 |  Tambah Karakter")
                print("3 |  Update Karakter")
                print("4 |  Hapus Karakter")
                print("5 |  Logout")
                pilih_admin = inp_menu()
                
                # READ
                if pilih_admin == "1":
                    jud_utama()
                    jud_sub("Daftar Karakter Meta")
                    read_char()
                    print("")
                    print("═"*60)
                    input("→ 「 Enter untuk kembali 」")
                # CREATE
                elif pilih_admin == "2":
                    jud_utama()
                    jud_sub("Tambah Karakter Meta")
                    create_char()
                    input("→ 「 Enter untuk kembali 」")
                # UPDATE
                elif pilih_admin == "3":
                    jud_utama()
                    jud_sub("Update Karakter Meta") 
                    read_char()
                    update_char()
                    input("→ 「 Enter untuk kembali 」")
                # DELETE
                elif pilih_admin == "4":
                    jud_utama()
                    jud_sub("Hapus Karakter Meta") 
                    read_char()
                    hapus_char()
                    input("→ 「 Enter untuk kembali 」")

                # Logout Admin
                elif pilih_admin == "5":
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
                print("1 |  Daftar Karakter Meta")
                print("2 |  Logout")
                pilih_user = inp_menu()
                if pilih_user == "1":
                    jud_utama()
                    jud_sub("Daftar Karakter Meta")
                    read_char()
                    print("")
                    print("═"*60)
                    input("→ 「 Enter untuk kembali 」")
                elif pilih_user == "2":
                    pesan_berhasil("Logout berhasil!")
                    input("→ 「 Enter untuk lanjut 」")
                    break
                else:
                    pesan_peringatan("Pilihan menu tidak ditemukan!", 15)
                    input("→ 「 Enter untuk kembali 」")

    # REGISTER
    # ════════════════════════════════════════════════════
    elif pilih == "2":
        jud_utama()
        jud_sub("Registrasi Akun Anda")
        register()
        input("→ 「 Enter untuk kembali 」")

    # KELUAR PROGRAM
    # ════════════════════════════════════════════════════
    elif pilih == "3":
        jud_utama()
        jud_sub("Terima Kasih Telah Datang!")
        break

    # SALAH INPUT YANG AWAL
    # ════════════════════════════════════════════════════
    else:
        pesan_peringatan("Pilihan menu tidak ditemukan!", 15)
        input("→ 「 Enter untuk kembali 」")