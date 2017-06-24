#This file defines the creature class

class Creature():
	def __init__(self, x, y, name, icon, isPlayer):
		self.x = x
		self.y = y
		self.name = name
		self.icon = icon
		self.isPlayer = isPlayer
	
	def GetPosition(self):
		return [self.x, self.y]

	def GetName(self):
		return self.name

	def GetIcon(self):
		return self.icon

	def IsPlayer(self):
		return self.isPlayer

	def GetName(self):
		return self.name
