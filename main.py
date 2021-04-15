#method
import functions
from functions import Ac

la = functions.iden("37","2")
la.identitas()

li = functions.nama("Abdullah Faqih Mubarak","Didi Suhardi","Felisiana Ardelia Azzahra","Zakia Marrit")
li.anggota()

print("================ Pengaturan AC ================")

run = True
#perulangan while
while run:
    #variabel kondisi
    kondisi = input("Apakah kamu ingin menyalakan AC (Ya/Tidak)? ")
    
    #pengkondisian
    if kondisi == "Ya":
        print ("AC menyala")
        suhu = input("\nMasukkan suhu yang anda inginkan = ")
        Ac.ubah(suhu)

        On = True
        while On:            
            kondisi = input("\nApakah kamu ingin mengganti suhu (Ya/Tidak)? ")
            if kondisi == "Ya":
                suhu = input("Masukkan suhu yang anda inginkan = ")
                Ac.ubah(suhu)

            elif kondisi == "Tidak":
                break
            else:
                print("Anda salah memasukkan kondisi, mohon baca kembali perintah yang tertera")

    elif kondisi == "Tidak":
        print ("AC mati")
        break
    else:
        print("Anda salah memasukkan kondisi, mohon baca kembali perintah yang tertera")
