import unittest
from game.game import Game


class test_game(unittest.TestCase):
    def test_init(self):
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)
