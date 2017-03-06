class Osoba:


    def __init__(self, imie, nazwisko):
            self.imie = imie
            self.nazwisko = nazwisko

    def getImie(self):
        return self.imie



class Pracownik(Osoba):
    dodatekWakacyjny = 1000

    def __init__(self,imie, nazwisko,funkcja,wynagrodzenie,dodatekWakacyjny):
        Osoba.__init__(self, imie, nazwisko)
        self.funkcja = funkcja
        self.wynagrodzenie = wynagrodzenie
        self.dodatekWakacyjny = dodatekWakacyjny

    def setDodatekWakacyjny(self,dodatekWakacyjnyZeZmiennej):
        self.dodatekWakacyjny = dodatekWakacyjnyZeZmiennej

    def getWynagrodzenie(self):
        return self.wynagrodzenie

    def wynagrodzeniePoUwzglednieniuPremii(self, premia):
        self.wynagrodzenie = self.wynagrodzenie * premia

