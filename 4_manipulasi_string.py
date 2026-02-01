nama = "Mahmuddin"
umur = 25

# Cara yang salah
# pesan = "Nama saya " + nama + ", umur saya " + umur
# print(pesan)

# Cara yang benar
pesan = "Nama saya " + nama + ", umur saya " + str(umur)
print("Pesan: ", pesan)

#String method
print("String method:")
print("Nama: ", nama.upper()) # MAHMUDDIN
print("Nama: ", nama.lower()) # mahmuddin
print("Nama: ", nama.capitalize()) # Mahmuddin
print("Panjang nama: ", len(nama)) # 9
print("Panjang pesan: ", len(pesan)) # 33
print("Pesan: ", pesan.title()) # Nama Saya Mahmuddin, Umur Saya 25 (mengubah huruf awal menjadi huruf besar)
print("Pesan: ", pesan.strip()) # Nama saya Mahmuddin, umur saya 25 (menghapus spasi di awal dan akhir string)
print("Pesan: ", pesan.replace("Mahmuddin", "NF")) # Nama saya NF, umur saya 25 (mengganti Mahmuddin dengan NF)
print("Posisi Mahmuddin: ", pesan.find("Mahmuddin")) # 10 (mencari posisi dari Mahmuddin)
print("Jumlah huruf a: ", pesan.count("a")) # 7 (mencari jumlah huruf a)
print("Pesan: ", pesan.split(" ")) # ['Nama', 'saya', 'Mahmuddin', 'Umur', 'saya', '25'] (memisahkan string berdasarkan spasi)
print("Pesan dimulai dengan Nama: ", pesan.startswith("Nama")) # True (memeriksa apakah string dimulai dengan "Nama")
print("Pesan diakhiri dengan 25: ", pesan.endswith("25")) # True (memeriksa apakah string diakhiri dengan "25")
print("Pesan numerik: ", pesan.isnumeric()) # False
print("Pesan alfabet: ", pesan.isalpha()) # False  
print("Pesan alfanumerik: ", pesan.isalnum()) # False
print("Pesan digit: ", pesan.isdigit()) # False
print("Pesan huruf kecil: ", pesan.islower()) # False
print("Pesan huruf besar: ", pesan.isupper()) # False
print("Pesan title: ", pesan.istitle()) # False
print("Pesan spasi: ", pesan.isspace()) # False

#Manipulasi string
print("Manipulasi string:")
jalan = "Jl. Merdeka No. 123, Jakarta, Indonesia"
print("Pesan: ", jalan.split(","))
print("Pesan: ", jalan.replace("Jakarta", "Bandung"))
print("Pesan: ", jalan.find("No."))

print("Pesan: ", jalan[0]) # J (karakter pertama)
print("Pesan: ", jalan[1]) # l (karakter kedua)
print("Pesan: ", jalan[2]) # . (karakter ketiga)
print("Pesan: ", jalan[-1]) # a (karakter terakhir)
print("Pesan: ", jalan[-2]) # i (karakter kedua dari belakang)
print("Pesan: ", jalan[-3]) # s (karakter ketiga dari belakang)
print("Pesan: ", jalan[:5]) # Jl. M (dari awal sampai index 4)
print("Pesan: ", jalan[:]) # Jl. Merdeka No. 123, Jakarta, Indonesia (dari awal sampai akhir)
print("Pesan: ", jalan[2:]) # . Merdeka No. 123, Jakarta, Indonesia (dari index 2 sampai akhir)
print("Pesan: ", jalan[0:3]) # Jl. (karakter pertama hingga ketiga)
print("Pesan: ", jalan[0:5]) # Jl. M (karakter pertama hingga kelima)
print("Pesan: ", jalan[1:10]) # l. Merdek (karakter kedua hingga sepuluh)

#Escape character
print("Escape character:")
print("Hello\nWorld") # Hello World (menggunakan escape character untuk newline)
print("Hello\tWorld") # Hello World (menggunakan escape character untuk tab)
print("Hello\rWorld") # World (menggunakan escape character untuk return)
print("Hello\bWorld") # HelloWorld (menggunakan escape character untuk backspace)
print("Hello\fWorld") # HelloWorld (menggunakan escape character untuk form feed)
print("Hello\\World") # Hello\World (menggunakan escape character untuk backslash)
print("Hello\'World") # Hello'World (menggunakan escape character untuk single quote)
print("Hello\"World") # Hello"World (menggunakan escape character untuk double quote)
print("Dia berkata \"Halo\" kepada saya") # Dia berkata "Halo" kepada saya (menggunakan escape character untuk double quote dalam string)

#String Interpolation
print("String Interpolation:")
print("Nama saya %s, umur saya %d" % (nama, umur)) # Nama saya Mahmuddin, umur saya 25 (menggunakan string interpolation)
print("Nama saya {}, umur saya {}".format(nama, umur)) # Nama saya Mahmuddin, umur saya 25 (menggunakan string interpolation)
print(f"Nama saya {nama}, umur saya {umur}") # Nama saya Mahmuddin, umur saya 25 (menggunakan string interpolation)     

#Operasi matematika dalam f-string
harga = 10000
jumlah = 3
total = f"Total: Rp {harga * jumlah:,}"
print("Total: ", total) # Total: Rp 30,000 (menggunakan f-string untuk operasi matematika)

# Method calls dalam f-string
nama = "Mahmuddin"
salam = f"Halo {nama.upper()}"
print("Salam: ", salam) # Halo MAHMUDDIN (menggunakan method upper())
    