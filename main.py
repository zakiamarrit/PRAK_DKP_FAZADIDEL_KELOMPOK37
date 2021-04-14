#method
from functions import Ac

print("Kelompok = 37\n Shift = 2\n Anggota 1 = Abdullah Faqih\n Anggota 2 = Didi Suhardi\n Anggota 3 = Felisiana Ardelia\n Anggota 4 = Zakia Marrit\n")
print("===== Pengatur Suhu AC=====")

run = True
#perulangan while
while run:
    #variabel kondisi
    kondisi = input("On/Off ? ")
    
    #pengkondisian
    if kondisi == "On":
        suhu = input("Masukkan suhu yang anda inginkan = ")
        Ac.ubah(suhu)
        On = True
        while On:
            kondisi = input("Ganti suhu / Tidak perlu ? ")
            if kondisi == "Ganti suhu":
                suhu = input("Masukkan suhu yang anda inginkan = ")
                Ac.ubah(suhu)
            elif kondisi == "Tidak perlu":
                break
            else:
                print("Anda salah memasukkan kondisi, mohon baca kembali perintah yang tertera")
    elif kondisi == "Off":
        break
    else:
        print("Anda salah memasukkan kondisi, mohon baca kembali perintah yang tertera")
