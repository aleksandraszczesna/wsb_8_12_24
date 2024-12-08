#programowanie obietkowe - cały python to obiektówka
#obiektowka = tworzymy zestw danych = obiekt i mowimy co na tym mozemy zrobic, a czego nie mozna


#przykład
class Auto:
    def __init__(self, kolor, wiek): #metoda init inicjalizuje = zbior parametrow z wartosciami
        self.kolor = kolor
        self.ilosc_paliwa = 10
        self.kondycja = 5
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2024 - wiek
#self - stworzone zmienne w funkcji mają być dostępne w innych funkcjach tej samej klasy
    def zasieg(self):
        zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def zmien_tryb(self, tryb):
        if tryb == 'eco':
            print('wlaczono tryb ekonomiczny')
                self.tryb_ekonomiczny == True
                self.spalanie_na_100 == 8
        elif tryb == 'normal':
            print('wlaczono tryb normalny')

car1 = Auto('red', 12)   #obiekt klasy auto
car2 = Auto('blue', 1)

print(car1.rocznik)
car1.rocznik = 2004
print(car1.rocznik)

print(car2.ilosc_paliwa)
print(car2.zasieg())
