def isInteger(value):
	"""Returns true if entered value is integer, otherwise false."""
	try:
		int(value)
		return True
	except ValueError:
		return False