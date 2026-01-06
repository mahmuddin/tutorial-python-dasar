# List kosong
daftar_kosong = []

# List dengan angka
daftar_angka = [1, 2, 3, 4, 5]
print(daftar_angka)

#List dengan string
daftar_buah = ["apple", "banana", "cherry"]
print(daftar_buah)

#List campuran
daftar_campuran = [1, "apple", 3.14, True]
print(daftar_campuran)

# mengakses elemen list
buah = ["apel", "jeruk", "pisang", "mangga"]
print(buah[0]) # apel
print(buah[1]) # jeruk
print(buah[2]) # pisang
print(buah[3]) # mangga
print(buah[-1]) # mangga
print(buah[-2]) # pisang
print(buah[-3]) # jeruk

#mengubah elemen list 
warna = ["merah", "kuning", "hijau"]
print(warna)
warna[1] = "biru"
print(warna) # ["merah", "biru", "hijau"]

#menambah elemen list
warna.append("kuning")
print(warna) # ["merah", "biru", "hijau", "kuning"]

buah.insert(1, "semangka")
print(buah) # ["apel", "semangka", "jeruk", "pisang", "mangga"]

buah.remove("jeruk")
print(buah) # ["apel", "semangka", "pisang", "mangga"]

buah.pop(2)
print(buah) # ["apel", "semangka", "mangga"]

del buah[1]
print(buah) # ["apel", "mangga"]

buah.sort()
print(buah) # ["apel", "mangga"]

buah.reverse()
print(buah) # ["mangga", "apel"]

buah.count("apel")
print(buah.count("apel")) # 1

buah.index("mangga")
print(buah.index("mangga")) # 0

buah.copy()
print(buah.copy()) # ["mangga", "apel"]

print(len(buah)) # 2

satu = [1, 2, 3]
dua = [4, 5, 6]

print(satu + dua) # [1, 2, 3, 4, 5, 6]

banyak_buah = ["apel", "pisang", "mangga", "jeruk", "durian"]
for buah in banyak_buah:
    print(buah)  # "apel", "pisang", "mangga", "jeruk", "durian"

for i in range(len(banyak_buah)):
    print(banyak_buah[i]) # "apel", "pisang", "mangga", "jeruk", "durian"

if "pisang" in banyak_buah:
    print("ada")
else:
    print("tidak ada")
    