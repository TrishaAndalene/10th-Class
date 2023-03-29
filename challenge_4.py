#------------- Import System -------------
from os import system
 
#------------- Menu Layout ------------------
def cetak_menu():
	print("***********************************")
	print("1. Lihat daftar nama")
	print("2. Tambah nama ke daftar")
	print("3. Hapus nama dari daftar")
	print("4. Ubah/Perbarui nama di daftar")
	print("Q. Keluar dari program")
	print("***********************************")

#--------------- Clearing Screen ----------------
def clear():
	input("Tekan ENTER untuk kembali ke MENU")
	system('cls')

#------------- Naming system --------------------- 
def lihat_daftar_nama():
	system("cls")
	print("-DAFTAR NAMA-")
	if len(daftarNama) > 0:
		index = 0
		number = 1
		while index < len(daftarNama):
			print(number,".", daftarNama[index])
			index += 1
			number += 1
	else:
		print("Daftar Nama Kosong")
	clear()

def tambah_nama():
	system("cls")
	print("-TAMBAH NAMA-")
	nama_baru = input("Masukkan nama yang akan ditambah : ")
	if len(nama_baru) > 0:
		daftarNama.append(nama_baru)
		print("Nama tersimpan!")
	else:
		print("Nama tidak boleh kosong!")
	clear()
 
def hapus_nama():
	system("cls")
	print("-HAPUS NAMA-")
	nama_dihapus = input("Masukkan nama yang akan dihapus : ")
	if nama_dihapus in daftarNama:
		daftarNama.remove(nama_dihapus)
		print("Nama telah dihapus!")
	else:
		print("Nama tidak ditemukan!")
	clear()
 
def ubah_nama():
	system("cls")
	print("-UBAH NAMA-")
	print(daftarNama)
	nama_diubah = input("Masukkan nama yang akan diubah : ")
	nama_terbaru = input("Masukkan nama terbaru : ")
	if nama_diubah in daftarNama:
		index = daftarNama.index(nama_diubah)
		daftarNama[index] = nama_terbaru
		print("Nama telah diubah!")
	else:
		print("Nama tidak ditemukan!")
	clear()

#--------------- Name List ------------------- 
daftarNama = ["Jesse","Cat","Tris","Med"]
pilihan = None
error = False
 
while not error:
 
	cetak_menu()
 
	pilihan = input("Pilih Menu : ")
 
	if pilihan == "1":
		lihat_daftar_nama()
	elif pilihan == "2":
		tambah_nama()
	elif pilihan == "3":
		hapus_nama()
	elif pilihan == "4":
		ubah_nama()
	elif pilihan.upper() == "Q":
		error = True