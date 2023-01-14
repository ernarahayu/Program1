import model
import view
import os

while True:
    print("--------------")
    print("Pilihan Menu :")
    print("--------------")
    print()
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Hapus Data") 
    print("4. Ubah Data")
    print("5. Cari Data") 
    print("6. Keluar")

    pilihan=input("Silahkan Masukan Pilihan Menu: ")

    if pilihan == '1':
        from view.input_nilai import masukan_data
        masukan_data()

    elif pilihan == '2':
        from view.view_nilai import lihat_data
        lihat_data()

    elif pilihan =='3':
        from view.input_nilai import hapus_data
        hapus_data()

    elif pilihan =='4':
        from view.input_nilai import ubah_data
        ubah_data()

    elif pilihan == '5':
        from model.daftar_nilai import cari_data
        cari_data()

    elif pilihan == '6':
        print("Terimakasih")
        break 

    else:
        print("Masukan Pilihan Menu Yang Benar")
    

