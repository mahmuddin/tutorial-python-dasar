# dictionary dengan data
siswa = {
    "nama": "John",
    "umur": 22,
    "nilai": [90, 85, 95]
}

print("Siswa: ", siswa)
print("Nama: ", siswa["nama"]) # John
print("Umur: ", siswa["umur"]) # 22
print("Nilai: ", siswa["nilai"]) # [90, 85, 95]

# Mengubah nilai
siswa["umur"] = 23
print("Umur: ", siswa["umur"]) # 23

# Menambahkan nilai
siswa["alamat"] = "Bandung"
print("Alamat: ", siswa["alamat"]) # Bandung

# Menghapus key-value
del siswa["nilai"]
print("Siswa: ", siswa)

#mengiterasi keys
for key in siswa:
    print("Key: ", key, ":", siswa[key])

# mengiterasi values
for value in siswa.values():
    print("Value: ", value)

#mengiterasi keys dan values
for key, value in siswa.items():
    print("Key: ", key, ":", "Value: ", value)
