

print("═"*60)

def pesan_halo():
    print("sing sabar")
    print("jan ngamok")
pesan_halo()

print("═"*60)

def kali():
    X = 5*5
    print(X)
kali()

print("═"*60)

def luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    print ("luas persegi panjang adalah",luas)
luas_segitiga(10, 5)

print("═"*60)

def luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    return luas
print ("luas persegi panjang adalah",luas_segitiga(10, 5))

print("═"*60)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
def volume_kubus(sisi):
    volume_kubus = luas_persegi(sisi) * sisi
    print("volume kubus adalah", volume_kubus)
volume_kubus(5)

print("═"*60)

#Variabel global & lokal
x = 10
y = 5
def hitung():
    x = 2
    y = 3
    print("Si x", x)
    print("Si y", y)
print("Si x", x)
print("Si y", y)
hitung()

print("═"*60)

def faktorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * faktorial(n - 1)
hasil = faktorial(5)
print(f"Hasil dari 5! adalah: {hasil}")

