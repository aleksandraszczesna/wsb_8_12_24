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

