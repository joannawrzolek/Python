#!/usr/bin/env python
# -*- coding: windows-1250 -*-
import math;


#Zadanie 3: Napisz aplikacja wyliczajaca wartosc rownania kwadratowego dla podanego a, b i c.
#def rownanieKwardatowe(input):
#    aString = input('Podaj liczbe a: ');
#    bString = input('Podaj liczbe b: ');
#    cString = input('Podaj liczbe c: ');
#    a =  str.isdigit(aString )
#    b =  str.isdigit(bString )
#    c =  str.isdigit(cString )

#    if a and b and c == True:
#        if a == b == c == 0:
#            print("a, b, c = 0 - brak rownania")
#        else:
#            delta = (b**2 -4*a*c)
#            if delta > 0:
#               pierw_delta = sqrt(delta)
#               print(pierw_delta)
#    else:
#        print("Wprowadzone znaki nie jest liczbami")
    
#print(rownanieKwardatowe(input))


import math
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))
delta = b * b - 4 * a * c
if (delta > 0):
	delta = math.sqrt(delta)
	x1 = (-b - delta) / (2 * a)
	x2 = (-b + delta) / (2 * a)
	print('x1: ' + str(x1))
	print('x2: ' + str(x2))
elif (delta == 0):
	x = -b / 2 * a
	print('x: ' + str(x))
else:
	print('brak rozwiazan')