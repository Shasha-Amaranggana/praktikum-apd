username = "Shasha"
password = "063"
print("Silakan login ke akun Anda.")
input_un = input("Masukkan username: ")
input_pw = input("Masukkan password: ")

if input_un == username and input_pw == password:
    print("Login berhasil!")

    # Kalkulator
    jenis = input("Ingin mengonversikan apa? (Panjang/Massa/Suhu/Waktu/Mata Uang): ")

    # Konversi Panjang
    if jenis == "Panjang":
        satuan = input("Satuan apa yang ingin dikonversikan ke Meter? (Kaki/Kilometer/Centimeter): ")
        if satuan== "Kaki":
            nilai = float(input("Masukkan nilai dalam kaki: "))
            hasil = nilai * 0.3048
            print(str(nilai) + " ft = " + str(hasil) + " m")
        elif satuan == "Kilometer":
            nilai = float(input("Masukkan nilai dalam kilometer: "))
            hasil = nilai * 1000
            print(str(nilai) + " km = " + str(hasil) + " m")
        elif satuan == "Centimeter":
            nilai = float(input("Masukkan nilai dalam centimeter: "))
            hasil = nilai * 0.01
            print(str(nilai) + " cm = " + str(hasil) + " m")
        else:
            print("Jenis satuan tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")


    # Konversi Massa
    elif jenis == "Massa":
        satuan = input("Satuan apa yang ingin dikonversikan ke Kilogram? (Pon/Ton/Gram/Ons/Kwintal): ")
        if satuan == "Pon":
            nilai = float(input("Masukkan nilai dalam pon: "))
            hasil = nilai * 0.454
            print(str(nilai) + " lb = " + str(hasil) + " kg")
        elif satuan == "Ton":
            nilai = float(input("Masukkan nilai dalam ton: "))
            hasil = nilai * 1000
            print(str(nilai) + " ton = " + str(hasil) + " kg")
        elif satuan == "Gram":
            nilai = float(input("Masukkan nilai dalam gram: "))
            hasil = nilai * 0.001  
            print(str(nilai) + " g = " + str(hasil) + " kg")
        elif satuan == "Ons":
            nilai = float(input("Masukkan nilai dalam ons: "))
            hasil = nilai * 0.1
            print(str(nilai) + " ons = " + str(hasil) + " kg")
        elif satuan == "Kwintal": 
            nilai = float(input("Masukkan nilai dalam kwintal: "))
            hasil = nilai * 100
            print(str(nilai) + " kwintal = " + str(hasil) + " kg")
        else:
            print("Jenis satuan tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")

    # Konversi Suhu
    elif jenis == "Suhu":
        satuan = input("Satuan apa yang ingin dikonversikan ke Kelvin? (Celcius/Fahrenheit/Reamur): ")
        if satuan == "Celcius":
            nilai = float(input("Masukkan nilai dalam celcius: "))
            hasil = nilai + 273.15
            print(str(nilai) + "° C = " + str(hasil) + "° K")
        elif satuan == "Fahrenheit":
            nilai = float(input("Masukkan nilai dalam fahrenheit: "))
            hasil = 5/9 * (nilai - 32) + 273.15
            print(str(nilai) + "° F = " + str(hasil) + "° K")
        elif satuan == "Reamur":
            nilai = float(input("Masukkan nilai dalam reamur: "))
            hasil = (5/4 * nilai) + 273.15
            print(str(nilai) + "° R = " + str(hasil) + "° K")
        else:
            print("Jenis satuan tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")
    
    # Konversi Waktu
    elif jenis == "Waktu":
        satuan = input("Satuan apa yang ingin dikonversikan ke Detik? (Menit/Jam): ")
        if satuan == "Menit":
            nilai = float(input("Masukkan nilai dalam menit: "))
            hasil = nilai * 60
            print(str(nilai) + " menit = " + str(hasil) + " detik")
        elif satuan == "Jam":
            nilai = float(input("Masukkan nilai dalam jam: "))
            hasil = nilai * 3600
            print(str(nilai) + " jam = " + str(hasil) + " detik")
        else:
            print("Jenis satuan tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")

    # Konversi Mata Uang
    elif jenis == "Mata Uang":
        print("""1. Yen <-> Rupiah
2. Yuan <-> Rupiah
3. Yen <-> Yuan""")
        satuan = input("Konversi mata uang apa yang ingin Anda gunakan? (1/2/3): ")
        # Yen <-> Rupiah
        if satuan == "1":
            yen_rupiah = input("Ingin mengonversikan Yen ke Rupiah atau Rupiah ke Yen? (1/2): ")
            if yen_rupiah == "1":
                nilai = float(input("Masukkan nilai dalam Yen: "))
                hasil = nilai * 111.55
                print("JPY ¥" + str(nilai) + " = Rp" + str(hasil))
            elif yen_rupiah == "2":
                nilai = float(input("Masukkan nilai dalam Rupiah: "))
                hasil = nilai / 111.55
                print("Rp" + str(nilai) + " = JPY ¥" + str(hasil))
            else:
                print("Jenis konversi tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")
        # Yuan <-> Rupiah
        elif satuan == "2":
            yuan_rupiah = input("Ingin mengonversikan Yuan ke Rupiah atau Rupiah ke Yuan? (1/2): ")
            if yuan_rupiah == "1":
                nilai = float(input("Masukkan nilai dalam Yuan: "))
                hasil = nilai * 2337.90
                print("CNY ¥" + str(nilai) + " = Rp" + str(hasil))
            elif yuan_rupiah == "2":
                nilai = float(input("Masukkan nilai dalam Rupiah: "))
                hasil = nilai / 2337.90
                print("Rp" + str(nilai) + " = CNY ¥" + str(hasil))
            else:
                print("Jenis konversi tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")
        # Yen <-> Yuan
        elif satuan == "3":
            yen_yuan = input("Ingin mengonversikan Yen ke Yuan atau Yuan ke Yen? (1/2): ")
            if yen_yuan == "1":
                nilai = float(input("Masukkan nilai dalam Yen: "))
                hasil = nilai * 0.048
                print("JPY ¥" + str(nilai) + " = CNY ¥" + str(hasil))
            elif yen_yuan == "2":
                nilai = float(input("Masukkan nilai dalam Yuan: "))
                hasil = nilai / 0.048
                print("CNY ¥" + str(nilai) + " = JPY ¥" + str(hasil))
            else:
                print("Jenis konversi tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")     

        else:
            print("Jenis konversi tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")   

    # Salah ketik/konversi tidak tersedia
    else:
        print("Jenis konversi tidak tersedia atau salah ketik. Ejaan harus sesuai termasuk besar kecil huruf. Silakan coba lagi.")

elif input_un != username and input_pw == password:
    print("Login gagal! Username Anda salah.")

elif input_un == username and input_pw != password:
    print("Login gagal! Password Anda salah.")

else:
    print("Login gagal! Username dan password Anda salah.")

