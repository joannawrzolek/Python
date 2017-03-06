#!/usr/bin/env python
# -*- coding: windows-1250 -*-
s = 'Wojski, chlubnie skończywszy łowy, wraca z boru, A Telimena w głębi samotnego dworu Zaczyna polowanie. Wprawdzie nieruchoma Siedzi z założonemi na piersiach rękoma, Lecz myślą goni źwierzów dwóch; szuka sposobu, Jak by razem obsaczyć i ułowić obu: Hrabię i Tadeusza. Hrabia, panicz młody, Wielkiego domu dziedzic, powabnej urody; Już trochę zakochany! Cóż? może się zmienić! Potem, czy szczerze kocha? czy się zechce żenić? Z kobietą kilku laty starszą! niebogatą! Czy mu krewni pozwolą? co świat powie na to?'
inp = input()

if (inp.lower() in s.lower()):
	print('Wyrażenie "', inp, '" wystepuje w przechowywanym tekście')
else:
	print('Wyrażenie "', inp, '" nie wystepuje w przechowywanym tekście')