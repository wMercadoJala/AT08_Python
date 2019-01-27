from unittest import TestCase

from rodrigo.practice1.main import days_task


class TestdaysInMonth(TestCase):
    """Test Class for the calendar"""

    def test_days_in_month(self):
        """
        Test for wrong input.
        """
        self.assertEqual("Error, please check the input", days_task.days_in_month("Fe"))

    def test_july_month(self):
        """
        Test for correct month.
        """
        self.assertEqual(31, days_task.days_in_month("July"))

    def test_february_month(self):
        """
        Test for february who had 28 days.
        """
        self.assertEqual(28, days_task.days_in_month("February"))
