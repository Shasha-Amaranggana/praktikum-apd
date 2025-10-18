# # SET & DICTIONARY (PERTEMUAN 6: APD)

# # ===================================
# # SET
# # ===================================

# # SET tidak bisa duplikat saat di-print
# maem = {"nasgor", "telor", "mie", "bakso", "bakso"}
# print(maem)
#     # munculnya = {'nasgor', 'telor', 'mie', 'bakso'}

# # SET tidak bisa sama urutannya setiap running-an
# maem = {"nasgor", "telor", "mie", "bakso", "bakso"}
# print(maem)
#     # munculnya = {'nasgor', 'telor', 'mie', 'bakso'}
#     # munculnya = {'mie', 'nasgor', 'bakso', 'telor'}
#     # munculnya = {'bakso', 'mie', 'nasgor', 'telor'}

# # SET : add
# maem = {"nasgor", "telor", "mie", "bakso", "bakso"}
# maem.add("mie ayam")
# print(maem)
#     # munculnya = {'nasgor', 'telor', 'mie ayam', 'bakso', 'mie'}

# # SET : remove
# maem = {"nasgor", "telor", "mie", "bakso", "bakso"}
# maem.remove("nasgor")
# print(maem)
#     # munculnya = {'mie', 'telor', 'bakso'}
#     # kalo kita hapus yang tidak ada di set, maka akan muncul pesan error

# # SET : discard
# maem = {"nasgor", "telor", "mie", "bakso", "bakso"}
# maem.discard("kuah")
# print(maem)
#     # munculnya = {'mie', 'telor', 'bakso'}
#     # kalo kita hapus yang tidak ada di set, maka tidak akan muncul pesan error

# # SET : union (gabungan)
# nama = {"Dinda", "Shasha", "Aura", "Syifa"}
# nama2 = {"Shasha", "Aura", "Julpa", "Aya"}
# print("Gabungan nama dan nama2 =", nama.union(nama2))
#     # munculnya = {'Aura', 'Shasha', 'Aya', 'Dinda', 'Julpa', 'Syifa'}

# # SET : intersection (irisan)
# nama = {"Dinda", "Shasha", "Aura", "Syifa"}
# nama2 = {"Shasha", "Aura", "Julpa", "Aya"}
# print("Irisan nama dan nama2 =", nama.intersection(nama2))
#     # munculnya = {'Shasha', 'Aura'}

# # SET : difference (selisih)
# nama = {"Dinda", "Shasha", "Aura", "Syifa"}
# nama2 = {"Shasha", "Aura", "Julpa", "Aya"}
# print("Elemen yang ada di nama dan tidak ada di nama2 =", nama.difference(nama2))
#     # munculnya = {'Syifa', 'Dinda'} karena elemen di nama yang nggak ada di nama2
# print("Elemen yang ada di nama2 dan tidak ada di nama =", nama2.difference(nama))
#     # munculnya = {'Aya', 'Julpa'} karena elemen di nama2 yang nggak ada di nama
# print(nama.symmetric_difference(nama2))
#     # munculnya = {'Syifa', 'Julpa', 'Dinda', 'Aya'} karena kebalikan dari irisan

# # SET : update
# nama = {"Dinda", "Shasha", "Aura", "Syifa"}
# nama2 = {"Shasha", "Aura", "Julpa", "Aya"}
# nama.update(nama2)
# print(nama)
#     # munculnya = {'Syifa', 'Julpa', 'Aya', 'Shasha', 'Aura', 'Dinda'}



# # ===================================
# # DICTIONARY
# # ===================================

# Menu = {
#     "Maem" : ["nasgor", "telor", "mie", "bakso", "bakso", 1, 2], 
#     "Wedang" : ["jus", "susu", "teh"]
# }
# print(Menu["Maem"][1])

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {"Instagram" : "daffahrhap"
#     }
# }

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama"))

Nilai = {
    "Matematika": 80,
    "B. Indonesia": 90,
    "B. Inggris": 81,
    "Kimia": 78,
    "Fisika": 80
}

# # Tanpa menggunakan items()
# for k in Nilai:
#     print(k)
#     print("") # pemisah

# # Menggunakan items()
# for k, v in Nilai.items():
#     print(f"Nilai {k} anda adalah {v}")

Film = {
    "Avenger Endgame" : "Action",
    "Sherlock Holmes" : "Mystery",
    "The Conjuring" : "Horror"
}
print(Film)

Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller", "kuku" : "hai"})

#Setelah Ditambah
print(Film) 