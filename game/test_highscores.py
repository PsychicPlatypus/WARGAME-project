import unittest
import highscores

class Test_highscores(unittest.TestCase):
    
    def test_init(self):
        res = highscores()
        exp = highscores
        self.assertIsInstance(res, exp)

if __name__ == '__main__':
    unittest.main()