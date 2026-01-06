def nama_function():
    # kode yang akan dijalankan
    print("Hello dari function")

# Memanggil function
nama_function()
nama_function()
nama_function()

def sapa_nama(nama):
    print("Halo, " + nama)
    print("Senang bertemu dengan Anda")

# Memanggil function dengan parameter
sapa_nama("Mahmuddin")
sapa_nama("Fajri")
sapa_nama("Nurul")

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang adalah: ", luas)

# Memanggil function dengan parameter
hitung_luas_persegi_panjang(10, 20)
hitung_luas_persegi_panjang(8, 15)

def hitung_luas_lingkaran(r):
    pi = 3.14
    return pi * r * r

luas1 = hitung_luas_lingkaran(10)
luas2 = hitung_luas_lingkaran(15)

print("Luas lingkaran adalah: ", luas1)
print("Luas lingkaran adalah: ", luas2)
print("Total luas lingkaran adalah: ", luas1 + luas2)    

def sapa(nama, sapaan="Halo"):
    print(sapaan + ", " + nama)

sapa("Mahmuddin") # Halo, Mahmuddin
sapa("Fajri", "Hello") # Hello, Fajri
sapa("Nurul", "Hey") # Hey, Nurul

def perkenalan(nama, alamat, umur):
    print("Nama: " + nama)
    print("Alamat: " + alamat)
    print("Umur: " + str(umur))
    print("-----")

# positional arguments (urutan harus sesuai)
perkenalan("Mahmuddin", "Bandar Lampung", 22)
perkenalan("Fajri", "Bandar Lampung", 22)

# keyword arguments (urutan tidak harus sesuai)
perkenalan(nama="Mahmuddin", umur=22, alamat="Bandar Lampung")
perkenalan(alamat="Bandar Lampung", nama="Fajri", umur=22)

def buat_profile(nama, umur, kota="Jakarta", pekerjaan="Belum bekerja"):
    print(f"=== PORFILE {nama.upper()} ===")
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Kota: {kota}")
    print(f"Pekerjaan: {pekerjaan}")
    print("-----")

#Positional + keyword arguments
buat_profile("Alice", 25) #menggunakan default value
buat_profile("Bob", 30, kota="Bandung")
buat_profile("Diana", 32, kota="Bandar Lampung", pekerjaan="Mahasiswa")

def fungsi_test():
    x = 10 #local variable
    print("Nilai x di dalam fungsi: ", x)

fungsi_test()
# print("Nilai x di luar fungsi: ", x) # Error karena x tidak didefinisikan di luar fungsi

nama_global = "Mahmuddin" # global variable

def tampilkan_nama():
    print("Nama global: ", nama_global) # bisa mengakses global variable

def ubah_nama():
    global nama_global
    nama_global = "Fajri" # bisa mengubah global variable

tampilkan_nama() # Mahmuddin
ubah_nama()
tampilkan_nama() # Fajri

def cetak_list(*list):
    for item in list:
        print(item)

cetak_list(1,2,3,4,5,6,7,8,9,10)

def cetak_dict(**dict):
    for key, value in dict.items():
        print(key, value)

cetak_dict(nama="Mahmuddin", umur=22, alamat="Bandar Lampung")
