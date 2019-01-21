from unittest import TestCase

from rodrigo.practice1.main import DaysTask


class TestDays_in_month(TestCase):
    def test_days_in_month(self):
        self.assertEqual("Error, please check the input", DaysTask.days_in_month("Fe"))

    def test_july_month(self):
        self.assertEqual(31, DaysTask.days_in_month("July"))

    def test_february_month(self):
        self.assertEqual(28, DaysTask.days_in_month("February"))
