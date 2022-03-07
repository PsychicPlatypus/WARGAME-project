import unittest
from Card import Card

class test_card (unittest.TestCase):
    def test__init__(self):
        res = Card()
        exp = Card
        self.assertIsInstance(res, exp)

