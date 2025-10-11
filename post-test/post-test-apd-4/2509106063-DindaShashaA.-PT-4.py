print("│││             FORM LOGIN             │││")

username = "Shasha"
password = "063"
print()
print("Silakan login ke akun Anda.")

while True:
    input_un = input("Masukkan Username: ")
    input_pw = input("Masukkan Password: ")
    if input_un == username and input_pw == password:
        print(f"Login berhasil! Selamat datang {username}!")
        break
    elif input_un == "" or input_pw == "":
        print("Login gagal! Username dan Password Anda tidak boleh kosong. Silakan coba lagi.")
    elif input_un != username and input_pw == password:
        print("Login gagal! Username Anda tidak diketahui. Silakan coba lagi.")
    elif input_un == username and input_pw != password:
        print("Login gagal! Password Anda tidak sesuai. Silakan coba lagi.")
    else:
        print("Login gagal! Username dan Password Anda tidak diketahui. Silakan coba lagi.")

print("")
print(47*"-")
print("│││       INPUT DATA DARAH DONOR       │││")
print("")

A_pos = 0
A_neg = 0
B_pos = 0
B_neg = 0
Ab_pos = 0
Ab_neg = 0
O_pos = 0
O_neg = 0
jawab = "Ya"

while (jawab == "Ya"): 

    while True:
        jenis_goldar = input("Masukkan jenis golongan darah (A, B, AB, O): ")

        # Jika A
        if jenis_goldar == "A":
            while True:
                jenis_rhesus = input("Masukkan jenis Rhesus (+ / -): ")
                if jenis_rhesus == "+":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    A_pos += konversi_volume
                    break
                elif jenis_rhesus == "-":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    A_neg += konversi_volume
                    break
                elif jenis_rhesus == "":
                    print("Rhesus tidak boleh kosong! Isi ulang.")
                else:
                    print("Rhesus tidak diketahui! Isi ulang.")
            break

        # Jika B
        elif jenis_goldar == "B":
            while True:
                jenis_rhesus = input("Masukkan jenis Rhesus (+ / -): ")
                if jenis_rhesus == "+":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    B_pos += konversi_volume
                    break
                elif jenis_rhesus == "-":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    B_neg += konversi_volume
                    break
                elif jenis_rhesus == "":
                    print("Rhesus tidak boleh kosong! Isi ulang.")
                else:
                    print("Rhesus tidak diketahui! Isi ulang.")
            break

        # Jika AB
        elif jenis_goldar == "AB":
            while True:
                jenis_rhesus = input("Masukkan jenis Rhesus (+ / -): ")
                if jenis_rhesus == "+":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    Ab_pos += konversi_volume
                    break
                elif jenis_rhesus == "-":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    Ab_neg += konversi_volume
                    break
                elif jenis_rhesus == "":
                    print("Rhesus tidak boleh kosong! Isi ulang.")
                else:
                    print("Rhesus tidak diketahui! Isi ulang.")
            break

        # Jika O
        elif jenis_goldar == "O":
            while True:
                jenis_rhesus = input("Masukkan jenis Rhesus (+ / -): ")
                if jenis_rhesus == "+":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    O_pos += konversi_volume
                    break
                elif jenis_rhesus == "-":
                    jumlah_kantong = int(input("Masukkan jumlah kantong darah: "))
                    konversi_volume = jumlah_kantong * 500
                    O_neg += konversi_volume
                    break
                elif jenis_rhesus == "":
                    print("Rhesus tidak boleh kosong! Isi ulang.")
                else:
                    print("Rhesus tidak diketahui! Isi ulang.")
            break

        elif jenis_goldar == "":
            print("Golongan darah tidak boleh kosong! Isi ulang.")
        else:
            print("Golongan darah tidak diketahui! Isi ulang.")

    while True:
        print("Apakah Anda masih mau input lagi?  (Ya / Tidak)")
        jawab = input(": ")
        if jawab == "Ya" or jawab == "Tidak":
            break
        elif jawab == "":
            print("Jawaban tidak boleh kosong! Isi ulang.")
        else:
            print("Jawaban tidak tersedia! Isi ulang.")
    

print("")
print(47*"-")
print("│││  DAFTAR HASIL DARAH YANG TERKUMPUL │││")
print("")

print(f"• Golongan A+ = {A_pos}ml")
print(f"• Golongan A- = {A_neg}ml")
print(f"• Golongan B+ = {B_pos}ml")
print(f"• Golongan B- = {B_neg}ml")
print(f"• Golongan AB+ = {Ab_pos}ml")
print(f"• Golongan AB- = {Ab_neg}ml")
print(f"• Golongan O+ = {O_pos}ml")
print(f"• Golongan O- = {O_neg}ml")

print("")
print(f"Terima kasih atas bantuannya, {username}!")