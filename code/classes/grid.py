import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from overlap_check import *
from houses import *
from water import *

class Area(object):
	def __init__(self):
		self.width = 360
		self.height = 320

	# create grid of 360*320 filled with 0's
	def make_basic_grid(self):
		basic_grid = [["0"]*self.width for x in range(self.height)]
		return basic_grid

	# update the grid with house, water or space
	def update_grid(self, grid, housecords, thing):

		# if a house is placed, set h on coordinates of the house
		if thing == "single":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if grid[j][i] == "0":
						grid[j][i] = "h"
					else:
						exit(0)

		elif thing == "maison":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if grid[j][i] == "0":
						grid[j][i] = "h"
					else:
						exit(0)

		elif thing == "bungalow":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if grid[j][i] == "0":
						grid[j][i] = "h"
					else:
						exit(0)

		# if water is places set w on spot
		elif thing == "water":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if grid[j][i] == "0":
						grid[j][i] = "w"
					else:
						exit(0)

		# if space next to house, set s if it's empty
		# if there is water in place this counts as space
		elif thing == "space":
			for i in range(housecords[0], (housecords[2])):
				for j in range(housecords[3], (housecords[1])):
					if grid[j][i] == "0":
						grid[j][i] = "s"
					elif grid[j][i] == "w" or grid[j][i] == "s":
						pass

		return grid

	# check if around house enough space for free space
	def spacecheck(self, grid, housecords):
		for i in range(housecords[0], (housecords[2])):
			for j in range(housecords[3], (housecords[1])):
				if (grid[j][i] == "0" or grid[j][i] == "s"
					or grid[j][i] == "w"):
					pass
				else:
					return False
		return True

	# check if there is enough space to buid a house
	def housecheck(self, grid, housecords):
		for i in range(housecords[0], (housecords[2])):
			for j in range(housecords[3], (housecords[1])):
				if grid[j][i] == "0":
					pass
				else:
					return False
		return True

	# check if there is enough space for water (same as for house dus eventueel combineren)
	def watercheck(self, grid, water_coordinates):
		for i in range(water_coordinates[0], water_coordinates[2]):
			for j in range(water_coordinates[3], water_coordinates[1]):
				if grid[j][i] == "0":
					pass
				else:
					return False
		return True

	def fillgrid(self, grid):
		for i in range(360):
			for j in range(320):
				if grid[j][i] == "0":
					grid[j][i] = "s"

	def calculate_space(self, house_coordinates, grid):
		for index in range(1, 100):
			for i in range((house_coordinates[0] - index), (house_coordinates[2] + index)):
				if house_coordinates[0] - index >= 0 and house_coordinates[2] + index < 360:
					if house_coordinates[1] + index < 320 and house_coordinates[3] - index >= 0:
						if grid[house_coordinates[1] + index][i] != "h":
							pass
						if grid[house_coordinates[3] - index][i] != "h":
							pass
						else:
							return (index - 1)
					else:
						return (index - 1)
				else:
					return (index - 1)

	def makegrid(self, coordinatelist, water, total_value):

		# make the figure
		fig = plt.figure()

		# make plot
		ax = fig.add_subplot(1, 1, 1)

		# make axes grid
		major_ticks = np.arange(0, 320, 40)
		minor_ticks = np.arange(0, 400, 1)

		# makes lines for grid
		# ax.set_xticks(major_ticks)
		# ax.set_xticks(minor_ticks, minor=True)
		# ax.set_yticks(major_ticks)
		# ax.set_yticks(minor_ticks, minor=True)
		# ax.grid(which='both')

		# set limits for the plot
		ax.set_xlim(left=0, right=self.width, auto=False)
		ax.set_ylim(bottom=0, top=self.height, auto=False)

		# make background grid green
		x = [self.width, self.width, 0, 0]
		y = [0, self.height, self.height, 0]
		ax.fill(x, y, color ="#abd9e9")


		# iterate over coordinate list and select coordinates
		# for i in range(360):
		# 	for j in range(320):
		# 		if grid[j][i] == 'h':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color = "#ffffbf")
		# 		elif grid[j][i] == 's':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color = "#2c7bb6")
		# 		elif grid[j][i] == 'w':
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color ="#abd9e9")
		# 		else:
		# 			x = [(i+1), (i+1), i, i]
		# 			y = [j, (j+1), (j+1), j]
		# 			ax.fill(x, y, color ="#fdae61")

		if len(water) > 1:
			for body in range(len(water)):
				element = (water[body])
				x = [element[2], element[2], element[0], element[0]]
				y = [element[1], element[3], element[3], element[1]]
				ax.fill(x, y, color = "#2c7bb6")

		elif len(water) == 1:
			element = (water[0])
			x = [element[2], element[2], element[0], element[0]]
			y = [element[1], element[3], element[3], element[1]]
			ax.fill(x, y, color = "#2c7bb6")

		for element in coordinatelist:
			x = [element[2], element[2], element[0], element[0]]
			y = [element[1], element[3], element[3], element[1]]

			# color coordinates coresponding color
			if element[4] == 1:
				ax.fill(x, y, color = "#ffffbf")
			elif element[4] == 2:
				# total_value += bungalow(element).giveworth()
				ax.fill(x, y, color = "#fdae61")
			elif element[4] == 3:
				# total_value += maison(element).giveworth()
				ax.fill(x, y, color = "#d7191c")



		plt.xlabel('width')
		plt.ylabel('height')
		plt.title('Amstelhaege, worth: ${:,.2f}' .format(total_value))

		# bij deze beide manieren gaat de grid een beetje uit proporsie
		#plt.subplots_adjust(right = 0.75)
		plt.tight_layout(rect=[0,0,0.75,1])

		legend_single = mpatches.Patch(color = "#ffffbf", label = "single")
		legend_bungalow = mpatches.Patch(color = "#fdae61", label = "bungalow")
		legend_maison = mpatches.Patch(color = "#d7191c", label = "maison")
		legend_water = mpatches.Patch(color = "#2c7bb6", label = "water")
		plt.legend(handles=[legend_single, legend_bungalow, legend_maison, legend_water], bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0.)

		plt.show()
