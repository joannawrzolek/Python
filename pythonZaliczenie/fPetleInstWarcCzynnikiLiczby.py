import math
a = int(input('Podaj liczbe: '))

for x in range(1, a+1):
	if (a%x == 0):
		print(x)
