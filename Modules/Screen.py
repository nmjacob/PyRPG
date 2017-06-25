#Used for rendering the screen

import copy


#Constants

#The number of newlines used to clear the screen
#Set higher if the terminal is not clearing completely between renders
_NEWLINE_COUNT = 50


#Private Functions

#Clears the screen by newlining to the bottom of the screen
#Change the constant to add more newlines if the terminal is not clearing
def _ClearScreen():
	print("\n" * _NEWLINE_COUNT)

#Function to include the commands for the user to submit
#Currently supported commands:
#	a (Direction)
#		Attacks in the direction specified. Uses the same format for direction as moving
#	(Direction) Moves the character in that direction
		#Supported directions are n(up), w(left), e(right), s(down)
def _Commands():
	print("\n\nCommands:\na: Attack. Follow with a direction")
	print("(Direction): moves the user in that direction")
	print("Directions: n(up), w(left), e(right), s(down)")
	print("q: quits the application")

def _ApplyCreatures(matrixIn, creatures):
	matrix = copy.deepcopy(matrixIn)

	for x in range(0, len(creatures)):
		loc = creatures[x].GetPosition()
		icon = creatures[x].GetIcon()

		matrix[loc[1]][loc[0]] = icon

	return matrix


#Public Functions

#Renders everything on the screen
#INPUT:
#	Matrix to render. Created from the Vision module, which returns how much the user should see of the map
#PROCESSdeepcopy
#	Clears the screen uses the _ClearScreen function
#	Renders the matrix
#	Displays available commands
def Render(matrix, creatures):

	matrix = _ApplyCreatures(matrix, creatures)

	#Clear the screen
	_ClearScreen()

	#Render the matrix
	for x in range(0, len(matrix)):
		print("".join(matrix[x]))

	#Display commands
	_Commands()
