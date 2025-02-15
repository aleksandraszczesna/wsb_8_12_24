import math
from math import sqrt

class Kalkulator:
    def __init__(self, liczba_1, liczba_2):
        self.liczba_1 = liczba_1
        self.liczba_2 = liczba_2

    def dodawanie(self):
        return self.liczba_1 + self.liczba_2

    def odejmowanie(self):
        return self.liczba_1 - self.liczba_2

    def mnozenie(self ):
        return self.liczba_1 * self.liczba_2

    def dzielenie(self):
        return self.liczba_1 / self.liczba_2

    def potegowanie(self):
        return self.liczba_1 ** self.liczba_2

    def pierwiastkowanie(self):
        return math.sqrt(self.liczba_1)



class KlasaBezParametrowWKonstruktorze:
    def __init__(self):
        self.parametr = "dziś"

    def przyklad(self, liczba):
        print("Kociokwik " + self.parametr + str(liczba))