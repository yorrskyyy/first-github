umur = 20 

if umur >= 18:
    print("Anda sudah dewasa.")
else: 
    print("Anda masih di bawah umur.")

nilai = 12

if nilai >= 90:
    print("Nilai Anda adalah A.")
elif nilai >= 80:
    print("Nilai Anda adalah B.")   
elif nilai >= 70:
    print("Nilai Anda adalah C.")       
else:
    print("Nilai Anda adalah D.")           

# Dasar -----------------------------------------------------------------------------------------------

#1
umur = int(input("Masukkan umur Anda: "))

if umur >= 18:
    print("Anda boleh buat KTP.")
else:
    print("Anda belum boleh buat KTP.")

#2 
nilai =80 

if nilai >= 75:
    print("Selamat, Anda lulus!")
else:   
    print("Maaf, Anda tidak lulus.")   

#3
hujan = True
tidak_hujan = False

if hujan:
    print("Bawa payung.")   
else:
    print("Tidak perlu bawa payung.") 

#4
Total_belanja = 100000

if Total_belanja >= 50000:
    print("Anda mendapatkan diskon 20%.")
else:
    print("Maaf, Anda tidak mendapatkan diskon.")

#5
input_nama = input("Masukkan nama Anda: ")

if input_nama == "Fabio":
    print("Halo Boss") 
else:
    print("Halo pengguna baru")

# soal baru ---------------------------------------------------------------------------------------------

#1
angka = int(input("Masukkan sebuah angka: "))

if angka % 2 == 0:
    print("Angka tersebut adalah bilangan genap.")
else:
    print("Angka tersebut adalah bilangan ganjil.")

#2  
umur = int(input("Masukkan umur Anda: "))

if umur < 17:
    print("remaja")
elif umur <= 40:
    print("dewasa")
elif umur > 60:
    print("lansia")
else:
    print("tua")    

#3
nilai = int(input("Masukkan nilai Anda: "))
if nilai >= 75:
    print("LULUS")
else:
    print("TIDAK LULUS")    

#4
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin" and password == "12345":
    print("Login berhasil") 
else:
    print("Login gagal")    

#5
suhu = float(input("Masukkan suhu dalam Celcius: "))

if suhu > 37.5:
    print("Demam")
elif suhu >= 36.5:
    print("Normal")
elif suhu < 36.5:
    print("Terlalu dingin")

#6
lama_parkir= int(input("Masukkan lama parkir (dalam jam): "))

if lama_parkir <= 2:
    biaya = lama_parkir * 3000  
else:
    biaya = (2 * 3000) + ((lama_parkir - 2) * 5000) 

print("Total biaya parkir: Rp", biaya)

#7

Total_belanja = int(input("Masukkan total belanja Anda: "))

if Total_belanja > 100000:
    diskon = Total_belanja * 0.2    
    total_bayar = Total_belanja - diskon
    print("Anda mendapatkan diskon 20%. Total yang harus dibayar: Rp", total_bayar)
else:       
    print("Maaf, Anda tidak mendapatkan diskon. Total yang harus dibayar: Rp", Total_belanja)

