from collections import defaultdict


input = []

with open('Day06/Day06Input.txt') as file:
    for line in file:
        for number in line.split(','):
            input.append(int(number))


timersAfter = {}
timers = {}
for i in input:
    if i not in timers:
        timers[i] = 0
    timers[i] += 1

print('Timers at the beginning:', timers)

for i in range(256):
    print('Day:', i + 1)
    timersAfter = defaultdict(int)
    for key, counter in timers.items():
        if (key == 0):
            timersAfter[6] += counter
            timersAfter[8] += counter
        else:
            timersAfter[key - 1] += counter

    timers = timersAfter

counter = 0
for value in timers.values():
    counter += value

print('FINAL RESULT:', counter)
