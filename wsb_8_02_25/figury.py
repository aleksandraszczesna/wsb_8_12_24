import math
from math import pi

class Kwadrat:
    def __init__(self, dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku

    def powierzchnia(self): #oblicza pole kwadratu
        return self.dlugosc_boku ** 2

class Kolo:
    def __init__(self, promien):
        self.promien = promien

    def powierzchnia_kola(self):
        return (self.promien ** 2) * math.pi