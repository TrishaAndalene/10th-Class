'''
   *
  **
 ***
****

'''
rows= 5

for row in range(rows):
	for star in range(rows-(row+1)):
		print(" ", end=" ")
	for stars in range(row+1):
		print("*", end= " ")
	print()