#------- Import resource -----
from os import system
from time import sleep

#------- Score ------
poin_f = 32
poin_k = 273

#----- Calculator ------
def to_celcius(code, awal):
	if code == 'rc':
		res = awal*5/4
	elif code == 'fc':
		res = (awal - poin_f)*5/9
	elif code == 'kc':
		res = awal - poin_k

	return res

def to_reamur(code, awal):
	if code == 'cr':
		res = awal*4/5
	elif code == 'fr':
		res = (awal - poin_f)*4/9
	elif code == 'kr':
		res = (awal - poin_k)*4/5

	return res

def to_fahrenheit(code, awal):
	if code == 'cf':
		res = awal*9/5 + poin_f
	elif code == 'rf':
		res = awal*9/4 + poin_f
	elif code == 'kf':
		res == (awal - 273)*9/5 + poin_f

	return res

def to_kelvin(code, awal):
	if code == 'ck':
		res = awal + poin_k
	elif code == 'rk':
		res = awal*5/4 + poin_k
	elif code == 'fk':
		res = (awal - 32)*5/9 + poin_k

	return res

def cetak_pilihan():
	print("Available options :")
	print("[cr] From Celcius to Reamur")
	print("[ck] From Celcius to Kelvin")
	print("[cf] From Celcius to Fahrenheit")
	print("[rc] From Reamur to Celcius")
	print("[rk] From Reamur to Kelvin")
	print("[rf] From Reamur to Fahrenheit")
	print('[fc] From Fahrenheit to Celcius')
	print('[fr] From Fahrenheit to Reamur')
	print('[fk] From Fahrenheit to Kelvin')
	print('[kc] From Kelvin to Celcius')
	print('[kr] From Kelvin to Reamur')
	print('[kf] From Kelvin to Fahrenheit')
	print("[qt] Shut down")

stats = True
pilihan = None

while stats:
	system('cls')
	cetak_pilihan()
	pilihan = input('Option : ')
	if len(pilihan) != 2:
		pass
	elif pilihan[1] == 'c':
		awal = float(input("Temperature : "))
		res = to_celcius(pilihan, awal)
		print("Result : ", res)
		input("Press [enter] to continue")

	elif pilihan[1] == 'r':
		awal = float(input("Temperature : "))
		res = to_reamur(pilihan, awal)
		print("Result : ", res)
		input("Press [enter] to continue")

	elif pilihan[1] == 'f':
		awal = float(input("Temperature : "))
		res = to_fahrenheit(pilihan, awal)
		print("Result : ", res)
		input("Press [enter] to continue")

	elif pilihan[1] == 'k':
		awal = float(input("Temperature : "))
		res = to_kelvin(pilihan, awal)
		print("Result : ", res)
		input("Press [enter] to continue")

	elif pilihan == 'qt':
		stats = False
		print("Shutting down . . .")
		sleep(1)
	else:
		pass