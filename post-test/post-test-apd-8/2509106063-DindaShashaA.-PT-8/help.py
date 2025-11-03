import os

def jud_utama(): 
    os.system('cls' if os.name == 'nt' else 'clear')
    print("═"*70)
    print("DAFTAR META TERBAIK KARAKTER GENSHIN IMPACT".center(70))
    print("═"*70)

def jud_sub(judul):
    print(("═"*40).center(70))
    print(judul.center(70))
    print(("═"*40).center(70))
    print("")

def pesan_berhasil(pesan):
    print("")
    print(("═"*20).center(70))
    print(pesan.center(70))
    print(("═"*20).center(70))
    print(("═"*40).center(70))
    print("")

def pesan_peringatan(pesan, jumlah):
    print("")
    print(("──" * jumlah).center(70))
    print((pesan).center(70)    )
    print(("──" * jumlah).center(70))
    print(("═" * 40).center(70))
    print("")