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

	def shuffle(self):
		"""
		Uses numpy to shuffle cards(stored in numpy array)
		fix the random seed for this in init, to let people reproduce results
		"""
		self.x = np.random.shuffle(self.x)
		np.savetxt('shuffle.out',x,fmt = '%0.1d',delimiter=',')
