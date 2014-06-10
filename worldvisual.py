__author__ = 'Sunjay'

import argparse
import visual as vpy

from worldparser import parse_world

WIDTH = 100
LENGTH = 100

terrain_key = {
	'R': (34,34,34),
	'S': (170, 170, 170),
	'W': (158, 87, 25),
	'G': (0,255,0),
	'L': (105,143,255),
}

def reduce_grid(world_data):
	"""
	Reduces a given set of data and returns a list of squares and their
	dimensions in single units. Each unit represents a square in the
	matrix.

	For example, for this grid:
	AAABB
	AAACB
	BBBBB

	This will return a square for the As, 3 squares for the Bs, and 1 for Cs.
	"""


def draw_world(world_data):
	"""
	Draws a world in 3D
	"""
	for obj in vpy.scene.objects:
		del obj

	box_width = WIDTH // len(world_data[0])
	box_length = LENGTH // len(world_data)

	for row_i, row in enumerate(world_data):
		for col_i, col in enumerate(row):
			color = terrain_key.get(row[col_i], None)
			if color is not None:
				vpy.box(pos=(col_i*box_width, 0, row_i*box_length),
					length=box_length, height=box_width, width=1, color=color)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--file', '-f', '-w', '--world', required=True)

	args = parser.parse_args()

	filename = args.file

	with open(filename) as f:
		world_data = parse_world(f)

	vpy.scene.background = vpy.color.white
	draw_world(world_data)
