import sys
import random

print("To jest mój pierwszy program w pythonie")

#zmienna - kontener do przechowywania jakiś wartości
#nazwa zmiennej jest jak etykieta dla tej wartości

nick = "Trener Python"
print(nick)

#nazwa zmiennej może zawierać litery i liczby
#nazwa zmiennej nie może zaczynać się od liczb

#istnieje 5 typów danych: numbers (liczby), strings (łańcuchy znaków), list (listy), tuples (krotki) i dictionaries (słowniki)
#można przechowywać dowolne z nich w tej samej zmiennej

liczba = 15
print(liczba)

#operatory arytmetyczne
#dodawanie -> +
#odejmowanie -> -
#mnożenie -> *
#dzielenie -> /
#reszta z dzielenia/modulo -> %

#kolejność wykonywania działań tak samo jak w matematyce

#aby napisać coś w cudzysłowie, użyj \"
motto = "motto: \"aby nauczyć się programować, należy pisać programy\""
print(motto)

#wielowierszowa zmienna
wielowierszowe_motto = """aby nauczyć się programować,
należy pisać programy"""
print(wielowierszowe_motto)

#aby osiadzić stringa na wyjściu w consoli użyj %s
print("%s %s" % ("lubie to ", motto))

#aby nie printować nowe linie użyj end= " "
print("lubię", end=" ")
print("lubię pythona")

#może wyświetlić ciąg wiele razy za pomocą *
print("\n" *5)

#\n to pusta linijka w consoli

#lista - umozliwia tworzenie listy wartości i manipulowanie nimi
#każda wartość posiada indeks, pierwszy zaczyna się od 0
lista_zakupów = ["jaja", "ser", "pomidorki", "chilli"]
print("najważniejszy składnik jajecznicy to: ", lista_zakupów[0])
print("dodatkowy składnik jajecznicy to: ", lista_zakupów[2])

#zmiana wartości przechowywania w polu listy
lista_zakupów[1] = "masło"
print(lista_zakupów)

#można zmienić wartości tak, aby uzyskac podzbiór listy
print(lista_zakupów[1:3])

#można umieścić dowolny typ danych na liście, łącznie z listą
inne_czynności = ['sprzątanie', 'nauka', 'gotowanie']
do_zrobienia = [inne_czynności, lista_zakupów]
print(do_zrobienia)

#pobierz drugą pozycję na drugiej liście
print(do_zrobienia[1][1])

#dodaj wartości za pomocą append
lista_zakupów.append("cytryna")
print(do_zrobienia)

#wstawianie elementów pod danym indeksem
lista_zakupów.insert(3, 'ketchup')
print(do_zrobienia)

#usuwanie pozycji z listy
lista_zakupów.remove("ketchup")
print(lista_zakupów)

#sortowanie pozycji na liście
lista_zakupów.sort()
print(lista_zakupów)

#odwrócenie sortowania
lista_zakupów.reverse()
print(lista_zakupów)

#usuwanie elementów o okreslonym indeksie
del lista_zakupów[4]
print(lista_zakupów)

#łączenie list za pomocą +
do_zrobienia = inne_czynności + lista_zakupów
print(do_zrobienia)

#pozyskiwanie długości listy
print(len(do_zrobienia))

#pozyskiwanie maksymalnej pozycji nas liście
print(max(do_zrobienia))

#pozyskiwanei minimalnej pozycji na liście
print(min(do_zrobienia))

#krotka - lista, której nie da się modyfikować
pi_krotka = (3,1,4,1,5,9)

#konwertuj krotkę na listę
nowa_krotka = list(pi_krotka)

#krotki mają len, min, max
print(len(pi_krotka))

#słowniki - wartości z unikalnym kluczem dla każdej wartości
super_bohaterowie = {'batman':'superman',
                    'iron men' :'robin',
                    'wizard':'deadpool'}
print(super_bohaterowie)

#usuń wpis
del super_bohaterowie['wizard']
print(super_bohaterowie)

#zastąp wartość
super_bohaterowie['wizard'] = 'spider man'
print(super_bohaterowie)

#wyświetl liczbę elementów w słowniku
print(len(super_bohaterowie))

#uzyskaj listę kluczy słownika
print(super_bohaterowie.keys())

#uzyskaj listę wartości słownikowych
print(super_bohaterowie.values())

#warunki - instrukcje if, elif, else
#if wykona kod, jeśli warunek zostanie spełniony
#operatory porównania: ==, !=, >, <, <=, >=
wiek = 28
if wiek > 18:
    print("możesz robić prawko")
else:
    print("poczekaj do 18")

#pętle for - pozwala wykonywać akcję określoną liczbę razy
for x in range(8, 20):
    print(x, '', end="")

print('\n')

#pętla for w celu przejścia przez listę
lista_zakupów = ['jaja', 'ser', 'pomidory', 'chilli']

for y in lista_zakupów:
    print(y)

#można zdefiniować listę numerów do przejścia przez wszystkie elementy
lista_liczb = [[2, 5, 20], [20, 50, 100], [200, 500, 1000]];

for x in range(0, 3):
    for y in range(0, 3):
        print(lista_liczb[x][y])

#pętla while - gdy wiesz z wyprzedzeniem ile razy pętla ma się wykonać
losowa_liczba = random.randrange(0, 1000)

while(losowa_liczba != 500):
    print(losowa_liczba)
    losowa_liczba = random.randrange(0, 1000)

#interator pętli while nie jest zdefiniowany przed pętlą
i = 0
while(i <= 10):
    if (i%2 == 0):
        print(i)
    elif (i == 9):
        break   #wymusza zakończenie pętli
    else:
        i += 1  #skrót dla i = i + 1
        continue    #przechodzi do następnej iteracji pętli

    i += 1

#funkcje - pozwalają na ponowne użycie i napisanie czytelnego kodu
# def (zdefiniuj) + nazwa funkcji i otrzymane parametry
# return - zwraca parametr lub wartość

def dodaj_liczby(liczba1, liczba2):
    suma = liczba1 + liczba2
    return suma

print(dodaj_liczby(5,10))

#jeśli zdefiniujesz zmienną poza funkcją, będzie ona działać w każdym miejscu
suma = 0

def roznica_liczba(liczba1, liczba2):
    roznica = liczba1 - liczba2
    return roznica

print(roznica_liczba(21, 6))

#Input / output
print("Podaj swoje imię: ")

#przechowuje wszystko co zostało wpisane aż do wywołania przez ENTER
imie = sys.stdin.readline()

print('Cześć, ', imie)

#stringi
dlugi_string = "na na na na na na na na na na na na na na na na na na na na na na na na na na na na"

#pobierz pierwszed 4 znaki
print(dlugi_string[0:4])

#wyświetl ostatnie 5 znaków
print(dlugi_string[-5:])

#wszystko do ostatnich 5 znaków
print(dlugi_string[:-5])

#łączenie części stringa
print(dlugi_string[:4] + '+ cytat')

#pierwsza litera jest wielka literą
print(dlugi_string.capitalize())

#zwraca indeks początku łańcucha
#rozróżniana wielkość liter
print(dlugi_string.find("na na"))

#zwraca prawdę, jeśli wszystkie znaki sa literami
print(dlugi_string.isalpha())

#zwraca długość stringa
print(len(dlugi_string))

#zastap pierwsze slowo drugim
print(dlugi_string.replace("na", "be"))

#usuwanie spacji z przodu i konca
print((dlugi_string.strip()))

#podziel ciag na liste na podstawie podanego separatora
cytat_lista = dlugi_string.split(" ")
print(cytat_lista)

#pliki input/output
testowy_plik = open('test.txt', 'wb')

#pobieranie używanego trybu pliku
print(testowy_plik.mode)

#wypisz tekst do pliku z nową linią
testowy_plik.write(bytes("tekst\n ", "UTF-8"))

#zamyka plik
testowy_plik.close()

#otwiera plik do odczytu i zapisu
testowy_plik = open("test.txt", "r+")

#przeczytaj / wyswiel tekst z pliku
testowy_plik = testowy_plik.read()
print(testowy_plik)

print(testowy_plik.find('zdanie'))

#klasy i obiekty
#koncepcja programowania obiektowego (OOP) pozwala nam modelować rzeczy ze świata rzeczywistego za pomocą kodu
#każdy obiekt ma pewne atrybuty (np. kolor), które są zmiennymi obiektu

#obiekt jest zbiorem danych (zmiennych) i metod (funkcji), które działaja na tych danych
class czlowiek:
    __imie = None
    __wzrost = None
    __waga = None
    __jezyk = None

#konstruktrot jest wywoływany w celu ustawienia lub zainicjowania obiektu
#self - pozwala obiektowi odwoływac się do siebie wewnątrz

#"None" oznacza brak wartości

    def __init__(self, imie, wzrost, waga, jezyk):
        self.__imie = imie
        self.__wzrost = wzrost
        self.__waga = waga
        self.__jezyk = jezyk

    def ustaw_imie(self, imie):
        self.__imie = imie

    def ustaw_wzrost(self, wzrost):
        self.__wzrost = wzrost

    def ustaw_wage(self, waga):
        self.__waga = waga

    def ustaw_jezyk(self, jezyk):
        self.__jezyk = jezyk

    def pobierz_imie(self):
        return self.__imie

    def pobierz_wzrost(self):
        return self.__wzrost

    def pobierz_wage(self):
        return self.__waga

    def pobierz_jezyk(self):
        return self.__jezyk

    def pobierz_typ(self):
        print('czlowiek')

    def naString(self):
        return "{} ma {} cm wzrostu i waży {} kg, a programuje w {}".format(self.__imie, self.__wzrost, self.__waga, self.__jezyk)

#jak stworzyć człowieka
programista = czlowiek('Kris', 175, 70, 'python')
print(programista.naString())

#nie możesz uzyskac bezpośredniego dostepu do tejw artosci poniewaz jest ona prywatna
#print(programista.__imie)
#print(programista.imie)

#inheritance / dziedziczenie
#możesz dziedziczyć wszytskie zmienne i metody z innej klasy
class Kierowca(czlowiek):
    __firma = None

    def __init__(self, imie, wzrost, waga, jezyk, firma):
        self.__firma = firma
        self.__pobierz_typ = None

        #jak wywołać konstruktora superklasy
        super(Kierowca, self).__init__(imie, wzrost, waga, jezyk)

    def ustaw_firme(self, firma):
        self.__firma = firma

    def pobierz_firme(self):
        return self.__firma

    def pobierz_typ(self):
        print("Kierowca")

    def naString(self):
        return "{} ma {} cm wzrostu i waży {} kg, a programuje w {}. Pracuje w firmie {}".format(self.pobierz_imie(),
                                                                                                 self.pobierz_wzrost(),
                                                                                                 self.pobierz_wage(),
                                                                                                 self.pobierz_jezyk(),
                                                                                                 self.__firma)

mario = Kierowca('mariusz', 190, 86, "java", "dhl")
print(mario.naString())