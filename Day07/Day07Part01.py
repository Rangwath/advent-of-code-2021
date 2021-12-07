numbersList = []

with open('Day07/Day07Input.txt') as file:
    for line in file:
        tempNumbers = line.split(',')
        for number in line.split(','):
            numbersList.append(int(number))

print(numbersList)
print('Max:', max(numbersList))
print('Min:', min(numbersList))

fuelCostsList = []

for i in range(min(numbersList), max(numbersList) + 1):
    print('Iteration:', i)
    fuelCost = 0
    for number in numbersList:
        #print('Fuel cost for', number, 'is', abs(i - number))
        fuelCost += abs(i - number)

    fuelCostsList.append(fuelCost)

print('FINAL RESULT:', min(fuelCostsList))

