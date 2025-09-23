# Variabel suhu dalam derajat celcius
suhu_1 = 27
suhu_2 = 33
suhu_3 = 46
suhu_4 = 55
suhu_5 = 67
suhu_6 = 92
suhu = [suhu_1, suhu_2, suhu_3, suhu_4, suhu_5, suhu_6] #POIN PLUS
print("List suhu belum dikonversikan (Celcius):") 
print(str(suhu_1) + "° C") 
print(str(suhu_2) + "° C") 
print(str(suhu_3) + "° C") 
print(str(suhu_4) + "° C") 
print(str(suhu_5) + "° C") 
print(str(suhu_6) + "° C")

# Variabel suhu konversi #POIN PLUS
suhu_1_F = (9/5 * suhu[0]) + 32 #Celcius ke Fahrenheit
suhu_2_F = (9/5 * suhu[1]) + 32 #Celcius ke Fahrenheit
suhu_1_K = suhu[2] + 273.15 #Celcius ke Kelvin
suhu_2_K  = suhu[3] + 273.15 #Celcius ke Kelvin
suhu_1_R  = (4/5) * suhu[4] #Celcius ke Reamur
suhu_2_R  = (4/5) * suhu[5] #Celcius ke Reamur
suhu_Konversi = [suhu_1_F, suhu_2_F, suhu_1_K, suhu_2_K, suhu_1_R, suhu_2_R]
print("List suhu setelah dikonversikan:")
print("27° C ke Fahrenheit = " + str(suhu_1_F) + "° F") 
print("33° C ke Fahrenheit = " + str(suhu_2_F) + "° F") 
print("46° K ke Kelvin = " + str(suhu_1_K) + "° K") 
print("55° K ke Kelvin = " + str(suhu_2_K) + "° K") 
print("67° R ke Reamur = " + str(suhu_1_R) + "° R") 
print("92° R ke Reamur = " + str(suhu_2_R) + "° R") 

# Jumlah dan rata-rata suhu konversi
Jumlah = suhu_1_F + suhu_2_F + suhu_1_K + suhu_2_K + suhu_1_R + suhu_2_R
Rata2 = Jumlah / 6
print("Total suhu yang telah dikonversikan adalah", Jumlah)
print("Hasil variabel Jumlah dibagi dengan banyak data adalah", Rata2)

# NIM dan bandingkan dengan rata-rata
NIM = 63
print("NIM saya adalah", NIM)
Bolean = NIM < Rata2
print("NIM < Rata2 adalah", Bolean)

print("List suhu 46 sampai 92 (Celcius):", suhu[-4:6]) #POIN PLUS