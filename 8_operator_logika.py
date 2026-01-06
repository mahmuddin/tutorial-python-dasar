umur = int(input("Masukkan umur: "))
punya_sim = input("Punya SIM? (ya/tidak): ")

if umur >= 18 and punya_sim == "ya":
    print("Anda boleh mengemudi")
else:
    print("Anda tidak boleh mengemudi")