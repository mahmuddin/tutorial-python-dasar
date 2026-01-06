buah = {"apel", "pisang", "mangga"}
print(buah)

# menambahkan data
buah.add("semangka")
print(buah)

# menghapus data
buah.remove("pisang")
print(buah)

# mengiterasi data
for e in buah:
    print(e)
    
# Jika ingin mengosongkan isi set tanpa menghapus variabelnya, gunakan:
buah.clear()
print(buah)

# menghapus set
del buah
# print(buah) # Error karena variabel buah sudah dihapus dari memori
