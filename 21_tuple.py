point = (5,10)

print("Point: ", point[0]) # 5
print("Point: ", point[1]) # 10

# Untuk data yang tidak berubah
tanggal_lahir = (21, 12, 2000) # tanggal, bulan, tahun
print("Tanggal Lahir:", tanggal_lahir) # (21, 12, 2000)

#iterasi di table
for i in tanggal_lahir:
    print("Tanggal Lahir: ", i)

#iterasi di tuple dengan index
for i in range(len(tanggal_lahir)):
    print("Tanggal Lahir: ", tanggal_lahir[i])