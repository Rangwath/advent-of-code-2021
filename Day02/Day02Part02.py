horizontalPos = 0
depth = 0
aim = 0

with open('Day02/Day02Input.txt') as file:
    for line in file:
        splitLine = line.split()
        print(splitLine)

        if (splitLine[0] == 'forward'):
          horizontalPos = horizontalPos + int(splitLine[1])
          print("Horizontal Position: ", horizontalPos)
          if (aim != 0):
            depth = depth + (aim * int(splitLine[1]))
            print("Depth: ", depth)

        elif (splitLine[0] == 'down'):
          aim = aim + int(splitLine[1])
          print("Aim: ", aim)

        elif (splitLine[0] == 'up'):
          aim = aim - int(splitLine[1])
          print("Aim: ", aim)

        else:
          print("ERROR")

print()
print("FINAL Horizontal Position: ", horizontalPos)
print("FINAL Depth: ", depth)
print("FINAL RESULT: ", horizontalPos * depth)
print()