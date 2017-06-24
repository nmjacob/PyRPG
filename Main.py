#Main file, used for command and control as well

import re

from Modules import Screen
from Modules import FileRead
from Modules import Creature

#Global Variables

#The current level, in it's current state
LEVEL = []
CREATURES = []

#Private Functions

def _FindPosition(icon):
	for y in range(0, len(LEVEL)):
		try:
			x = LEVEL[y].index('S')

		except:
			#Except requires an action, this is a garbage action to satisfy the interpreter
			x = 1;

		else:
			return [x,y]
			
	return False
			


#Public Functionions

def CommandAndControl():

	LEVEL = FileRead.GetLevel()

	CREATURES = FileRead.GetCreatures()

	Screen.Render(LEVEL, CREATURES)

	print(LEVEL)

	#print(_FindPosition('S'))

	#player = Creature.Creature(_FindPosition('S'))

	#print(player.GetPosition())

	print(LEVEL)

	#print(_FindPosition())

CommandAndControl()

#    attackPattern = re.compile("^[a]\s[nwes]$")
#    movePattern = re.compile("^[nwes]$")

#    command = input("Command: ")

#    if movePattern.match(command):
		
