timers = []

with open('Day06/Day06Input.txt') as file:
    for line in file:
        tempNumbers = line.split(',')
        for number in tempNumbers:
            timers.append(int(number))

timersAfter = []

print('Timers at the beginning:', timers)

for i in range(80):
    print('Day:', i + 1, 'Number of fish:', len(timers))
    for j in range(len(timers)):
        if (timers[j] == 0):
            timersAfter.append(6)
            timersAfter.append(8)
        else:
            timersAfter.append(timers[j] - 1)

    timers = timersAfter
    timersAfter = []

print('FINAL RESULT:', len(timers))