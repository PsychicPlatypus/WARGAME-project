from Card import Card
class Game():
    def play_short(self):
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
                print(
                    f"You win.\nYou have {human_cards} cards"
                    f" and the computer has {computer_cards}")
            elif value_computer > value_you:
                human_cards -= 2
                computer_cards += 2
                print(
                    f"The computer wins!!!\nYou have {human_cards} cards"
                    f" and the computer has {computer_cards}")
            else:
                if computer_cards < 8 or human_cards < 8:
                    print("We don't have enough cards for war")
                    pass
                else:
                    if (outcome := self.war()):
                        human_cards += 8
                        computer_cards -= 8
                    else:
                        human_cards -= 8
                        computer_cards += 8
        print(f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")

    def play_long(self):
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
                print(
                    f"You win.\nYou have {human_cards} cards"
                    f" and the computer has {computer_cards}")
            elif value_computer > value_you:
                human_cards -= 2
                computer_cards += 2
                print(
                    f"The computer wins!!!\nYou have {human_cards} cards"
                    f" and the computer has {computer_cards}")
            else:
                if computer_cards < 8 or human_cards < 8:
                    print("We don't have enough cards for war")
                    pass
                else:
                    if (outcome := self.war()):
                        human_cards += 8
                        computer_cards -= 8
                    else:
                        human_cards -= 8
                        computer_cards += 8
        print(
            f"No more cards!\n"
            f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")

    #def print_score(self, val_you, val):
        

    def war(self):
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
    