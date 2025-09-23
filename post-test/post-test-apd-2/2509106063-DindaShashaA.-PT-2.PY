# Variabel suhu dalam derajat celcius
suhu_1 = 27
suhu_2 = 33
suhu_3 = 46
suhu_4 = 55
suhu_5 = 67
suhu_6 = 92
Suhu = [suhu_1, suhu_2, suhu_3, suhu_4, suhu_5, suhu_6] #POIN PLUS
print("List suhu belum dikonversikan (Celcius):", Suhu)

# Variabel suhu konversi #POIN PLUS
Konversi_1 = (9/5 * Suhu[0]) + 32 #Celcius ke Fahrenheit
Konversi_2 = (9/5 * Suhu[1]) + 32 #Celcius ke Fahrenheit
Konversi_3 = Suhu[2] + 273.15 #Celcius ke Kelvin
Konversi_4 = Suhu[3] + 273.15 #Celcius ke Kelvin
Konversi_5 = (4/5) * Suhu[4] #Celcius ke Reamur
Konversi_6 = (4/5) * Suhu[5] #Celcius ke Reamur
SuhuKonversi = [Konversi_1, Konversi_2, Konversi_3, Konversi_4, Konversi_5, Konversi_6]
print("List suhu setelah dikonversikan:", SuhuKonversi)

# Jumlah dan rata-rata suhu konversi
Jumlah = SuhuKonversi[0] + SuhuKonversi[1] + SuhuKonversi[2] + SuhuKonversi[3] + SuhuKonversi[4] + SuhuKonversi[5]
Rata2 = Jumlah / 6
print("Total suhu yang telah dikonversikan adalah", Jumlah)
print("Hasil variabel Jumlah dibagi dengan banyak data adalah", Rata2)

# NIM dan bandingkan dengan rata-rata
NIM = 63
print("NIM saya adalah", NIM)
Bolean = NIM < Rata2
print("NIM < Rata2 adalah", Bolean)

print("List suhu 46 sampai 92 (Celcius):", Suhu[-4:6]) #POIN PLUS