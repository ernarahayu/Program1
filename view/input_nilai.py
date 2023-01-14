from model.daftar_nilai import tambah_data, proses_hapus_data, proses_ubah_data

def masukan_data():

    print(":-----------------------------:")
    print(":----Silahkan Masukan Data----:")
    print(":-----------------------------:")

    nama = input("Masukan Nama : ")
    nim =int(input("Masukan NIM : "))
    tugas =int(input("Masukan nilai tugas : "))
    uts =int(input("Masukan nilai UTS : "))
    uas =int(input("Masukan nilai UAS : "))
    akhir =float((0.30*tugas)+(0.35*uts)+(0.35*uas))
    tambah_data(nama, nim, tugas, uts, uas, akhir)

def hapus_data():
    proses_hapus_data(input("Masukan Data Yang Ingin Dihapus : "))

def ubah_data():
    proses_ubah_data(input("Masukan data yang ingin diubah : "))
    
