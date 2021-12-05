def isInteger(value):
	"""Returns true if entered value is integer, otherwise false."""
	try:
		int(value)
		return True
	except ValueError:
		return False

numberOfLines = 0
numberOfBits = 0
numbers = []
counters = []

with open('Day03/Day03Input.txt') as file:
    for line in file:
        numberOfLines += 1
        tempList = list(line)

        if not (isInteger(tempList[-1])):
            tempList.pop()

        numberOfBits = len(tempList)
        numbers.append(tempList)

for i in range(numberOfBits):
    counters.append(0)

for number in numbers:
    for i in range(len(number)):
        counters[i] += int(number[i])
        
print('Bit counters: ', counters)
print()

gammaRateList = []
epsilonRateList = []

for bitCount in counters:
    if (bitCount > (numberOfLines / 2)):
        gammaRateList.append('1')
        epsilonRateList.append('0')
    elif (bitCount < (numberOfLines / 2)):
        gammaRateList.append('0')
        epsilonRateList.append('1')
    else:
        print('ERROR')

gammaRateBinary = ''.join(gammaRateList)
epsilonRateBinary = ''.join(epsilonRateList)

print('Gamma Rate Binary: ', gammaRateBinary)
print('Epsilon Rate Binary: ', epsilonRateBinary)
print()

gammaRateDecimal = int(gammaRateBinary, 2)
epsilonRateDecimal = int(epsilonRateBinary, 2)

print('Gamma Rate Decimal: ', gammaRateDecimal)
print('Epsilon Rate Decimal: ', epsilonRateDecimal)
print()

print('FINAL RESULT: ', gammaRateDecimal * epsilonRateDecimal)
print()