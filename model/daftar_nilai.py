database = {}

def tambah_data(nama, nim, tugas, uts, uas, akhir):
    database[nama] = nama, nim, tugas, uts, uas, akhir

def proses_hapus_data(nama):
    if nama in database.keys():
        del database[nama]
        print(f'Data dengan nama {nama} berhasil dihapus!!')
        return True
    else:
        print(f'Upss nama {nama} tidak ditemukan!!')
        return False

def proses_ubah_data(nama):
    if nama in database.keys():
        del database[nama]
        print()
        print(":----------------------------------:")
        print(":----Silahkan Masukan Data Baru----:")
        print(":----------------------------------:")
        print()
        nama = input("Masukan Nama : ")
        nim =int(input("Masukan NIM : "))
        tugas =int(input("Masukan nilai tugas : "))
        uts =int(input("Masukan nilai UTS : "))
        uas =int(input("Masukan nilai UAS : "))
        akhir =float((0.30*tugas)+(0.35*uts)+(0.35*uas))
        tambah_data(nama, nim, tugas, uts, uas, akhir)
    else :
        print("Data tidak ditemukan")

def cari_data():
    from view.view_nilai import cari
    cari(input("Masukan nama yang dicari : "))