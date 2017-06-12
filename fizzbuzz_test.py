import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_FizzBuzz_1(self):
        self.assertEqual(FizzBuzz(1), 1)
    def test_FizzBuzz_2(self):
        self.assertEqual(FizzBuzz(2), 2)
    def test_FizzBuzz_3(self):
        self.assertEqual(FizzBuzz(3), "Fizz")
    def test_FizzBuzz_5(self):
        self.assertEqual(FizzBuzz(5), "Buzz")
    def test_FizzBuzz_15(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")
    def test_FizzBuzz_9(self):
        self.assertEqual(FizzBuzz(9), "Fizz")


if __name__ == '__main__':
    unittest.main()
