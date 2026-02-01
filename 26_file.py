print("===SIMPAN DATA NILAI====")


# Use 'with' to ensure file is closed automatically
with open("nilai_siswa.txt", "w") as file:
    while True: 
        nama = input("Nama siswa (enter untuk selesai): ")
        if nama == "": 
            break

        nilai = input("Nilai: ") 
        
        # Tulis ke file 
        file.write(nama + "," + nilai + "\n")
        file.flush()
        print("Data", nama, "berhasil disimpan!")
 
print("Semua data berhasil disimpan ke nilai_siswa.txt")


print("=== MENAMPILKAN DATA NILAI")
try:
    with open("nilai_siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(f"{data[0]} : {data[1]}")
except FileNotFoundError:
    print("File tidak ditemukan")
print("=== SELESAI ===")