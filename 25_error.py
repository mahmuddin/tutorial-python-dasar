# Contoh syntax error
# Kurung tidak ditutup
# print("Hello World"   

# Contoh name error
# print(nama) # Variabel 'nama' belum didefinisikan

# Contoh type error
# print("Hello" + 5) # String tidak bisa ditambahkan dengan integer

# Contoh value error
# int("hello") # String tidak bisa diubah menjadi integer

# Contoh index error
# list = [1, 2, 3]
# print(list[3]) # Index out of range

# Contoh key error
# dict = {"nama": "John", "umur": 22}
# print(dict["alamat"]) # Key tidak ditemukan

# Contoh zero division error
# print(10 / 0) # Pembagian dengan nol

print("====KALKULATOR SEDERHANA====")

try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        print("Hasil: ", angka1 + angka2)
    elif pilihan == 2:
        print("Hasil: ", angka1 - angka2)
    elif pilihan == 3:
        print("Hasil: ", angka1 * angka2)
    elif pilihan == 4:
        print("Hasil: ", angka1 / angka2)
    else:
        print("Pilihan tidak ada")
except ValueError:
    print("Input tidak valid")
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")
except Exception as e:
    print("Terjadi kesalahan: ", e)
except:
    print("Terjadi kesalahan lain")
finally:
    print("Selesai")


print("====TRY-EXCEPT-ELSE====")

try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid")
else:
    print("Angka yang Anda masukkan: " , angka)
    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka negatif")
    else:
        print("Angka nol")
finally:
    print("Selesai")

print("====TRY-EXCEPT-FINALLY====")

try:
    angka = int(input("Masukkan angka: "))
    print("Angka yang Anda masukkan: " , angka)
except ValueError:
    print("Input tidak valid")
finally:
    print("Selesai")