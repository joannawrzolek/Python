# oceny = [4.5, 3.0, 4.5, 4.5, 4.0, 4.5, 5.0, 5.0, 4.5, 4.0]
# oceny.sort(reverse=True)
# print oceny

from collections import OrderedDict
import operator

oceny_dict = {
    "Algebra liniowa W" : 4.5,
    "Algebra liniowa C" : 3.0,
    "bAlgorytmy i zlozonosc W" : 4.5,
    "cAlgorytmy i zlozonosc C" : 4.5,
    "Bazy danych W" : 4.0,
    "Bazy danych C" : 4.5,
    "xPodstawy sieci komputerowych W" : 5.0,
    "fPodstawy sieci komputerowych C": 5.0,
    "eRachunek prawdopodobienstwa W" : 4.5,
    "dRachunek prawdopodobienstwa C": 4.0,
}


for key in sorted(oceny_dict, reverse=True)[::2]:
    print ("%s: %s" % (key, oceny_dict[key]))
#print ("---------------------------------------------------------------------")
#print(OrderedDict(sorted(oceny_dict.items(),key=lambda t: t[0], reverse=False)) )

print ("---------------------------------------------------------------------")

for w in sorted(oceny_dict, key=oceny_dict.get, reverse=False):
    print( w, oceny_dict[w]  )
