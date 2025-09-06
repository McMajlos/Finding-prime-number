import unittest
from main import is_prime_l1
from main import is_prime_l2
from main import is_prime_l3

# class TestIsPrimeL1(unittest.TestCase):
#     def test_small_primes(self):
#         self.assertTrue(is_prime_l1(2))
#         self.assertTrue(is_prime_l1(3))
#         self.assertTrue(is_prime_l1(5))
#         self.assertTrue(is_prime_l1(101))
#     def test_non_primes(self):
#         self.assertFalse(is_prime_l1(4))
#         self.assertFalse(is_prime_l1(100))
#         self.assertFalse(is_prime_l1(678))
#         self.assertFalse(is_prime_l1(882))
    
# if __name__ == "__main__":
#     unittest.main()    




class TestIsPrimeL2(unittest.TestCase):
    def test_small_primes(self):
        self.assertTrue(is_prime_l2(5))


class TestIsPrimeL3(unittest.TestCase):
    def test_small_primes(self):
        self.assertTrue(is_prime_l3(3))
        self.assertTrue(is_prime_l3(5))


if __name__ == "__main__":
    unittest.main()    