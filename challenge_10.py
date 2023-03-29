#------ Import resource -----
import random
import os

#------ Function used[board] -------
def setting_up_board(rows):
	board = []

	for row in range(rows):
		line = []
		for item in range(rows):
			line.append("O") #["O", "O", "O", "O", "O"]
		board.append(line)

		"""
		[
		["O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O"], ...
		]
		"""

	return board

#-------- Function used[ship] -------------
def setting_up_ship_location(rows):
	location = [str(random.randint(0, rows-1)), str(random.randint(0, rows-1))] #[x, y]
	return location

#------------ System function -----------
def printing_board(board):
	os.system('clear') # windows : cls
	for row in board:
		for item in row:
			print(item, end=" ")
		print()

def check_user_input():
	user_input = input("Enter ship location: ").split(" ")
	#print(user_input)
	if my_ship == user_input:
		stats = True
		return True
	else:
		my_board[int(user_input[0])] [int(user_input[1])] = " " #my_board[row][col] -> " "
		return False

#--------- Object needed -----------
win = False
attempt = 1
stats = False

my_board = setting_up_board(5)
my_ship = setting_up_ship_location(5)

#--------- Looping stage ------------
while not win:
	printing_board(my_board)
	print(my_ship)
	win = check_user_input()

	if not win and attempt < 10:
		attempt += 1
	else:
		win = True

if stats == True:
	print(f"Congrats for winning in {attempt} time(s)")
else:
	print(attempt)
	print(f"Try again next time will you?")