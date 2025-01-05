def checkIfCellInNewGenerationIsAlive(lifeBoard, y, x, rangeY, rangeX):
    isAlive = lifeBoard[y][x] == 'X'
    aliveCount = 0
    for Y in range(y-1,y+2):
        for X in range(x-1, x+2):
            if (Y, X) != (y, x):
                if Y > rangeY:
                    Y = Y - (rangeY + 1)
                if X > rangeX:
                    X = X - (rangeX + 1)
                if (Y, X) != (y,x):
                    if lifeBoard[Y][X] == 'X':
                        aliveCount += 1

    # print(isAlive, aliveCount)
    if isAlive:
        return (aliveCount == 2 or aliveCount == 3)
    else:
        return aliveCount == 3



with open('gra.txt','r+') as file:
    lifeBoard = [line.replace('\n','') for line in file.readlines()]
    lifeBoards = [[],[]]
    activeCOORDS = []
    rangeY = lifeBoard.__len__() - 1
    rangeX = lifeBoard[0].__len__() - 1

    for i in range(2,100):
        activeCOORDS.clear()
        for idxY, line in enumerate(lifeBoard):
            for idxX, oneChar in enumerate(line):
                if checkIfCellInNewGenerationIsAlive(lifeBoard, idxY, idxX, rangeY, rangeX):
                    activeCOORDS.append((idxY, idxX))
        lifeBoard = [line.replace('X','.') for line in lifeBoard]
        lifeBoard = [list(line) for line in lifeBoard]
        for y,x in activeCOORDS:
            lifeBoard[y][x] = 'X'
        lifeBoard = ["".join(line) for line in lifeBoard]
        lifeBoards.append(lifeBoard)
        print(i)
        print('\n'.join(lifeBoard))
    print()
    print("\n".join(lifeBoards[37]))
    # print(activeCOORDS)
    # print(checkIfCellInNewGenerationIsAlive(lifeBoard,2, 3, rangeY, rangeX))