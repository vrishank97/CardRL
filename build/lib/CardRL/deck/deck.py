import numpy as np
class Deck:
	def __init__(self):
		"""
		generates a pair list with 1-4 packs
		and 1-13 cards of each pack
		"""
		self.x = np.empty([52,2],dtype = int)

		for i in range(52):
			self.x[i][0] = i/13 +1
			self.x[i][1] = i%13+1

	def refill(self):
		self.x = np.empty([52,2],dtype = int)

		for i in range(52):
			self.x[i][0] = i/13 +1
			self.x[i][1] = i%13+1

	def shuffle(self):
		"""
		Uses numpy to shuffle cards(stored in numpy array)
		fix the random seed for this in init, to let people reproduce results
		"""
		np.random.shuffle(self.x)
		# np.savetxt('shuffle.out',self.x,fmt = '%0.1d',delimiter=',')

	def __str__(self):
		return str(self.x)

	def deal(self, num_cards):
		"""
		Deals num_cards
		"""
		if num_cards>len(self.x):
			raise ValueError("Insufficient cards in deck")

		else:
			cards = self.x[:num_cards]
			self.x = self.x[num_cards:]
			return cards
