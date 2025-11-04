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

def next_key(dict):
    if not dict:
        return "1"
    nums = []
    for k in dict.keys():
        if k.isdigit():
            nums.append(int(k))
    if not nums:
        return "1"
    return str(max(nums) + 1)