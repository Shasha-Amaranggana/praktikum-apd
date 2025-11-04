from help import pesan_berhasil, pesan_peringatan
from data import akun
import re

def login():
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if username == "" or password == "":
            pesan_peringatan("Semua kolom harus diisi!", 12)
            raise ValueError
        for nomor, user in akun.items():
            if user["us"] == username and user["pw"] == password:
                pesan_berhasil(f"Login berhasil! Selamat datang, {username}!")
                input("→ 「 Enter untuk lanjut 」")
                if user["st"] == "admin":
                    return ("menu admin", username)
                else:
                    return ("menu pengguna", username)
        pesan_peringatan("Username atau Password salah atau akun belum terdaftar!", 27)
        raise ValueError
    except ValueError:
        input("→ 「 Enter untuk kembali 」")
        return None
    
def register():
    print("   > Username min 5 karakter, mengandung huruf/angka,")
    print("     tidak mengandung karakter spesial!")
    print("   > Password min 8 karakter, mengandung huruf besar & kecil & angka,")
    print("     tidak mengandung karakter spesial!")
    print("")
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if username == "" or password == "":
            pesan_peringatan("Semua kolom harus diisi!", 12)
            raise ValueError
        elif not re.search(r"^[a-zA-Z0-9]{4,}$", username):
            pesan_peringatan("Sesuaikan dengan syarat yang tersedia", 12)
            raise ValueError
        else:
            pola_pw = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
            if not re.search(pola_pw, password):
                pesan_peringatan("Sesuaikan dengan syarat yang tersedia", 12)
                raise ValueError
            else:
                for nomor, user in akun.items():
                    if user["us"] == username:
                        pesan_peringatan("User telah tersedia", 12)
                        raise ValueError
                akun.update({
                    str(len(akun)+1): {
                        "us": username,
                        "pw": password,
                        "st": "pengguna"}})
                pesan_berhasil("Registrasi berhasil! Silakan login.") 
                input("→ 「 Enter untuk kembali 」")
                return True
    except ValueError:
        input("→ 「 Enter untuk kembali 」")
        return None