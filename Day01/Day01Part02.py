depths = []
threeSums = []

with open('Day01/Day01.txt') as file:
    for line in file:
        depths.append(int(line))



for i in range(len(depths)):
    if (i == 0 or i == 1):
        continue
    threeSums.append(depths[i] + depths[i - 1] + depths[i - 2])

print(threeSums)
print('\n')

counter = 0

for i in range(len(threeSums)):
    if (i == 0):
        continue
    print(threeSums[i], end='')
    if (threeSums[i] > threeSums[i - 1]):
        print(' - INCREASED')
        counter += 1
    else:
        print(' - decreased')

print('\n')
print('Number of increments: ', counter)