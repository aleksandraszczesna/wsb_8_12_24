import time #time – Jest to wbudowana biblioteka Pythona, która pozwala na manipulowanie czasem. W tym przypadku używana jest funkcja sleep, aby na chwilę "zatrzymać" wykonanie programu.
import pytest   #pytest – Jest to popularna biblioteka do testowania w Pythonie, która oferuje wiele narzędzi do pisania testów jednostkowych oraz integracyjnych. W tym przypadku wykorzystujemy ją do uruchamiania benchmarków.

def slow_function():    #funkcja ktora symuluje wolne dzialanie, usypiamy program na 0,5 sek
    time.sleep(0.5)
    return "Done"   #Po upływie tej przerwy funkcja zwraca napis "Done".

@pytest.mark.benchmark  #dekorator, który oznacza, że ten test będzie wykonywał benchmark (mierzenie czasu wykonania).
def test_slow_function(benchmark):  #uruchamia finkcję slow_function i mierzy czas jej wykonania
    """
    funkcja która przeprowadzi test sprawdzjący ile średnio zajmuje wykonanie funkcji slow_function
    """

    result = benchmark(slow_function)   #Na końcu testu sprawdzamy, czy wynik funkcji slow_function to dokładnie "Done". Jest to standardowy sposób sprawdzenia, czy funkcja działa poprawnie, niezależnie od jej czasu wykonania.
    assert result == "Done"


#slow_function symuluje opóźnienie (0,5 sekundy).
#test_slow_function używa narzędzia benchmark z pytest, aby zmierzyć czas działania slow_function.
#Test sprawdza, czy wynik działania tej funkcji jest równy "Done" (potwierdza, że funkcja działa poprawnie).
#Dodatkowo, dzięki użyciu @pytest.mark.benchmark, możemy uzyskać szczegółowe dane na temat czasu wykonania tej funkcji.