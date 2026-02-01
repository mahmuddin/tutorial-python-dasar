# List kosong
daftar_kosong = []

# List dengan angka
daftar_angka = [1, 2, 3, 4, 5]
print("Daftar angka: ", daftar_angka)

#List dengan string
daftar_buah = ["apple", "banana", "cherry"]
print("Daftar buah: ", daftar_buah)

#List campuran
daftar_campuran = [1, "apple", 3.14, True]
print("Daftar campuran: ", daftar_campuran)

# mengakses elemen list
buah = ["apel", "jeruk", "pisang", "mangga"]
print("Buah: ", buah[0]) # apel
print("Buah: ", buah[1]) # jeruk
print("Buah: ", buah[2]) # pisang
print("Buah: ", buah[3]) # mangga
print("Buah: ", buah[-1]) # mangga
print("Buah: ", buah[-2]) # pisang
print("Buah: ", buah[-3]) # jeruk

#mengubah elemen list 
warna = ["merah", "kuning", "hijau"]
print("Warna: ", warna)
warna[1] = "biru"
print("Warna: ", warna) # ["merah", "biru", "hijau"]

#menambah elemen list
warna.append("kuning")
print("Warna: ", warna) # ["merah", "biru", "hijau", "kuning"]

buah.insert(1, "semangka")
print("Buah: ", buah) # ["apel", "semangka", "jeruk", "pisang", "mangga"]

buah.remove("jeruk")
print("Buah: ", buah) # ["apel", "semangka", "pisang", "mangga"]

buah.pop(2)
print("Buah: ", buah) # ["apel", "semangka", "mangga"]

del buah[1]
print("Buah: ", buah) # ["apel", "mangga"]

buah.sort()
print("Buah: ", buah) # ["apel", "mangga"]

buah.reverse()
print("Buah: ", buah) # ["mangga", "apel"]

buah.count("apel")
print("Buah: ", buah.count("apel")) # 1

buah.index("mangga")
print("Buah: ", buah.index("mangga")) # 0

buah.copy()
print("Buah: ", buah.copy()) # ["mangga", "apel"]

print("Panjang buah: ", len(buah)) # 2

satu = [1, 2, 3]
dua = [4, 5, 6]

print("Satu + Dua: ", satu + dua) # [1, 2, 3, 4, 5, 6]

banyak_buah = ["apel", "pisang", "mangga", "jeruk", "durian"]
for buah in banyak_buah:
    print("Buah: ", buah)  # "apel", "pisang", "mangga", "jeruk", "durian"

for i in range(len(banyak_buah)):
    print("Buah: ", banyak_buah[i]) # "apel", "pisang", "mangga", "jeruk", "durian"

if "pisang" in banyak_buah:
    print("Buah: ada")
else:
    print("Buah: tidak ada")
    