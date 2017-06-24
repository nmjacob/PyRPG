#Used for rendering the screen


#Constants

#The number of newlines used to clear the screen
#Set higher if the terminal is not clearing completely between renders
_NEWLINE_COUNT = 50


#Private Functions

#Clears the screen by newlining to the bottom of the screen
#Change the constant to add more newlines if the terminal is not clearing
def _ClearScreen():
	print("\n" * _NEWLINE_COUNT)


#Public Functions

#Renders everything on the screen
#INPUT:
#	Matrix to render. Created from the Vision module, which returns how much the user should see of the map
#PROCESS
#	Clears the screen uses the _ClearScreen function
#	Renders the matrix
#	TODO: Displays the commands the user can use
def Render(matrix):

	#Clear the screen
	_ClearScreen()

	#Render the matrix
	for x in range(0, len(matrix)):
		print("".join(matrix[x]))

