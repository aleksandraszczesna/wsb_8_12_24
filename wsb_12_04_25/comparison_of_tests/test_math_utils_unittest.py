import unittest
from wsb_12_04_25.comparison_of_tests.math_utils import add
from wsb_9_02_25.test_api_post import result


class TestAddFunction(unittest.TestCase):
    #test czy dodawanie 2 + 3 = 5
    def test_add_two_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5) #oczekiwany wynik to 5

if __name__ == '__main__':
    unittest.main()