import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_FizzBuzz_not_multiples_of_15(self):
        self.assertEqual(FizzBuzz(1), 1)
        self.assertEqual(FizzBuzz(2), 2)

    def test_FizzBuzz_multiples_of_3(self):
        self.assertEqual(FizzBuzz(3), "Fizz")
        self.assertEqual(FizzBuzz(9), "Fizz")

    def test_FizzBuzz_multiples_of_5(self):
        self.assertEqual(FizzBuzz(5), "Buzz")
        self.assertEqual(FizzBuzz(10), "Buzz")

    def test_FizzBuzz_multiples_of_15(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz(30), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
