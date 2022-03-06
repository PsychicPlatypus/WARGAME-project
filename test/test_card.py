import unittest
from Card.Card import Card

class test_card (unittest.TestCase):
    def test__init__(self):
        res = Card()
        exp = Card
        self.assertIsInstance(exp, res)

