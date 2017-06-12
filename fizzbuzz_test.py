import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_FizzBuzz_1(self):
        self.assertEqual(FizzBuzz(1), 1)
    def test_FizzBuzz_2(self):
        self.assertEqual(FizzBuzz(2), 2)

if __name__ == '__main__':
    unittest.main()
