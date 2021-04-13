#method
from functions import Ac

run = True
#perulangan while
while run:
    #variabel kondisi
    kondisi = input("On/Off")
    
    #pengkondisian
    if kondisi == "On":
        suhu = input("Masukkan suhu yang anda inginkan")
        Ac.ubah(suhu)
        On = True
        while On:
            kondisi = input("Ganti suhu / Off")
            if kondisi == "Ganti suhu":
                suhu = input("Masukkan suhu yang anda inginkan")
                Ac.ubah(suhu)
            elif kondisi == "Off":
                run = False
            else:
                print("Anda salah memasukkan kondisi, mohon baca kembali perintah yang tertera")
    elif kondisi == "Off":
        break
    else:
        print("Anda salah memasukkan kondisi, mohon baca kembali perintah yang tertera")
