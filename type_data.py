#print ("Hallo python dari VS code!")
#nama = "Fabio"
#umur = 20
#tinggi = 165.5
#print ("Nama saya " + nama)
#print ("Umur saya " + str(umur) + " tahun") 

#nama = input("Masukkan nama Anda: ")
#umur = int(input("Masukkan umur Anda: "))
#umur_tahun_depan = umur + 1
#print("Halo " + nama + " Tahun depan, umur anda akan menjadi " + str(umur_tahun_depan) + " tahun.")

#umur  = 20
#tahun_lahir = 2006
#print(umur + 6) 

#sudah_makan = True
#sedang_tidur = False
#print("Sudah makan: " , sudah_makan)

#1 soal str
nama_depan = "Fabio"
nama_belakang = "Ariant"
print("nama lengkap saya adalah : ", nama_depan , nama_belakang)

#2
kota = "Bandung"
print("Saya tinggal di kota : ", kota)

#3
hobi = "coding"
print("Hobi saya adalah : ", hobi)

#4 soal int
umur = 20 
umur_10_tahun_depan = umur + 10
print("Umur saya 10 tahun lagi adalah : ", umur_10_tahun_depan)

#5
orang_beli = 5
beli_gorengan = 3

total_gorengan = orang_beli + beli_gorengan
print("Total gorengan yang dibeli adalah : ", total_gorengan)

#6
harga_esteh = 5000
total_hitung = 4

total_bayar = harga_esteh * total_hitung
print("Total bayar esteh untuk 4 gelas adalah : ", total_bayar)

#7 soal float
tinggi_badan = 165.5
berat_badan = 60.0
print("Tinggi badan saya adalah : ", tinggi_badan , "cm dan Berat badan saya adalah : ", berat_badan , "kg")

#8
botol_air = 1.5
minum_air = 0.3

sisa_air = botol_air - minum_air
print("Sisa air dalam botol adalah : ", sisa_air , "liter")

#9
ujian_matematika = 78.5
ujian_IPA = 82.3

rata_rata_nilai = (ujian_matematika + ujian_IPA) / 2
print("Rata-rata nilai ujian saya adalah : ", rata_rata_nilai)

#10 soal boolean (bool)
sudah_makan = True
belum_makan = False
print("Hari ini sudah makan? ", sudah_makan)

#11
punya_hewan = True
print("Punya hewan: ", punya_hewan)

#12
online = True
print("Apakah sedang online? ", online)

#13 soal list
makanan = ["Nasi Goreng", "Mie Ayam", "Sate"]
print("Makanan favorit saya adalah: ", makanan)

#14
makanan = ["Nasi Goreng", "Mie Ayam", "Sate"]
print("Makanan kedua favorit saya adalah: ", makanan[1])

#15
angka = [10, 20, 30, 40, 50]
print("Angka pertama dalam daftar adalah: ", angka[0])
print("Angka kelima dalam daftar adalah: ", angka[4])

#16 soal dictionary dict)
profil = {
    "nama": "Fabio",
    "umur": 20,
    "hobi": "Coding"
}

print("Nama saya adalah: ", profil)

#17
profil = {
    "nama": "Fabio",
    "umur": 20,
    "hobi": "Coding"
}
print("Umur saya adalah: ", profil["umur"])

#18
profil = {
    "nama": "Fabio",
    "umur": 20,
    "hobi": "Coding"
}
print("Hobi saya adalah: ", profil["hobi"])

#19 soal gabungan 
nama = "Fabio"
umur = 20
tinggi = 165.5
sudah_makan = True

print(f"Nama saya {nama}, umur saya {umur} tahun , tingggi saya {tinggi} cm, Sudah makan:  {sudah_makan}")

#20
profil = {
    "hilo sachet":2500,
    "cococrrunch": 4000,
    "milku": 4000,
}

total_harga = profil["hilo sachet"] + profil["cococrrunch"] + profil["milku"]
print("Total harga semua barang adalah: ", total_harga)