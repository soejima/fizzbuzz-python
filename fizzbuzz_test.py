import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_FizzBuzz_not_multiples_of_15(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(2), 2)

    def test_FizzBuzz_multiples_of_3(self):
        self.assertEqual(FizzBuzz(3), "Fizz")
        self.assertEqual(FizzBuzz(9), "Fizz")

    def test_FizzBuzz_5(self):
        self.assertEqual(FizzBuzz(5), "Buzz")

    def test_FizzBuzz_15(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")

    def test_FizzBuzz_10(self):
        self.assertEqual(FizzBuzz(10), "Buzz")


if __name__ == '__main__':
    unittest.main()
