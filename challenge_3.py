'''
1. Pergi ke 5 destinasi wisata
2. Buatkan list dari 5 tempat tersebut dan tidak perlu berurut secara alphabet
3. cetak lists ori
4. cetak list urut tanpa mengubah list yang asli
5. karena dana terbatas hapus 2 tujuan , index 3 dan index terakhir
6. tiba-tiba ada sponsor untuk ke paris, masukan kota paris menjadi tujuan pertama
7. cetak list setelah diurutkan secara permanen -> Z - A
'''

destination = ['Ente Isla', 'Apostle', 'Alfeheim', 'Fontaine', 'Jura']

#1
print(destination)

#2
print(sorted(destination))

#3
destination.pop(3)
leng = len(destination)
destination.pop(-1)

#4
destination.insert(0, 'Pariss')
'''
destination.append('Parris')

current_info = []
if True:
	n = 0
	while n != leng - 2:
		current_info.append(destination[n])
		n += 1
		if n <= 3:
			current_info.append(destination[n])
		destination.pop(n)

	destination.pop(1)
	#print(destination)

	destination[0] = 'Parris'

	a = 0
	#print(current_info)
	while a != 3:
		destination.append(current_info[a])
		a += 1

print(destination)
'''

#5
destination.sort(reverse=True)
print(destination)