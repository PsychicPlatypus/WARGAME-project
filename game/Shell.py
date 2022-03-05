# Assigned to einav

import cmd
import game

class Shell(cmd.Cmd):
    """Shell for war game"""

    intro = """
    
░██╗░░░░░░░██╗░█████╗░██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔══██╗██╔══██╗  ██╔════╝░██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝███████║██████╔╝  ██║░░██╗░███████║██╔████╔██║█████╗░░
░░████╔═████║░██╔══██║██╔══██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

       \nWelcome to war game! type 'start', 'help' or 'long'\n"""  

    def do_start(self, _):
        print("""You and me will play war game. When you want to draw a card, press enter.
        Whoever has a higher card win both cards.\n""")
        the_game = game.Game()
        the_game.play_short()
        print("""Type 'start' to start a new game or 'exit' to quit.""")
    
    def do_long(self, _):
        print("""This is a long version of the game. 
        We will play until one of us has all the deck.
        When you want to draw a card, press enter.""")
        long_game = game.Game()
        long_game.play_long()
        print("""\nType 'long' to start a new game or 'exit' to quit.\n""")
        
        
    def do_exit(self, _):
        """Exit the game."""
        print("""\nThank you for playing with me! Bye!\n""")
        return True


    def do_restart(self, _):
        print("""You chose to restart the game.""")
        self.do_start(_)


    def do_cheat(self, _):
        pass