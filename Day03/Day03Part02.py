def isInteger(value):
	"""Returns true if entered value is integer, otherwise false."""
	try:
		int(value)
		return True
	except ValueError:
		return False

numberOfLines = 0
numberOfBits = 0
counters = []
allNumbers = []

with open('Day03/Day03Input.txt') as file:
    for line in file:
        numberOfLines += 1
        tempList = list(line)

        if not (isInteger(tempList[-1])):
            tempList.pop()

        numberOfBits = len(tempList)
        allNumbers.append(tempList)

for i in range(numberOfBits):
    counters.append(0)

for number in allNumbers:
    for i in range(len(number)):
        counters[i] += int(number[i])

print('Numbers: ', allNumbers)
print()
        
print('Bit counters: ', counters)
print()

allOxygenNumbers = allNumbers
chosenOxygenNumbers = []
finalOxygenNumber = []

bitCounterOxygen = counters[0]

print('STARTING WITH OXYGEN NUMBERS')
print()

for i in range(len(counters)):

    print('Iteration: ', i + 1)
    print('Number of Oxygen numbers: ', len(allOxygenNumbers))
    print('Bit counter Oxygen: ', bitCounterOxygen)

    if (bitCounterOxygen >= (len(allOxygenNumbers) / 2)):
        for number in allOxygenNumbers:
            if (number[i] == '1'):
                chosenOxygenNumbers.append(number)

    elif (bitCounterOxygen < (len(allOxygenNumbers) / 2)):
        for number in allOxygenNumbers:
            if (number[i] == '0'):
                chosenOxygenNumbers.append(number)

    else:
        print('ERROR')   

    print('Chosen Oxygen numbers: ', chosenOxygenNumbers)

    allOxygenNumbers = chosenOxygenNumbers

    if (len(chosenOxygenNumbers) == 1):
        finalOxygenNumber = chosenOxygenNumbers
        print('Only one Oxygen number remains, breaking.')
        print()
        break
        
    bitCounterOxygen = 0

    if (len(number) > i + 1):
        for number in allOxygenNumbers:
            bitCounterOxygen += int(number[i + 1])

        print('New bit counter Oxygen: ', bitCounterOxygen)
    else:
        print('No other bit to check')

    print()
    
    chosenOxygenNumbers = []

allScrubberNumbers = allNumbers
chosenScrubberNumbers = []
finalScrubberNumber = []

bitCounterScrubber = counters[0]

print('STARTING WITH SCRUBBER NUMBERS')
print()

for i in range(len(counters)):

    print('Iteration: ', i + 1)
    print('Number of Scrubber numbers: ', len(allScrubberNumbers))
    print('Bit counter Scrubber: ', bitCounterScrubber)

    if (bitCounterScrubber >= (len(allScrubberNumbers) / 2)):
        for number in allScrubberNumbers:
            if (number[i] == '0'):
                chosenScrubberNumbers.append(number)

    elif (bitCounterScrubber < (len(allScrubberNumbers) / 2)):
        for number in allScrubberNumbers:
            if (number[i] == '1'):
                chosenScrubberNumbers.append(number)

    else:
        print('ERROR')   

    print('Chosen Scrubber numbers: ', chosenScrubberNumbers)

    allScrubberNumbers = chosenScrubberNumbers

    if (len(chosenScrubberNumbers) == 1):
        finalScrubberNumber = chosenScrubberNumbers
        print('Only one Scrubber number remains, breaking.')
        print()
        break
        
    bitCounterScrubber = 0

    if (len(number) > i + 1):
        for number in allScrubberNumbers:
            bitCounterScrubber += int(number[i + 1])

        print('New bit counter Scrubber: ', bitCounterScrubber)
    else:
        print('No other bit to check')

    print()   
    chosenScrubberNumbers = []

print('Final Oxygen number list: ', finalOxygenNumber)
print('Final Scrubber number list: ', finalScrubberNumber)
print()

oxygenNumberBinary = ''.join(finalOxygenNumber[0])
scrubberNumberBinary = ''.join(finalScrubberNumber[0])

print('Oxygen Number Binary: ', oxygenNumberBinary)
print('Scrubber Number Binary: ', scrubberNumberBinary)
print()

oxygenNumberDecimal = int(oxygenNumberBinary, 2)
scrubberNumberDecimal = int(scrubberNumberBinary, 2)

print('Oxygen Number Decimal: ', oxygenNumberDecimal)
print('Scrubber Number Decimal: ', scrubberNumberDecimal)
print()

print('FINAL RESULT: ', oxygenNumberDecimal * scrubberNumberDecimal)
print()