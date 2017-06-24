#Used to read the files

from Modules import Creature


#Global Constants


#Public Functions
#Reads the sample file, and returns it as a matrix. Will eventually accept a specified file
#RETURNS
#	A matrix of the level from the sample file
def GetLevel():

	#Matrix to be returned
	matrix = []

	#Read the file and store it as a matrix
	with open("sample.dat") as f:
		array = list(f)

	#splitting it into a matrix
	for x in range(0, len(array)):
		matrix.append(list(array[x])[:-1])
	print(matrix)

	return matrix


def GetCreatures():

	x = 0

	creatures = []

	with open("sample_creatures.dat") as f:
		array = list(f)

	while x <= len(array):
		name = str(array[x])[:-1]
#		print(name)
		x += 1
		icon = str(array[x])[:-1]
#		print(icon)
		x += 1
		locX = int(str(array[x])[:-1])
#		print(locX)
		x += 1
		locY = int(str(array[x])[:-1])
#		print(locY)
		x += 1
		isPlayer = bool(str(array[x])[:-1])
#		print(isPlayer)
		x += 2

		creatures.append(Creature.Creature(locX, locY, name, icon, isPlayer))

	return creatures
