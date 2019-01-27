from unittest import TestCase

from rodrigo.practice1.main import sum_task


class TestsumTo(TestCase):
    """Class for test the successive sum."""

    def test_sum_to(self):
        """
        Test for number smaller than 35.
        """
        self.assertEqual(55, sum_task.sum_to(10))

    def test_sum_to_50(self):
        """
        Test for number equal to 35.
        """
        self.assertEqual(630, sum_task.sum_to(35))

    def test_sum_to_200(self):
        """
        Test for number greater than 35, should sum until 35.
        """
        self.assertEqual(630, sum_task.sum_to(200))
