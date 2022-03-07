"""The logic behind the War card game."""
from card import Card
from highscores import highscores


class Game:
    """Placeholder for docstring."""

    def play_short(self):
        """Plays the game for only 26 turns, shorter version."""
        computer_cards, human_cards, counter = 26, 26, 0

        for i in range(26):
            if computer_cards <= 0 or human_cards <= 0:
                break
            c = Card()
            print("\n" + "-" * 30)
            card_you, card_computer = c.random_card(), c.random_card()
            val_you, val_com = c.value(card_you), c.value(card_computer)
            print(f"You: {card_you:<8} Computer: {card_computer}")
            if val_you > val_com:
                human_cards += 2
                computer_cards -= 2
                self.print_screen(True, human_cards, computer_cards)
            elif val_com > val_you:
                human_cards -= 2
                computer_cards += 2
                self.print_screen(False, human_cards, computer_cards)
            else:
                if computer_cards < 8 or human_cards < 8:
                    print("We don't have enough cards for war")
                    pass
                else:
                    if (outcome := self.war()):
                        human_cards += 8
                        computer_cards -= 8
                        self.print_screen(outcome, human_cards, computer_cards)
                    else:
                        human_cards -= 8
                        computer_cards += 8
                        self.print_screen(outcome, human_cards, computer_cards)
            counter += 1
        print(f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")
        highscores().short_scores("Dzenis", human_cards, counter)

    def play_long(self):
        """Plays the game until the entire deck runs out, long version."""
        computer_cards, human_cards, counter = 26, 26, 0

        while computer_cards or human_cards > 0:
            if computer_cards <= 0 or human_cards <= 0:
                break
            c = Card()
            print("\n" + "-" * 30)
            card_you, card_computer = c.random_card(), c.random_card()
            val_you, val_com = c.value(card_you), c.value(card_computer)
            print(f"You: {card_you:<8} Computer: {card_computer}")
            if val_you > val_com:
                human_cards += 2
                computer_cards -= 2
                self.print_screen(True, human_cards, computer_cards)
            elif val_com > val_you:
                human_cards -= 2
                computer_cards += 2
                self.print_screen(False, human_cards, computer_cards)
            else:
                if computer_cards < 8 or human_cards < 8:
                    print("We don't have enough cards for war")
                    pass
                else:
                    if (outcome := self.war()):
                        human_cards += 8
                        computer_cards -= 8
                        self.print_screen(outcome, human_cards, computer_cards)
                    else:
                        human_cards -= 8
                        computer_cards += 8
                        self.print_screen(outcome, human_cards, computer_cards)
            counter += 1
        print(
            f"No more cards!\n"
            f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")
        highscores().long_scores("Dzenis", human_cards, counter)

    def ask_input() -> None:
        arg = input("Would you like to continue?: ")

    def print_screen(self, arg, human_cards, computer_cards):
        """Repetitive print function."""
        if arg:
            print(
                f"You win.\nYou have {human_cards} cards"
                f" and the computer has {computer_cards}")
        else:
            print(
                f"The computer wins!!!\nYou have {human_cards} cards"
                f" and the computer has {computer_cards}")

    def war(self) -> str:
        """In case of a draw."""
        print("\nSAME CARDS, WAR!")
        c = Card()
        card_you, card_computer = c.random_card(), c.random_card()
        val_you, val_com = c.value(card_you), c.value(card_computer)
        return val_you > val_com \
            if card_you != card_computer else self.war()