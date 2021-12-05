depths = []

with open('Day01/Day01Input.txt') as file:
    for line in file:
        depths.append(int(line))

counter = 0

for i in range(len(depths)):
    if (i == 0):
        continue
    print(depths[i], end='')
    if (depths[i] > depths[i - 1]):
        print(' - INCREASED')
        counter += 1
    else:
        print(' - decreased')

print()
print('Number of increments: ', counter)
print()