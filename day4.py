def subfinder(mylist, pattern):
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            matches.append(pattern)
    return matches   

def getDiagonals(grid):
    #build diagonal
    finalDiag = []
    for x in range(len(grid)):
        y = 0
        currentDiag = []
        while x >= 0 and y <= len(grid[x]):
            currentDiag.append(grid[y][x])
            x -= 1
            y += 1
        finalDiag.append(currentDiag)
    for y in range(len(grid)-1)[::-1]:
        x = 0
        currentDiag = []
        while (x <= len(grid[x])-1 and y >= 0):
            currentDiag.append(grid[::-1][y][::-1][x])
            x += 1
            y -= 1
        finalDiag.append(currentDiag)
    return finalDiag

def getVertical(grid):
    length = len(grid[0])
    vertical = []
    for col in range(length):
        curRow = []
        for row in grid:
            curRow.append(row[col])
        vertical.append(curRow)
    return vertical

def partOne():
    with open("sample.out", "r") as fi:
        grid = fi.readlines()
        grid = [x.replace("\n", "") for x in grid]
        grid = [list(x) for x in grid]
        revGrid = grid[::-1]
        xmasCount = 0
        #all forward
        for row in grid:
            xmasCount += len(subfinder(row, ["X","M","A","S"]))
        #all backward
        for row in grid:
            xmasCount += len(subfinder(row[::-1], ["X","M","A","S"]))
        #build vertical
        vertical = getVertical(grid)
        #check vertical
        for row in vertical:
            xmasCount += len(subfinder(row, ["X","M","A","S"]))
        #backwards vertical
        for row in vertical:
            xmasCount += len(subfinder(row[::-1], ["X","M","A","S"]))
        #build diagonal
        finalDiag = getDiagonals(grid)
        #forward pass diag one
        for row in finalDiag:
            xmasCount += len(subfinder(row, ["X","M","A","S"]))
        #backwards pass diag one
        for row in finalDiag[::-1]:
            xmasCount += len(subfinder(row[::-1], ["X","M","A","S"]))
        # #reverse diag
        finalDiag = getDiagonals(revGrid)
        #forward pass diag two
        for row in finalDiag:
            xmasCount += len(subfinder(row, ["X","M","A","S"]))
        #backward pass diag two
        for row in finalDiag[::-1]:
            xmasCount += len(subfinder(row[::-1], ["X","M","A","S"]))

        print(xmasCount)

def partTwo():
    with open("sample.out", "r") as fi:
        grid = fi.readlines()
        grid = [x.replace("\n", "") for x in grid]
        grid = [list(x) for x in grid]
        xmasCount = 0
        for x in range(1, len(grid)-1):
            for y in range(1, len(grid[x])-1):
                if(grid[x][y] == "A"):
                    testOne = [grid[x-1][y-1], grid[x][y], grid[x+1][y+1]]
                    testTwo = [grid[x-1][y+1], grid[x][y], grid[x+1][y-1]]
                    if(testOne == ["M","A","S"] or testOne[::-1] == ["M","A","S"]):
                        if(testTwo == ["M","A","S"] or testTwo[::-1] == ["M","A","S"]):
                            xmasCount += 1
                
        print(xmasCount)
