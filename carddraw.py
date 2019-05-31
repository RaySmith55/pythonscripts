import random

card = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Clubs', 'Spades','Hearts','Diamonds']

print(random.choice(card) + ' of ' + random.choice(suits))