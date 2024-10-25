import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
print("Card:",Card) #Card: <class '__main__.Card'>

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    print(ranks) #['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    print(suits) # ['spades', 'diamonds', 'clubs', 'hearts']
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        print("__init__:",self._cards)
    
    def __len__(self):
        print("__len__ self:",self)
        print("__len__:",len(self._cards))
        return len(self._cards)
    
    def __getitem__(self, position):
        print("__getitem__:",self._cards[position])
        return self._cards[position]
print("------------------")
print("Instanciar Card")
beer_card = Card('7', 'diamonds')
print(beer_card) #Card(rank='7', suit='diamonds')

print("------------------")
print("Len Baralho")
deck = FrenchDeck() # __init__
print(len(deck)) #52 ; __len__
print("------------------")
print("Pegar carta Baralho")
print(deck[0]) #Card(rank='2', suit='spades') ; __getitem__
print(deck[-1]) #Card(rank='A', suit='hearts') ; __getitem__

print("------------------")
print(choice(deck)) #Card(rank='{qualquer numero}}', suit='{qualquer nipe}') ; __len__ , __len__ , __getitem__
print(choice(deck)) #Card(rank='{qualquer numero}}', suit='{qualquer nipe}') ; __len__ , __len__ , __getitem__
print(choice(deck)) #Card(rank='{qualquer numero}}', suit='{qualquer nipe}') ; __len__ , __len__ , __getitem__
print("------------------")

print(deck[:3]) #[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')] ; __getitem__
print(deck[12::13]) #[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')] ; __getitem__

print("------------------")
# doctest: +ELLIPSIS
for card in deck:
    print(card) # Card(rank='2', suit='spades') ..{50 Card}.. Card(rank='A', suit='hearts') ; __getitem__
print("------------------")
for card in reversed(deck):
    print(card) # Card(rank='A', suit='hearts') ..{50 Card}.. Card(rank='2', suit='spades') ; __getitem__
print("------------------")
Card('Q', 'hearts') in deck #True ; __getitem__
Card('7', 'beasts') in deck #False ; __getitem__
print("------------------")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    print("spades_high:",card)
    rank_value = FrenchDeck.ranks.index(card.rank)
    print("rank_value:",rank_value)
    print("rank_value: {} * len(suit_values) {} + suit_values[card.suit] {} = return: {}".format(rank_value,len(suit_values),suit_values[card.suit],rank_value * len(suit_values) + suit_values[card.suit]))
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card) # Card(rank='2', suit='clubs') ..{50 Card}.. Card(rank='A', suit='spades') ; __len__ , __getitem__

