from model.daftar_nilai import database 
from tabulate import tabulate 
def lihat_data():
    print(tabulate(database.values(), headers=["NAMA", "NIM", "TUGAS", "UTS", "UAS","AKHIR"], tablefmt="double_grid"))

def cari(nama):
    
    for key, value in database.items():
        if nama in value:
            print(tabulate(database.values(), headers=["NAMA", "NIM", "TUGAS", "UTS", "UAS","AKHIR"], tablefmt="double_grid"))
        else :
            print("Upss Data Tidak Ditemukan! ")
    