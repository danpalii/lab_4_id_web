from django.test import TestCase
from .views import sum_two_numbers, differ_two_numbers, multiple_two_numbers, division_two_numbers


class Test1(TestCase):
    def test_sum(self):
        x = 2
        y = 2
        sum = sum_two_numbers(x, y)
        self.assertEqual(sum, 4)

    def test_differ(self):
        x = 4
        y = 1
        differ = differ_two_numbers(x, y)
        self.assertEqual(differ, 3)

    def test_multiple(self):
        x = 3
        y = 2
        multiple = multiple_two_numbers(x, y)
        self.assertEqual(multiple, 6)

    def test_division(self):
        x = 10
        y = 2
        division = division_two_numbers(x, y)
        self.assertEqual(division, 5)

