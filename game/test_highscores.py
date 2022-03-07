import unittest
import highscores

class Test_highscores(unittest.TestCase):
    
    def test_init(self):
        res = highscores.highscores()
        exp = highscores.highscores
        self.assertIsInstance(res, exp)

if __name__ == '__main__':
    unittest.main()