class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return '({},{}->{},{})'.format(self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        return '({},{}->{},{})'.format(self.x1, self.y1, self.x2, self.y2)

print()

segmentsList = []

with open('Day05/Day05Input.txt') as file:
    for line in file:
        tempLine = line.strip().split() 
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0

        for i in range(len(tempLine)):            
            
            if (i == 0):
                tempCoord = tempLine[i].split(',')
                x1 = int(tempCoord[0])
                y1 = int(tempCoord[1])

            if (i == 2):
                tempCoord = tempLine[i].split(',')
                x2 = int(tempCoord[0])
                y2 = int(tempCoord[1])
        
        if (x1 == x2 or y1 == y2):
            segmentsList.append(Segment(x1, y1, x2, y2))
             
print('Only horizontal and vertical segments:')
for segment in segmentsList:
    print(segment)
print()

dangerousVents = {}

for i in range(len(segmentsList)):
    print(i + 1, '. iteration over list of segments', sep='')
    print()
    segment = segmentsList[i]
    
    if (segment.x1 == segment.x2):
        fromY = 0
        toY = 0
        if (segment.y1 < segment.y2):
            fromY = segment.y1
            toY = segment.y2
        else:
            fromY = segment.y2
            toY = segment.y1

        for j in range(fromY, toY + 1):
            if (segment.x1, j) not in dangerousVents:
                dangerousVents[segment.x1, j] = 0
            dangerousVents[segment.x1, j] += 1                          
    
    if (segment.y1 == segment.y2):
        fromX = 0
        toX = 0
        if (segment.x1 < segment.x2):
            fromX = segment.x1
            toX = segment.x2
        else:
            fromX = segment.x2
            toX = segment.x1

        for j in range(fromX, toX + 1):
            if (j, segment.y1) not in dangerousVents:
                dangerousVents[j, segment.y1] = 0
            dangerousVents[j, segment.y1] += 1
counter = 0
print('Dangerous vents:')
for k in dangerousVents:
    if (dangerousVents[k] > 1):
        print(k, dangerousVents[k])
        counter += 1    

print()
print('FINAL RESULT:', counter)
print()