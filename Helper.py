def isInteger(value):
	"""Returns true if entered value is integer, otherwise false."""
	try:
		int(value)
		return True
	except ValueError:
		return False

def indexExistsInList(list, index):
	"""Returns true if entered index is in the entered list, otherwise false."""
	try:
		list[index]
		return True
	except IndexError:
		return False