nama = "Mahmuddin"
usia = 22

print("Nama : " + str(nama) + " Usia : " + str(usia))

#Bilangan dengan koma
berat = 65.7
tinggi = 175.7
pi = 3.14159
suhu = 36.6
print("Tipe data dari berat: ", type(berat))
print("Tipe data dari tinggi: ", type(tinggi))
print("Tipe data dari pi: ", type(pi))
print("Tipe data dari suhu: ", type(suhu))

#Notasi scientific
speed_of_light = 2.998e8 # 299.8 * 10^8 = 299800000
very_small = 1e-10 # 1 * 10^-10 = 0.0000000001
print("Tipe data dari speed_of_light: ",type(speed_of_light))
print("Tipe data dari very_small: ", type(very_small))

#Bilangan bulat
jumlah_barang = 10
stok_gudang = 150
tahun_terbit = 2023
print("Tipe data dari jumlah_barang: ", type(jumlah_barang))
print("Tipe data dari stok_gudang: ",type(stok_gudang))
print("Tipe data dari tahun_terbit: ",type(tahun_terbit))

#Bilangan kompleks
z = 2 + 3j
print("Nilai z: ",z)
print("Tipe data dari z:", type(z))

#String dengan single quote
nama = 'Mahmuddin'
print("Nama: ", nama)
print("Tipe data dari nama: ", type(nama))

#String dengan double quote 
nama = "Mahmuddin"
print("Nama: ", nama)
print("Tipe data dari nama: ", type(nama))

#String dengan triple quote
alamat = """Jl. Merdeka No. 123,
Jakarta, Indonesia"""
print("Alamat: ", alamat)
print("Tipe data dari alamat: ", type(alamat))

#String kosong
nama = ""
print("Nama: ", nama)
print("Tipe data dari nama: ", type(nama))

#Tipe data boolean
is_student = True
is_active = False
print("Apakah is_student: ", is_student)
print("Apakah is_active: ", is_active)
print("Tipe data dari is_student: ", type(is_student))
print("Tipe data dari is_active: ", type(is_active))

#Multiple Assignment
x = y = z = 10 #Semua variabel akan memiliki nilai yang sama
a, b, c = 1, 2, 3 #Setiap variabel akan memiliki nilai yang berbeda
name, age, is_active = "Mahmuddin", 22, True #Variabel akan memiliki nilai yang berbeda

#Mengubah nilai variabel
x = 10
y = 20
print(x)
print(y)
x, y = y, x #Mengubah nilai variabel
print("nilai x setelah diubah: ", x)
print("nilai y setelah diubah: ",y)

#Menggunakan variabel dalam operasi
panjang = 10
lebar = 20
luas = panjang * lebar
print("Luas persegi panjang : ", luas)

nama_depan = "Mahmuddin"
nama_belakang = "NF"
nama_lengkap = nama_depan + " " + nama_belakang
print("Nama Lengkap : ", nama_lengkap)