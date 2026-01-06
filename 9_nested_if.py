username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin":
    if password == "admin":
        print("Anda berhasil login")
        print("Selamat datang di dashboard admin")
    else:
        print("Password salah")
else:
    print("Username salah")