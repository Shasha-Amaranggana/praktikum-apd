from prettytable import PrettyTable
from data import char_meta, request_meta
from help import pesan_peringatan, pesan_berhasil, next_key
from menu import valid, no_char, inp_update

def read_char():
    global char_meta
    if len(char_meta) == 0:
        print("")
        print(("═"*20).center(70))
        print("Data karakter belum ada".center(70))
        print(("═"*20).center(70))
        print("")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["NO", "   NAMA   ", "ELEMEN", " SENJATA ", "  PERAN  "]
        no = 1
        for nomor, k in char_meta.items():
            tabel.add_row([no, k["nama"], k["elemen"], k["senjata"], k["peran"]])
            no += 1
        output = tabel.get_string()
        for baris in output.splitlines():
            print(baris.center(70))

def create_char():
    global char_meta
    nama = input("                Nama              :          ")
    if nama == "":
        print("──────Kolom harus diisi!──────".center(70))
    elemen = valid("""                Elemen (Pyro/Dendro/Hydro/Electro/Geo/
                Anemo/Cryo)       :          """, "elemen")
    senjata = valid("""                Senjata baru (Catalyst/Claymore/Sword/
                Polearm/Bow)      :          """, "senjata")
    peran = valid("""                Peran baru (Main DPS/Sub DPS/Support)
                                  :          """, "peran")
    if nama == "" or elemen in (None, "Gagal") or senjata in (None, "Gagal") or peran in (None, "Gagal"):
        pesan_peringatan("Pastikan semua kolom diisi dengan benar dan sesuai!", 26)
        return None
    char_meta[next_key(char_meta)] = {"nama": nama, "elemen": elemen, "senjata": senjata, "peran": peran}
    pesan_berhasil(f"Karakter {nama} berhasil ditambahkan!")

def update_char():
    global char_meta
    if len(char_meta) == 0:
        print("")
        print(("═"*40).center(70))
        print("")
        return None
    hasil = no_char("update")
    if hasil:
        data, nomor = hasil
        print("")
        print(f"                Nama              :          {data["nama"]}")
        print(f"                Elemen            :          {data["elemen"]}")
        print(f"                Senjata           :          {data["senjata"]}")
        print(f"                Peran             :          {data["peran"]}")
        print("")
        nama, s1 = inp_update("nama", data)
        elemen, s2 = inp_update("elemen", data) 
        senjata, s3 = inp_update("senjata", data)
        peran, s4 = inp_update("peran", data)
        status = [s1, s2, s3, s4]
        if "Gagal" in status:
            pesan_peringatan("Pastikan semua kolom diisi dengan benar dan sesuai!", 26)
        else:
            semua_false = True
            for s in status:
                if s:
                    semua_false = False
                    break
            if semua_false:
                pesan_peringatan("Tidak ada data yang diubah!", 14)
            else:
                char_meta[nomor] = {"nama": nama, "elemen": elemen, "senjata": senjata, "peran": peran}
                pesan_berhasil("Data berhasil diperbarui!")

def hapus_char():
    global char_meta
    if len(char_meta) == 0:
        print("")
        print(("═"*40).center(70))
        print("")
        return None
    hasil = no_char("hapus")
    if hasil:
        hapus, nomor = hasil
        char_meta.pop(nomor)
        pesan_berhasil(f"Karakter {hapus['nama']} berhasil dihapus!")

def daftar_request():
    global request_meta, char_meta
    if len(request_meta) == 0:
        print("")
        print(("═"*20).center(70))
        print("Data request karakter belum ada".center(70))
        print(("═"*20).center(70))
        print("")
        print("")
        print(("═"*40).center(70))
        print("")
        return None
    else:
        tabel = PrettyTable()
        tabel.field_names = ["NO", "   NAMA   ", "ELEMEN", "SENJATA", "  PERAN  ", "PENGUSUL"]
        no = 1
        for nomor, k in request_meta.items():
            tabel.add_row([no, k["nama"], k["elemen"], k["senjata"], k["peran"], k["pengusul"]])
            no += 1
        output = tabel.get_string()
        for baris in output.splitlines():
            print(baris.center(70))

    hasil = no_char("request")
    if hasil:
        data, nomor = hasil
        print("")
        konfirm = input(f"""╰┈➤  Masukkan jawaban anda atas request karakter '{data['nama']}' dari pengguna
'{data['pengusul']}' [y/n]: """)
        if konfirm == "y":
            char_meta[next_key(char_meta)] = {"nama": data["nama"], "elemen": data["elemen"], "senjata": data["senjata"], "peran": data["peran"]}
            request_meta.pop(nomor)
            pesan_berhasil(f"Request {data['nama']} disetujui dan ditambahkan ke daftar!")
        elif konfirm == "n":
            request_meta.pop(nomor)
            pesan_berhasil(f"Request {data['nama']} ditolak!")
        else:
            pesan_peringatan("Pilihan tidak tersedia!", 15)

def request_char(username):
    global request_meta
    nama = input("                Nama              :          ")
    if nama == "":
        print("──────Kolom harus diisi!──────".center(70))
    elemen = valid("""                Elemen (Pyro/Dendro/Hydro/Electro/Geo/
                Anemo/Cryo)       :          """, "elemen")
    senjata = valid("""                Senjata baru (Catalyst/Claymore/Sword/
                Polearm/Bow)      :          """, "senjata")
    peran = valid("""                Peran baru (Main DPS/Sub DPS/Support)
                                  :          """, "peran")
    if nama == "" or elemen in (None, "Gagal") or senjata in (None, "Gagal") or peran in (None, "Gagal"):
        pesan_peringatan("Pastikan semua kolom diisi dengan benar dan sesuai!", 26)
        return None
    request_meta[next_key(request_meta)] = {
        "nama": nama, "elemen": elemen, "senjata": senjata, "peran": peran, "pengusul": username}
    pesan_berhasil(f"Request anda telah dikirim ke admin!")