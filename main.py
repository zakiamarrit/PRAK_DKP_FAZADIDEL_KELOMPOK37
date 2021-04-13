#method
from functions import Ac

#perulangan while
while True:
    #variabel kondisi
    kondisi = input("On/Off")
    
    #pengkondisian
    if kondisi == "On":  
        suhu = input("Masukkan suhu yang anda inginkan")
        Ac.ubah(suhu)
    elif kondisi == "Off":
        break
    else:
        print("Anda salah memasukkan kondisi, mohon baca kembali perintah yang tertera")
