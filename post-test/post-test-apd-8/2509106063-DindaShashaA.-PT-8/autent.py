from help import pesan_berhasil, pesan_peringatan
from data import akun

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
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if len(username) <= 4 or len(password) <= 4:
            pesan_peringatan("Username atau password harus lebih dari 4 karakter!", 20)
            raise ValueError
        if username == "" or password == "":
            pesan_peringatan("Semua kolom harus diisi!", 12)
            raise ValueError
        for nomor, user in akun.items():
            if user["us"] == username:
                pesan_peringatan("User sudah tersedia!", 10)
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