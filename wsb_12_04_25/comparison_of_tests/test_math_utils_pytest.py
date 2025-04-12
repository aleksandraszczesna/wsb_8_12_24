from wsb_12_04_25.comparison_of_tests.math_utils import add

def test_add_two_numbers():
    #testujemy czy dodawanie 2 + 3 = 5
    result = add(2, 3)
    assert result == 5  #oczekiwany wynik jest równy 5