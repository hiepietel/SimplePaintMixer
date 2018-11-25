import math


class ZbiornikZFarbą:
    kolor = "none" #red, green, blue
    zbiornikPusty = False
    pompaPracuje = False
    przeplyw = 0
    zgodaNaPrace = False

    def __init__(self, kolor, przeplywPompy, zbiornikPusty):
        self.kolor = kolor
        self.przeplyw = przeplywPompy
        self.zbiornikPusty = zbiornikPusty
        self.pompaPracuje = False
        if not self.zbiornikPusty:
            self.zgodaNaPrace = True

    def zwrocPrzepływ(self):
        if self.pompaPracuje:
            return self.przeplyw
        else: return 0

    def zwrocZgodeNaPrace(self):
        return self.zgodaNaPrace

    def wlaczPompe(self, wlacz):
        self.pompaPracuje = wlacz
        print("pompa z kolorem: "+self.kolor+" jest w trybie: "+str(self.pompaPracuje))


class ZbiornikGlowny:
    kolor = (0,0,0)
    zamKolor = [0, 0, 0] # zamowiony kolor
    aktKolor = [0,0,0] # aktaulny kolor
    calIlosc = 0 # zamowiona ilosc Farby
    aktIlosc = 0 # aktualna ilosc Farby
    zbiornikPusty = True
    zbiornikPelny = False
    zgodaNaPrace = False

    def __init__(self, zbiornikPusty, zbiornikPełny):
        self.zbiornikPełny=zbiornikPełny
        self.zbiornikPusty=zbiornikPusty
        if self.zbiornikPusty and not self.zbiornikPelny:
            self.zgodaNaPrace = True

    def ustawieniaPoczątkowe(self, r, g,b, ilosc ):
        self.aktIlosc = 0
        self.calIlosc = ilosc
        self.zamKolor[0] = round(r * self.calIlosc / (r + g + b), 2)
        self.zamKolor[1] = round(g * self.calIlosc / (r + g + b), 2)
        self.zamKolor[2] = round(b * self.calIlosc / (r + g + b), 2)
        print("potrzeba ilosc kazdego koloru: r: " + str(self.zamKolor[0]) + " g: " + str(self.zamKolor[1]) + " b: " + str(self.zamKolor[2]))

    def zwrocZgodeNaPrace(self):
        return self.zgodaNaPrace

    def mieszaj(self, ZbiornikZFarba):
        while self.aktIlosc < self.calIlosc:
            if self.aktKolor[0] < self.zamKolor[0]:
                zbiornikZFarba[0].wlaczPompe(True)
                self.aktKolor.insert(0, round(self.aktKolor[0] + zbiornikZFarba[0].zwrocPrzepływ(), 2))
                self.aktKolor.pop(1)
            else:
                zbiornikZFarba[0].wlaczPompe(False)

            if self.aktKolor[1] < self.zamKolor[1]:
                zbiornikZFarba[1].wlaczPompe(True)
                self.aktKolor.insert(1, round(self.aktKolor[1] + zbiornikZFarba[1].zwrocPrzepływ(), 2))
                self.aktKolor.pop(2)
            else:
                zbiornikZFarba[1].wlaczPompe(False)

            if self.aktKolor[2] < self.zamKolor[2]:
                zbiornikZFarba[2].wlaczPompe(True)
                self.aktKolor.insert(2, round(self.aktKolor[2] + zbiornikZFarba[2].zwrocPrzepływ(), 2))
                self.aktKolor.pop(3)
            else:
                zbiornikZFarba[2].wlaczPompe(False)

            #self.aktIlosc =0
            self.aktIlosc = round(self.aktKolor[0] + self.aktKolor[1] + self.aktKolor[2], 2)

            print("\naktualna ilosc: "+str(self.aktIlosc))
            print("aktualny ilosc poszczegolnego koloru: r: "+str(self.aktKolor[0])+" g: "+str(self.aktKolor[1])+" b: "+str(self.aktKolor[2])+"\n")
        self.zakoncz(zbiornikZFarba, True)

    def zakoncz(self, ZbiornikZFarbą, pozytywnie):
        for zbiornik in ZbiornikZFarbą:
            zbiornik.wlaczPompe(False)

        bladKoloru = (self.zamKolor[0]-self.aktKolor[0])/self.zamKolor[0] + (self.zamKolor[1]-self.aktKolor[1])/self.zamKolor[1] + (self.zamKolor[2]-self.aktKolor[2])/self.zamKolor[2]
        if pozytywnie:
            print("\nmieszanie zakonczone pozytywnie. Błąd bezwzgledny koloru wynosi: "+str(round(abs(bladKoloru), 3)))
        if not pozytywnie:
            print("\nmieszanie niezakonczone. Napraw usterki i sprobuj jescze raz")


if __name__ == "__main__":

    #print("podaj kolor (r g b)")
    zbiornikGlowny = ZbiornikGlowny(True, False)
    zbiornikZFarba = [ZbiornikZFarbą("czerwony", 0.6, False), ZbiornikZFarbą("zielony", 0.1, False), ZbiornikZFarbą("niebieski", 0.1, False)]
    zbiornikGlowny.ustawieniaPoczątkowe(123, 255, 255, 10)

    if zbiornikZFarba[0].zwrocZgodeNaPrace() and zbiornikZFarba[1].zwrocZgodeNaPrace() and zbiornikZFarba[2].zwrocZgodeNaPrace() and zbiornikGlowny.zwrocZgodeNaPrace():
        zbiornikGlowny.mieszaj(zbiornikZFarba)
    else:
        zbiornikGlowny.zakoncz(zbiornikZFarba, False)
