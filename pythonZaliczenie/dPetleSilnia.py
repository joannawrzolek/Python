 #!/usr/bin/env python
# -*- coding: windows-1250 -*-
import math;

 #Zadanie 3: Napisz aplikacje wyliczajaca silnie dla podanej liczby.
#def silnia(n):
#    silniaWynik=1
#    if n in (0,1):
#        return 1
#    else:
#        for i in range(2,n+1):
#            silniaWynik = silniaWynik*i
#            return silniaWynik
#print(silnia(15))


a = int(input('Podaj liczbe: '))
suma = 1
for x in range(1, a+1):
	suma *= x
print('Silnia: ' + str(suma))