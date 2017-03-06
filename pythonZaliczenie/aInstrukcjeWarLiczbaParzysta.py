#!/usr/bin/env python
# -*- coding: windows-1250 -*-


#Zadanie 1: Napisz aplikacje sprawdzajaca dla podanej liczby czy jest ona parzysta.
#def czyLiczbaParzysta(x):
#        xString = input('Podaj liczbe n: ');
#        x =  str.isdigit(xString)
#        if x ==True:
#            x = int(xString)
#            if (x%2)==0:
#             print("Liczba parzysta")
#            else:
#                print ("Liczba nie parzysta")
#        else:
#             print("Wprowadzony znak nie jest liczba")
#czyLiczbaParzysta(input)


a = int(input('Podaj liczbe: '))
if (a%2 == 0):
	print('Liczba ' + str(a) + ' jest parzysta')
else:
	print('Liczba ' + str(a) + ' jest nieparzysta')