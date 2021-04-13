#method
from functions import Ac

#variabel kondisi
kondisi = input("On/Off")

#perulangan while
while True:
    
    #pengkondisian
    if kondisi == "":
        suhu = input("Masukkan suhu yang anda inginkan")
        Ac.ubah(suhu)
    elif kondisi == "Off":
        break
    else:
        print("Anda salah memasukkan kondisi, bisa baca ga")
