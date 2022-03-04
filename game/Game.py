"""The logic behind the War card game."""
from Card import Card


class Game:
    """Placeholder for docstring."""

    def play_short(self):
        """Plays the game for only 26 turns, shorter version."""
        computer_cards, human_cards = 26, 26

        for i in range(26):
            if computer_cards <= 0 or human_cards <= 0:
                break
            c = Card()
            print("\n" + "-" * 30)
            card_you = c.random_card()
            value_you = c.value_of_card(card_you)
            card_computer = c.random_card()
            value_computer = c.value_of_card(card_computer)
            print(f"You: {card_you:<8} Computer: {card_computer}")
            if value_you > value_computer:
                human_cards += 2
                computer_cards -= 2
                self.print_screen(True, human_cards, computer_cards)
            elif value_computer > value_you:
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
        print(f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")

    def play_long(self):
        """Plays the game until the entire deck runs out, long version."""
        computer_cards, human_cards = 26, 26

        while computer_cards or human_cards > 0:
            if computer_cards <= 0 or human_cards <= 0:
                break
            c = Card()
            print("\n" + "-" * 30)
            card_you = c.random_card()
            value_you = c.value_of_card(card_you)
            card_computer = c.random_card()
            value_computer = c.value_of_card(card_computer)
            print(f"You: {card_you:<8} Computer: {card_computer}")
            if value_you > value_computer:
                human_cards += 2
                computer_cards -= 2
                self.print_screen(True, human_cards, computer_cards)
            elif value_computer > value_you:
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
        print(
            f"No more cards!\n"
            f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")

    def print_screen(self, arg, human_cards, computer_cards):
        """Repetitive print function."""
        match arg:
            case True:
                print(
                    f"You win.\nYou have {human_cards} cards"
                    f" and the computer has {computer_cards}")
            case False:
                print(
                    f"The computer wins!!!\nYou have {human_cards} cards"
                    f" and the computer has {computer_cards}")

    def war(self):
        """In case of a draw."""
        print("\nSAME CARDS, WAR!")
        c = Card()
        card_you = c.random_card()
        value_you = c.value_of_card(card_you)
        card_computer = c.random_card()
        value_computer = c.value_of_card(card_computer)
        return value_you > value_computer \
            if card_you != card_computer else self.war()


if __name__ == "__main__":
    test = Game()
    test.play_long()
