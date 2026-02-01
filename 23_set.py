buah = {"apel", "pisang", "mangga"}
print("Buah: ", buah)

# menambahkan data
buah.add("semangka")
print("Buah: ", buah)

# menghapus data
buah.remove("pisang")
print("Buah: ", buah)

# mengiterasi data
for e in buah:
    print("Buah: ", e)
    
# Jika ingin mengosongkan isi set tanpa menghapus variabelnya, gunakan:
buah.clear()
print("Buah: ", buah)

# menghapus set
del buah
# print(buah) # Error karena variabel buah sudah dihapus dari memori
