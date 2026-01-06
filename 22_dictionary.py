# dictionary dengan data
siswa = {
    "nama": "John",
    "umur": 22,
    "nilai": [90, 85, 95]
}

print(siswa)
print(siswa["nama"]) # John
print(siswa["umur"]) # 22
print(siswa["nilai"]) # [90, 85, 95]

# Mengubah nilai
siswa["umur"] = 23
print(siswa["umur"]) # 23

# Menambahkan nilai
siswa["alamat"] = "Bandung"
print(siswa["alamat"]) # Bandung

# Menghapus key-value
del siswa["nilai"]
print(siswa)

#mengiterasi keys
for key in siswa:
    print(key, ":", siswa[key])

# mengiterasi values
for value in siswa.values():
    print(value)

#mengiterasi keys dan values
for key, value in siswa.items():
    print(key, ":", value)
