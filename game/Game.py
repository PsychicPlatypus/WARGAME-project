from Card import Card
class Game:
    def play_short():
        #card Get random card
        computer_cards, human_cards = 26, 26

        for i in range(26):
            print("\n" + "-" * 30)
            #you_card = Card.draw()
            #you_value = Card.value(you_card)
            #computer_card = Card.draw()
            #computer_value = Card.value(computer_card)
            print(f"You: {card_you:<8} Computer: {card_computer}")
            if value_you > value_computer:
                human_cards, computer_cards += 2, -2
                print(
                    f"You win.\nYou have {score_you} cards"
                    f" and the computer has {score_computer}")
            elif value_computer > value_you:
                human_cards, computer_cards += 2, -2
                print(
                    f"The computer wins!!!\nYou have {score_you*2} cards"
                    f" and the computer has {score_computer*2}")
            else:
                outcome = war()
                human_cards, computer_cards += 8, -8 if outcome else -8, 8
        print(f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")

    def play_long():
        #card Get random card
        computer_cards, human_cards = 26, 26
        
        while computer_cards or human_cards > 0:
            print("\n" + "-" * 30)
            #you_card = Card.draw()
            #you_value = Card.value(you_card)
            #computer_card = Card.draw()
            #computer_value = Card.value(computer_card)
            print(f"You: {card_you:<8} Computer: {card_computer}")
            if value_you > value_computer:
                human_cards, computer_cards += 2, -2
                print(
                    f"You win.\nYou have {score_you} cards"
                    f" and the computer has {score_computer}")
            elif value_computer > value_you:
                human_cards, computer_cards += 2, -2
                print(
                    f"The computer wins!!!\nYou have {score_you*2} cards"
                    f" and the computer has {score_computer*2}")
            else:
                outcome = war()
                human_cards, computer_cards += 8, -8 if outcome else -8, 8
        print(
            f"No more cards!\n"
            f"Final score:\nYou: {human_cards}\tComputer: {computer_cards}")

    def war():
        #you_card = Card.draw()
        #you_value = Card.value(you_card)
        #computer_card = Card.draw()
        #computer_value = Card.value(computer_card)
        return value_you > valuecomputer \
            if card_you != card_computer else war()