"""Tests functionalities of the game class."""
import unittest, unittest.mock, io, random, sys, os
from game import Game


class test_game(unittest.TestCase):
    class HiddenPrints:
        """This class is used to hide the print outputs."""
        def __enter__(self):
            self._original_stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')

        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stdout = self._original_stdout
        
    
    def test_init(self):
        """Tests if the class exists."""
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)
    
    def test_wins(self):
        """Tests if the correct output will occur when the player wins."""
        with self.HiddenPrints():
            res = Game().who_wins(1, 1, 0, 2)
            exp = (None, 2, 0)
            self.assertEqual(res, exp)
    
    def test_loss(self):
        """Tests if the correct output will occur when the player loses."""
        with self.HiddenPrints():
            res = Game().who_wins(1, 1, 2, 0)
            exp = (None, 0, 2)
            self.assertEqual(res, exp)
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        """Used to catch the print output"""
        Game().print_screen(n, 1, 1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    def test_print_true(self):
        """Tests if the print function delivers the correct output
        when the player wins."""
        exp = f"You win.\n" + "You have 1 cards and the computer has 1\n"
        self.assert_stdout(True, exp)
    
    def test_print_false(self):
        """Tests if the print function delivers the correct output
        when the player loses."""
        exp = f"The computer wins!!!\nYou have 1 cards and the computer has 1\n"
        self.assert_stdout(False, exp)
    
    def test_war(self):
        """Tests if a war occurs correctly."""
        random.seed(0xBEEF)
        with self.HiddenPrints():
            res = Game().war(5, 5)
            exp = (None, 1, 9)
            self.assertEqual(res, exp)
    
    def test_input_yes(self):
        with unittest.mock.patch('builtins.input', return_value="yes"):
            res = Game().ask_input()
            exp = True
            self.assertEqual(res, exp)
    
    def test_input_no(self):
        with unittest.mock.patch('builtins.input', return_value="no"):
            res = Game().ask_input()
            exp = False
            self.assertEqual(res, exp)
    
    def test_cheat_short(self):
        res = Game().play_short("Tester", cheat=True)
        pass
        
        