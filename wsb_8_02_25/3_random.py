import random   #moduł do losowania liczb

#wylosujmy liczbę z przedziału 1 do 10
losowa = random.randint(1, 10)
print(f"Wynik losowania z zakresu 1 do 10 to: {losowa}")

#wylosujmy 5 liczb z zakresu od 1 do 10 i zapiszmy je do listy
losowe_liczby = random.sample(range(1, 11), 5)
print(f"Pięć losowych liczb z zakresu od 1 do 10 to: {losowe_liczby}")

