#Used to read the files

def GetLevel():

	matrix = []
	i = 0

	with open("sample.dat") as f:
		matrix.append(list(f))
		i += 1

	return matrix
