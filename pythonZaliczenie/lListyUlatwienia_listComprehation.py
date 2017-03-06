
oceny = [4.5, 3.0, 4.5, 4.5, 4.0, 4.5, 5.0, 5.0, 4.5, 4.0]
oceny.sort(reverse=True)
print( oceny )
print ("-----------------------------------------" )
print (oceny[::2]  )

#------------- co drugiego ze slownika --------------------
print ("-----------------------------------------" )


oceny_dict = {
    'Algebra liniowa W' : 4.5,
    'Algebra liniowa C' : 3.0,
    "Algorytmy i zlozonosc W" : 4.5,
    "Algorytmy i zlozonosc C" : 4.5,
    "Bazy danych W" : 4.0,
    "Bazy danych C" : 4.5,
    "Podstawy sieci komputerowych W" : 5.0,
    "Podstawy sieci komputerowych C": 5.0,
    "Rachunek prawdopodobienstwa W" : 4.5,
    "Rachunek prawdopodobienstwa C": 4.0,
}


for w in sorted(oceny_dict, key=oceny_dict.get, reverse=True)[::2]:
    print( w, oceny_dict[w] )
    
