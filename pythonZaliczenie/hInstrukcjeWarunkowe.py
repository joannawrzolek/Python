#!/usr/bin/env python
# -*- coding: windows-1250 -*-
s = 'Wojski, chlubnie sko�czywszy �owy, wraca z boru, A Telimena w g��bi samotnego dworu Zaczyna polowanie. Wprawdzie nieruchoma Siedzi z za�o�onemi na piersiach r�koma, Lecz my�l� goni �wierz�w dw�ch; szuka sposobu, Jak by razem obsaczy� i u�owi� obu: Hrabi� i Tadeusza. Hrabia, panicz m�ody, Wielkiego domu dziedzic, powabnej urody; Ju� troch� zakochany! C�? mo�e si� zmieni�! Potem, czy szczerze kocha? czy si� zechce �eni�? Z kobiet� kilku laty starsz�! niebogat�! Czy mu krewni pozwol�? co �wiat powie na to?'
inp = input()

if (inp.lower() in s.lower()):
	print('Wyra�enie "', inp, '" wystepuje w przechowywanym tek�cie')
else:
	print('Wyra�enie "', inp, '" nie wystepuje w przechowywanym tek�cie')