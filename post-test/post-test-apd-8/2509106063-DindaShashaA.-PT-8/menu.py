import inquirer
from data import char_meta, valid_esp, request_meta
from help import pesan_peringatan

def tamp_menu(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "awal": ['1 │ LOGIN'.center(33), '2 │ REGISTER'.center(35), '3 │ KELUAR'.center(33)],
        "admin": ['1 │ DAFTAR KARAKTER'.center(43), '2 │ TAMBAH KARAKTER'.center(43), '3 │ UPDATE KARAKTER'.center(43),
            '4 │ HAPUS KARAKTER'.center(42), '5 │ DAFTAR REQUEST KARAKTER'.center(51), '6 │ LOGOUT'.center(33)],
        "pengguna": ['1 │ DAFTAR KARAKTER'.center(43), '2 │ REQUEST KARAKTER'.center(44), '3 │ LOGOUT'.center(33)]}
    choices = daftar_menu[jenis] 
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan 

def valid(pesan, kategori, update = False):
    input_val = input(pesan.center(30))
    if input_val == "":
        if update:
            return None
        print("──────Kolom harus diisi!──────".center(70))
        return None
    k = valid_esp[kategori]
    if input_val not in k:
        print("──────Sesuaikan besar kecil pilihan yang tersedia!──────".center(70))
        return "Gagal"
    return input_val

def no_char(jenis):
    global char_meta, request_meta
    print("")
    print(("═"*20).center(70))
    nom = input("╰┈➤  Masukkan nomor karakter yang ingin dipilih: ")
    if not nom.isdigit():  
        pesan_peringatan("Input harus berupa angka!", 15)
        return None
    nom = int(nom)
    if jenis == "request":
        if not (1 <= nom <= len(request_meta)):
            pesan_peringatan("Nomor karakter tidak ditemukan!", 15)
            return None
        nomor = list(request_meta.keys())[nom - 1]
        data = request_meta[nomor]
        return data, nomor
    else:
        if not (1 <= nom <= len(char_meta)):
            pesan_peringatan("Nomor karakter tidak ditemukan!", 15)
            return None
        nomor = list(char_meta.keys())[nom - 1]
        if jenis == "update": 
            data = char_meta[nomor]
            return data, nomor
        if jenis == "hapus":
            hapus = char_meta.pop(nomor)
            return hapus, nomor
    
def inp_update(jenis, data):
    pesan_dict = {
        "elemen": """                Elemen baru (Pyro/Cryo/Hydro/Geo/Anemo/
                Electro/Dendro)   :          """,       
        "senjata": """                Senjata baru (Catalyst/Claymore/Sword/
                Polearm/Bow)      :          """,
        "peran": """                Peran baru (Main DPS/Sub DPS/Support)
                                  :          """}
    if jenis == "nama":
        baru = input("                Nama baru         :          ")
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