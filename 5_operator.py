a = 10
b = 3

#operator aritmatika
print(a + b) # 13 (penjumlahan)
print(a - b) # 7 (pengurangan)
print(a * b) # 30 (perkalian)
print(a / b) # 3.3333333333333335 (pembagian)
print(a % b) # 1 (sisa pembagian)
print(a ** b) # 1000 (pangkat)
print(a // b) # 3 (pembagian bulat) 

#Operator Precedence
#urutan prioritas (dari tinggi ke rendah)
# () (kurung)
# ** (pangkat)
# * (perkalian), / (pembagian), // (pembagian bulat), % (sisa pembagian)
# + (penjumlahan), - (pengurangan)
# == (sama dengan), != (tidak sama dengan), > (lebih dari), < (kurang dari), >= (lebih dari atau sama dengan), <= (kurang dari atau sama dengan)
# not (membalikkan hasil)
# and (kedua kondisi harus benar)
# or (satu kondisi harus benar)
print(2 + 3 * 5) # 17 (perkalian akan dieksekusi terlebih dahulu)
print((2 + 3) * 5) # 25 (kurung akan dieksekusi terlebih dahulu)

#Operator Assignment
a = 10
a += 5 # a = a + 5
print("a += 5:", a) # 15 (penjumlahan)
a -= 5 # a = a - 5
print("a -= 5:", a) # 10 (pengurangan)
a *= 5 # a = a * 5
print("a *= 5:", a) # 50 (perkalian)
a /= 5 # a = a / 5
print("a /= 5:", a) # 10.0 (pembagian)
a %= 5 # a = a % 5
print("a %= 5:", a) # 0.0 (sisa pembagian)
a **= 5 # a = a ** 5
print("a **= 5:", a) # 0.0 (pangkat)
a //= 5 # a = a // 5
print("a //= 5:", a) # 0.0 (pembagian bulat)

# Operator Perbandingan
a = 10
b = 3
print(a == b) # False (sama dengan)
print(a != b) # True (tidak sama dengan)
print(a > b) # True (lebih dari)
print(a < b) # False (kurang dari)
print(a >= b) # True (lebih dari atau sama dengan)
print(a <= b) # False (kurang dari atau sama dengan)

nama1 = "Alice"
nama2 = "Bob"
nama3 = "Alice"
print(nama1 == nama2) # False (sama dengan)
print(nama1 == nama3) # True (sama dengan)
print(nama1 != nama2) # True (tidak sama dengan)
print(nama1 != nama3) # False (tidak sama dengan)
print(nama1 > nama2) # False (lebih dari)
print(nama1 < nama2) # True (kurang dari)
print(nama1 >= nama2) # False (lebih dari atau sama dengan)
print(nama1 <= nama2) # True (kurang dari atau sama dengan)

#Operator Logika
umur = 25
nama = "Mahmuddin"
print(umur > 18 and nama == "Mahmuddin") # True (kedua kondisi harus benar)
print(umur > 18 or nama == "Mahmuddin") # True (satu kondisi harus benar)
print(not umur > 18) # False (membalikkan hasil)

hari = "Senin"
print(hari == "Senin" or hari == "Selasa") # True (satu kondisi harus benar)
print(hari == "Senin" and hari == "Selasa") # False (kedua kondisi harus benar)
print(not hari == "Senin") # False (membalikkan hasil)

#operator string
nama_depan = "Mahmuddin"
nama_belakang = "NF"
print(nama_depan + " " + nama_belakang) # Mahmuddin NF (penjumlahan string)

kata = "Python"
print(kata * 3) # PythonPythonPython (perkalian string)
print(kata[0]) # P (indeks string)

garis = "-"
print(garis * 20) # ------------------------ (perkalian string) 

kalimat = "Python adalah bahasa pemrograman"
print("Python" in kalimat) # True (operator in)
print("Java" in kalimat) # False (operator in)
print("Python" not in kalimat) # False (operator not in)
print("Java" not in kalimat) # True (operator not in)

