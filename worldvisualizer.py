__author__ = 'Sunjay'

import argparse

from Tkinter import *

from worldparser import parse_world

terrain_key = {
	'R': '#222222',
	'S': '#AAAAAA',
	'W': '#9e5719',
	'G': 'green',
	'L': '#698fff',
}

def show_world(canvas, world):
	"""
	Draws world on canvas
	"""

	width = canvas.winfo_width()
	if width <= 1:
		width = int(canvas["width"])

	height = canvas.winfo_height()
	if height <= 1:
		height = int(canvas["height"])

	box_width = width // len(world[0])
	box_height = height // len(world)

	for row_i, row in enumerate(world):
		for col_i, col in enumerate(row):
			color = terrain_key.get(row[col_i], None)
			if color is not None:
				canvas.create_rectangle(col_i*box_width + 1, row_i*box_height + 1,
					(col_i+1)*box_width + 1, (row_i+1)*box_height + 1, fill=color)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--file', '-f', '-w', '--world', required=True)

	args = parser.parse_args()

	filename = args.file

	master = Tk()
	master.title("World Map")

	canvas = Canvas(master, width=500, height=500, bg="white")
	canvas.pack(fill=BOTH, expand=YES)

	def redraw(event=None):
		print "Redraw"
		with open(filename, 'r') as f:
			try:
				world_data = parse_world(f)
			except AssertionError:
				print "Invalid dimensions"
				return

		canvas.delete(ALL)
		show_world(canvas, world_data)

	master.bind("<Control-r>", redraw)
	master.bind("<Configure>", redraw)

	master.mainloop()