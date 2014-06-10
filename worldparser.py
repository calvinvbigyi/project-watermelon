__author__ = 'Sunjay'

import numpy as np

def parse_world(fp):
	"""
	Parses a file into a world
	"""
	world_data = map(list, map(str.strip, filter(None, fp.readlines())))
	assert(all(len(r) == len(world_data[0]) for r in world_data))

	return np.array(world_data)

class World:

	def __init__(self, data=None):
		if data is None:
			data = []

		self.data = data

	def __iter__(self):
		return iter(self.data)

	def parse_world(self, fp):
		"""
		Parses a world file and *sets* it as this world's data

		Data cannot simply be extended due to consistency and
		dimensional problems.
		"""
		self.data = parse_world(fp)

		return self.data