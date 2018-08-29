import sys
sys.path.append('../')
from deck.deck import Deck

class TexasPlayer:
	def __init__(self, buyIn, number):
		self.cash = buyIn
		self.cards = None
		self.id = number

	def bet(self, amount):
		self.cash -= amount


class Texas:
	def __init__(self, num_agents, min_buy_in, max_buy_in, buy_ins):
		"""
		Used to set environment variables
		"""
		self.deck = Deck()
		self.deck.shuffle()

		self.player_count = num_agents
		self.players = []
		self.minBuyIn = min_buy_in
		self.maxBuyIn = max_buy_in

		for i in range(num_agents):
			players.append(TexasPlayer(buy_ins[i], i + 1))

	def step(self, move):
		"""
		Player uses this function to make a move
		"""

	def reset(self):
		"""
		Resets all game variables
		"""
