from kod import *


def test_multiply_basic():
    assert multiply(2, 5) == 10
    assert multiply(3, 1) == 3
    assert multiply(7, 3) == 21
# facet gadał ze jak wiele assercji to rozbic na wiele metod
# bo wywali na pierwszej assersji i nie pójdzie dalej
# mowil ze roznie mozna to dzielic
# ale wedle mnie lepiej skorzystac z czegos takiegop jak softassertions


def test_multiply_round():
    assert multiply(100, 1.1) == 110

def test_multiply_string():
    assert multiply('5', '3') == 15

def testy_multiply_string_not_to_float():
    assert multiply('4', 'swieta') == None



