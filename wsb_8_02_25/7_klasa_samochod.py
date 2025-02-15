class Samochod:
    #definicja klasy
    def __init__(self, marka, model):
        #self reprezentuje nowo tworzoną instancje/obiekt
        self.marka = marka  #ustawiamy atrybut "marka" obiektu
        self.model = model  #ustawiamy atrybut "model" obiektu
        self.predkosc = 0   #ustawiamy prędkość początkową samochodu = 0 km/h
        self.wlaczony_silnik = False
        self.kolor = "czerwony"

    def uruchom_silnik(self):
        print("Silnik został uruchomiony")
        self.wlaczony_silnik = True

    def przyspiesz(self, wartosc):
        #zakładamy, źe atrybut predkosc istnieje
        self.predkosc += wartosc

moj_samochod = Samochod("Toyota", "Yaris")
#moj_samochod.uruchom_silnik()
#moj_samochod.przyspiesz(50)

#print(moj_samochod.wlaczony_silnik)
#print(moj_samochod.predkosc)

moj_samochod_2 = Samochod("BMW", "5")
moj_samochod_2.uruchom_silnik()

print(moj_samochod_2.kolor)