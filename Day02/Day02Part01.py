horizontalPos = 0
depth = 0

with open('Day02/Day02Input.txt') as file:
    for line in file:
        splitLine = line.split()
        print(splitLine)

        if (splitLine[0] == 'forward'):
          horizontalPos = horizontalPos + int(splitLine[1])
          print("Horizontal Position: ", horizontalPos)

        elif (splitLine[0] == 'down'):
          depth = depth + int(splitLine[1])
          print("Depth: ", depth)

        elif (splitLine[0] == 'up'):
          depth = depth - int(splitLine[1])
          print("Depth: ", depth)

        else:
          print("ERROR")

print()
print("FINAL Horizontal Position: ", horizontalPos)
print("FINAL Depth: ", depth)
print("FINAL RESULT: ", horizontalPos * depth)
print()