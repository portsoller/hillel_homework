import unittest
from lesson_12.homework_12 import sum_num, avg_value, reverse_string, words_count

class MyTest(unittest.TestCase):

    def test_sum_num_positive_numbers(self):
        result = sum_num(2, 4)
        self.assertEqual(result, 6)

    def test_sum_num_negative_numbers(self):
        result = sum_num(-2, -3)
        self.assertEqual(result, -5)

    def test_sum_num_a_number_with_zero(self):
        result = sum_num(9, 0)
        self.assertEqual(result, 9)

    def test_avg_value_with_floating_result(self):
        lst = [2, 5, 7, 10, 15, 20]
        result = avg_value(lst)
        self.assertAlmostEqual(result, 9.833333333333334)

    def test_avg_value_empty_list_raises_error(self):
        lst = []
        with self.assertRaises(ZeroDivisionError):
            avg_value(lst)

    def test_reverse_string(self):
        result = reverse_string("blablabla")
        self.assertEqual(result, "albalbalb")

    def test_reverse_empty_string(self):
        result = reverse_string("")
        self.assertEqual(result, "")

    def test_reverse_palindrome_case(self):
        result = reverse_string("madam")
        self.assertEqual(result, "madam")

    def test_words_count(self):
        result = words_count('Hello, world!')
        self.assertEqual(result, 2)

    def test_empty_words_count(self):
        result = words_count('')
        self.assertEqual(result, 0)

    def test_words_count_multiple_spaces(self):
        result = words_count('Hello,    world!')
        self.assertEqual(result, 2)

    if __name__ == '__main__':
        unittest.main()