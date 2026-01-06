password_benar = "python123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("Masukkan password: ")
    percobaan += 1
    if password == password_benar:
        print("Password benar!")
        break
    else:
        print("Password salah. Percobaan ke-", max_percobaan - percobaan)
else:
    print("Anda telah melebihi batas percobaan.")