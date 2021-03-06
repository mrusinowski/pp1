import unittest

from sum_numbers import sum_even


class TestSumEven(unittest.TestCase):
    def test_sum_even(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z dowolnego przedziału m,n
        m = 1
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_fromeven(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie m parzyste
        m = 2
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)

    def test_sum_even_nm(self):
        # Testuj sumę liczb naturalnych parzystych 
        # z przedziału m,n, gdzie n<m
        m = 5
        n = 2
        result = sum_even(m,n)
        self.assertEqual(result, 0)
        
    def test_sum_even_toeven(self):
        # Testuj sumę liczb naturalnych parzystych
        # z przedziału m,n, gdzie n parzyste
        m = 1
        n = 6
        result = sum_even(m,n)
        self.assertEqual(result, 12)
        
    def test_sum_even_fromnegative(self):
        # Testuj sumę liczb naturalnych parzystych
        # z przedziału m,n, gdzie m ujemne
        m = -2
        n = 5
        result = sum_even(m,n)
        self.assertEqual(result, 6)
        
    def test_sum_even_string(self):
        # Testuj działanie funkcji
        # gdy m lub n są łancuchami znakowymi
        m = 'jeden'
        n = 'osiem'
        result = sum_even(m,n)
        self.assertEqual(result, -1)



if __name__ == '__main__':
    unittest.main()