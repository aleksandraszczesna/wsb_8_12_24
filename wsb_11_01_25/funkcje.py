def pozdrowienia(name1, name2):
    print(f"hello {name1} {name2}")


pozdrowienia("ola", "sz")
pozdrowienia("adam", "małysz")
pozdrowienia("kamil", "stoch")


#ĆW1
def ulubiona_ksiazka(tytuł):
    print(f"Moja ulubiona książka to: {tytuł}")

ulubiona_ksiazka("Hobbit")

#ĆW2
def koszulka(rozmiar, wiadomość):
    print(f"Koszulka o rozmiarze: {rozmiar} i z napisem: {wiadomość}")

koszulka("M", "lubie ciepło")
koszulka(rozmiar= "L", wiadomość= "jagody są spoko")


#RETURN
def dodawanie(a, b, c=' '):
    return a + b

print(dodawanie(2, 7))

#c = ' ' -> nie jest wymagany argument c do wykonania się funkcji

#ĆW3
def panstwa_miasta(miasto, kraj = "Polska"):
    print(f"{miasto} jest w kraju {kraj}")

panstwa_miasta("Warszawa")
panstwa_miasta("Kraków")
panstwa_miasta("Londyn", "Wielka Brytania")

#SŁOWNIK
#czy ludność jest równa zero

def panstwa_miasta(miasto, ludnosc = 0, panstwo = "Polska"):
    miasto_panstwo_slownik = {"państwo" : panstwo, "ludnosc" : ludnosc, "miasto" : miasto}
    if ludnosc == 0:
        ludnosc = "NaN"
    else:
        return miasto_panstwo_slownik

miasto_funkcja = panstwa_miasta("Paryż", 5000000, "Francja")
print(miasto_funkcja)


#ĆW4
def stworz_album(artysta, tytul_albumu, liczba_utworow = None):
    album = {"artysta" : artysta, "tytuł albumu" : tytul_albumu}
    if liczba_utworow is not None:
        album["liczba_utworow"] = liczba_utworow
    return album

album1 = stworz_album("shakira", "tytuł", liczba_utworow= 3)
album2 = stworz_album("rihanna", "tytuł2", liczba_utworow= 6)
album3 = stworz_album("usher", "tytuł3")

print(album1)
print(album2)
print(album3)

# konflciasfafas