# mencetak angka 1 sampai 10
angka = 1
while angka <= 10:
    print("Angka: ", angka)
    angka += 1

# Input sampai benar
password = ""
while password != "123456":
    password = input("Masukkan password: ")
    if password != "123456":
        print("Password salah. Coba lagi.")

print("Password benar!")