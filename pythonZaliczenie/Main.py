from Pracownik import *

Person = Pracownik("Ala", "K","programista",3000,1500 )
Person.getImie()
print("Wynagrodzenie przed")
print(Person.getWynagrodzenie())
Person.setDodatekWakacyjny(1300)
Person.wynagrodzeniePoUwzglednieniuPremii(2)

print("Wynagrodzenie po")
print (Person.getWynagrodzenie())

