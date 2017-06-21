import unittest
from hell_triangule import HellTriangule


class HellTrianguleTest(unittest.TestCase):
    def test_triangule_with_test_case2_should_return_7273(self):
        table = [map(int, s.split()) for s in open('test_case2.in').readlines()]

        hell_triangule = HellTriangule(table)
        sum = hell_triangule.hell_triangule()

        self.assertEquals(7273, sum, msg='Test with 1 hundred lines')

    def test_triangule_with_test_case1_should_return_26(self):
        table = [map(int, s.split()) for s in open('test_case1.in').readlines()]

        hell_triangule = HellTriangule(table)
        sum = hell_triangule.hell_triangule()

        self.assertEquals(26, sum, msg='Test with Challenge Sample')