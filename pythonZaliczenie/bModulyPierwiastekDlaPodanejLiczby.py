#!/usr/bin/env python
# -*- coding: windows-1250 -*-
import math;
import string;

#Zadanie 1: Napisz aplikacje wyliczajace pierwiastek dla podanej liczby.
def pierwiastek(y):
     yString = input('Podaj liczbe k: ');
     y =  str.isdigit(yString)
     if y == True:
        y = float(yString)
        return math.sqrt(y)
     else:
        print("Wprowadzony znak nie jest liczba")
print(pierwiastek(input))