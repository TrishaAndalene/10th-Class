#---------------- Import system -----------------
import os
#---------------- Menu system -----------------
def print_menu():
	os.system('cls')
	print('***********************************')
	print("[1] Wish list")
	print('[2] Add to cart')
	print('[3] Disposing item from cart')
	print("[4] Update wish list's item")
	print("[Q] Close program")
	print("***********************************")

def clear():
	input("Press [ENTER] to go back")
	os.system('cls')

#----------------- Function list ----------------
def show_wish_list():
	os.system('cls')
	print("Wish List :")
	#print(wishList)
	if len(wishList) > 0:
		index = 0
		number = 1
		while index < len(wishList):
			print(number, ".", wishList[index]) #ganti number dengan index
			index += 1
			number += 1
	else:
		print("No items found in directory")
	clear()

def add_items():
	os.system('cls')
	print("Add items to cart")
	new = input("Insert item's name : ")
	if len(new) > 0:
		wishList.append(new)
		print("Item's successfuly added")
	else:
		print("The item's name can't be empty")
	clear()

def removing_items():
	os.system('cls')
	print("'Dispose item")
	deleted = input("Insert item's name : ")
	if deleted in wishList:
		wishList.remove(deleted)
		print("Successfully deleted")
	else:
		print("No such item in wish list")
	clear()

def update_items():
	os.system('cls')
	print("Update items")
	begin = input("The item you want to change : ")
	if begin in wishList:
		index = wishList.index(begin)
		end = input("Insert the item's new name : ")
		wishList[index] = end
		print("Item's updated")
	else:
		print("Item's not found")
	clear()

#---------------- Machine --------------------
wishList = ["Genesis", "Mora"]

pilihan = None

stats = True

while stats:

	print_menu()

	pilihan = input("Choice :")
	if pilihan == '1':
		show_wish_list()
	elif pilihan == '2':
		add_items()
	elif pilihan == '3':
		removing_items()
	elif pilihan == '4':
		update_items()
	elif pilihan.upper() == 'Q':
		stats = False

print("Thank you for using our service")