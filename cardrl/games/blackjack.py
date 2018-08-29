import sys
sys.path.append('../')
from deck.deck import Deck

class BlackJack:

	def __init__(self, players):
		self.deck = Deck()

		self.numPlayers = players
		self.cards = []

		for i in range(players):
			self.cards.append(self.deck.deal(1)[0])

		for i in range(players):
			self.cards[i].append(self.deck.deal(1)[0])

		print(self.cards)

	def step(self):
		pass

b = BlackJack(3)