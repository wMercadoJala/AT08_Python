from unittest import TestCase
from rodrigo.practice1.main import sum_task


class TestsumTo(TestCase):
    def test_sum_to(self):
        self.assertEqual(55, sum_task.sum_to(10))

    def test_sum_to_50(self):
        self.assertEqual(630, sum_task.sum_to(35))

    def test_sum_to_200(self):
        self.assertEqual(630, sum_task.sum_to(200))
