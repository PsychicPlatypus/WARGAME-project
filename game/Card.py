# Assigned to Luan
import random

class Card:
    suits = ['Hearts','Clubs','Spades','Diamonds']

    ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']

    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six' : 6 , 'Seven' :7, 'Eight': 8,'Nine':9,
          'Ten':10,'Jack':11, 'Queen': 12,'King': 13,'Ace':14 }
    
    def random_card():
        random.shuffle(ranks)
        random.shuffle(suits)
        return ranks[0] + " of " + suits[0]

    def value_of_card(input):
        return values.get(input.split(" of ")[0])
