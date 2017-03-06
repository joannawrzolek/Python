import string
a = input('Podaj imie i nazwisko: ')
a = a.split(' ')
if (len(a) < 2):
	print('Nie wprowadzono imienia i/lub nazwiska')
else:
	print('Imie: ' + a[0])
	print('Nazwisko: ' + a[len(a)-1])