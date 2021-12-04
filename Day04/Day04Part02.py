import Helper

class BingoNumber:
    def __init__(self, number, board, coordX, coordY, drawn):
        self.number = number
        self.board = board
        self.coordX = coordX
        self.coordY = coordY
        self.drawn = drawn
    
    def __str__(self):
        return '(no:{},brd:{},x:{},y:{},{})'.format(self.number, self.board, self.coordX, self.coordY, self.drawn)

    def __repr__(self):
        return '(no:{},brd:{},x:{},y:{},{})'.format(self.number, self.board, self.coordX, self.coordY, self.drawn)

boards = []
drawnNumbers = []
allBingoNumbers = []
lineNumber = 0
boardNumber = 1
counter = 0
xCounter = 1

with open('Day04/Day04.txt') as file:
    for line in file:

        if (line == '\n'):            
            # Skipping empty line
            continue

        if (lineNumber == 0):
            tempLine = line.rstrip()
            tempNumbers = tempLine.split(',')
            for number in tempNumbers:
                drawnNumbers.append(int(number))
        else:
            tempList = line.split()
            if not (Helper.isInteger(tempList[-1])):
                tempList.pop()
            
            tempBingoList = []

            for i in range(len(tempList)):
                    bingoNumber = BingoNumber(int(tempList[i]), boardNumber, xCounter, i + 1, False)
                    tempBingoList.append(bingoNumber)
                    allBingoNumbers.append(bingoNumber)
                    counter += 1
                    if (counter >= 25):
                        counter = 0
                        xCounter = 0
                        boardNumber += 1
                            
            print(tempBingoList)
            boards.append(tempBingoList) 
            xCounter += 1

        lineNumber += 1

print()
print('Drawn numbers:', drawnNumbers)
print()

numberOfBoards = boardNumber - 1
drawnBingoNumbers = []
winningBoardNumber = 0
lastWinningBoardNumber = 0
lastNumber = 0
won = False

notWinningBoards = []

for i in range (1, numberOfBoards + 1):
    notWinningBoards.append(i)

for i in range (0, len(drawnNumbers)):
    if won:
        break

    print(i + 1 , '. draw is number ', drawnNumbers[i], sep='')
    for bingoNumber in allBingoNumbers:
        if (bingoNumber.number == drawnNumbers[i]):
            bingoNumber.drawn = True
            drawnBingoNumbers.append(bingoNumber)

    #print(drawnBingoNumbers)
    print()

    bingoCounterX = 0
    bingoCounterY = 0

    for j in range(1, numberOfBoards + 1):
        if won:
            break

        print('CHECKING BOARD:', j)
        print()
        for k in range(1, 6):
            if won:
                break

            #print('Checking coord:', k)
            for bingoNumber in drawnBingoNumbers:

                if (bingoNumber.board == j):

                    if (bingoNumber.coordX == k):
                        bingoCounterX += 1
                        #print('Bingo Counter X:', bingoCounterX)
                        if (bingoCounterX >= 5):
                            print('WINNING BOARD NUMBER:', j)
                            print()
                            winningBoardNumber = j
                            lastNumber = drawnNumbers[i]
                            if (winningBoardNumber in notWinningBoards):
                                if (len(notWinningBoards) == 1):
                                    lastWinningBoardNumber = notWinningBoards[0]
                                notWinningBoards.remove(winningBoardNumber)
                            if (len(notWinningBoards) == 0):
                                won = True
                                break

                    if (bingoNumber.coordY == k):
                        bingoCounterY += 1
                        #print('Bingo Counter Y:', bingoCounterY)
                        if (bingoCounterY >= 5):
                            print('WINNING BOARD NUMBER:', j)
                            print()
                            winningBoardNumber = j
                            lastNumber = drawnNumbers[i]
                            if (winningBoardNumber in notWinningBoards):
                                if (len(notWinningBoards) == 1):
                                    lastWinningBoardNumber = notWinningBoards[0]
                                notWinningBoards.remove(winningBoardNumber)
                            if (len(notWinningBoards) == 0):
                                won = True
                                break
            
            #print()
            bingoCounterX = 0
            bingoCounterY = 0

    #print()

notDrawnCounter = 0

for bingoNumber in allBingoNumbers:
    if (bingoNumber.board == lastWinningBoardNumber and bingoNumber.drawn == False):
        notDrawnCounter += bingoNumber.number

print('Last Winning Board Number:', lastWinningBoardNumber)
print('Last Drawn Number:', lastNumber)
print('Sum of not drawn numbers:', notDrawnCounter)
print()
print('FINAL RESULT:', notDrawnCounter * lastNumber)
print()