#Main file, used for command and control as well

import re
import copy

from Modules import Screen
from Modules import FileRead
from Modules import Creature

#Global Variables

#The current level, in it's current state
LEVEL = []
CREATURES = []
PLAYER_ID = 0

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
		

def _FindPlayerId():
	for x in range(0, len(CREATURES)):
		if CREATURES[x].IsPlayer():
			global PLAYER_ID 
			PLAYER_ID = x
			break

	
def _Move(creature, direction):
	
	pos = creature.GetPosition()

	global LEVEL

	if 'n' == direction:
		if LEVEL[pos[1]-1][pos[0]] not in ['=', '|']:
			pos[1] -= 1

	elif 'e' == direction:
		if LEVEL[pos[1]][pos[0]+1] not in ['=', '|']:
			pos[0] += 1

	elif 'w' == direction:
		if LEVEL[pos[1]][pos[0]-1] not in ['=', '|']:
			pos[0] -= 1

	elif 's' == direction:
		if LEVEL[pos[1]+1][pos[0]] not in ['=', '|']:
			pos[1] += 1

	creature.SetPosition(pos[0], pos[1])

#Public Functionions

def CommandAndControl():

	attackPattern = re.compile("^[a]\s[nwes]$")
	movePattern = re.compile("^[nwes]$")

	global LEVEL

	LEVEL = FileRead.GetLevel()

	FileRead.GetCreatures(CREATURES)

	_FindPlayerId()

	while True:
		Screen.Render(LEVEL, CREATURES)

		playerCommand = input("Command: ")

		if movePattern.match(playerCommand):
			_Move(CREATURES[PLAYER_ID], playerCommand)

		if "q" == playerCommand:
			break

CommandAndControl()
