# Assigned to einav

import cmd
import game


class Shell(cmd.Cmd):
    """Shell for war game"""

    def __init__(self, name):
        super(Shell, self).__init__()
        print("""Type 'start', 'help' or 'long'""")
        self.name = name

    def do_start(self, _):
        print("""You and me will play war game. When you want to draw a card, press enter.
        Whoever has a higher card win both cards.\n""")
        the_game = game.Game()
        the_game.play_short(self.name)
        print("""Type 'start' to start a new game or 'exit' to quit.""")

    def do_long(self, _):
        print("""This is a long version of the game. 
        We will play until one of us has all of the deck.
        When you want to draw a card, press enter.""")
        long_game = game.Game()
        long_game.play_long(self.name)
        print("""\nType 'long' to start a new game or 'exit' to quit.\n""")

    def do_exit(self, _):
        """Exit the game."""
        print("""\nThank you for playing with me! Bye!\n""")
        return True

    def do_restart(self, _):
        print("""You chose to restart the game.""")
        self.do_start(_)

    def do_cheat(self, _):
        print("""Cheater!""")
        cheat_game = game.Game()
        cheat_game.play_short("Cheater", cheat=True)

    def do_long_cheat(self, _):
        print("""Cheater!""")
        cheat_game = game.Game()
        cheat_game.play_long("Cheater", cheat=True)
