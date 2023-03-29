
def cpsc(a, b, c, d, x):
	for i in range(3,x):
		print('ok')
		temp = b
		b = (d*a) - (c*b)
		a = temp
	return b

print(cpsc(3, 4, 4, 5, 7))