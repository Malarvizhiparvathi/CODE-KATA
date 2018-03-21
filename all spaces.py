def removeSpaces(string):

	count = 0

	list = []

	for i in xrange(len(string)):
		if string[i] != ' ':
			list.append(string[i])

	return toString(list)
def toString(List):
	return ''.join(List)

string =raw_input("")
print removeSpaces(string)


