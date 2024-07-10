import unittest
from sum_even_numbers import sum_of_even_numbers


class TestSumOfEvenNumbers(unittest.TestCase):

    def test_mixed_numbers(self) -> None:
        self.assertEqual(sum_of_even_numbers([1, 2, 3, 4, 5]), 6)

    def test_all_even_numbers(self) -> None:
        self.assertEqual(sum_of_even_numbers([2, 4, 6, 8, 10]), 30)

    def test_all_odd_numbers(self) -> None:
        self.assertEqual(sum_of_even_numbers([1, 3, 5, 7, 9]), 0)

    def test_negative_even_and_odd_numbers(self) -> None:
        self.assertEqual(sum_of_even_numbers([-2, -3, -4, -5, -6]), -12)

    def test_empty_list(self) -> None:
        self.assertEqual(sum_of_even_numbers([]), 0)

    def test_single_even_number(self) -> None:
        self.assertEqual(sum_of_even_numbers([2]), 2)

    def test_single_odd_number(self) -> None:
        self.assertEqual(sum_of_even_numbers([3]), 0)

    def test_list_with_zero(self) -> None:
        self.assertEqual(sum_of_even_numbers([0, 1, 2, 3, 4, 5]), 6)

    def test_large_even_numbers(self) -> None:
        self.assertEqual(sum_of_even_numbers([1000000, 2000000, 3000000]), 6000000)


if __name__ == '__main__':
    unittest.main()
