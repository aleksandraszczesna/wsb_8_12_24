import time #moduł pozwalający mierzyć czas i usypiać program

def slow_function():
    print("Rozpoczynam działanie slow_function...")
    time.sleep(3)    #uśpienie programu na 3 sekundy -> symulacja czegoś czasochłonnego
    print("Zakończyłem działanie slow_function")

print("Zaczynam pomiar czasu")
start_time = time.time()    #znacznik czasu w momencie zakończenia działania pomiaru #time.time() pobiera aktualny czas

slow_function()

end_time = time.time()  #znacznik czasu w momencie zakończenia działania pomiaru

elapsed_time = end_time - start_time    #różnica czasu, pomiędzy wywołaniem, a zakończeniem funkcji

print(f"Funckja wykonała się w czasie {elapsed_time} sekund")