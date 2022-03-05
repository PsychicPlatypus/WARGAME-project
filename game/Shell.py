# Assigned to einav

import cmd
import Game

class Shell(cmd.Cmd):
    """Shell for war game"""

    intro = """Welcome to war game! type 'start', 'help' or 'long'"""
    

    def do_start(self, _):
        print("""You and me will play war game. When you want to draw a card, press enter.
        Whoever has a higher card win both cards.""")
        the_game = Game.Game()
        the_game.play_short()
        print("""Type 'start' to start a new game or 'exit' to quit.""")
    
    def do_long(self, _):
        print("""This is a long version of the game. 
        We will play until one of us has all the deck.
        When you want to draw a card, press enter.""")
        long_game = Game.Game()
        long_game.play_long()
        print("""Type 'long' to start a new game or 'exit' to quit.""")
        
        
    def do_exit(self, _):
        """Exit the game."""
        print("""Thank you for playing with me! Bye!""")
        return True