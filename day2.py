import copy
def partOne():
    with open("sample.out", "r") as fi:
        content = fi.readlines()
        content = [[int(y) for y in x.split(" ")] for x in content]
        theSum = 0
        for i in content:
            if(checkSafety(i)):
                theSum += 1
        print(theSum)


def partTwo():
    with open("sample.out", "r") as fi:
        content = fi.readlines()
        content = [[int(y) for y in x.split(" ")] for x in content]
        theSum = 0
        for i in content:
            if(checkSafety(i)):
                theSum += 1
            else:
                for z in range(len(i)):
                    temp = copy.deepcopy(i)
                    if(len(temp) % 2 == 0):
                        temp.pop(z-1)
                    else:
                        temp.pop(z)
                    if(checkSafety(temp)):
                        theSum += 1
                        break
        print(theSum)

def checkSafety(i):
    newList = []
    for x in range(len(i)):
        if(x != len(i)-1):
            newList.append(i[x] - i[x+1])
    allPos = sum([x > 0 for x in newList]) == len(newList)
    allNeg = sum([x < 0 for x in newList]) == len(newList)
    values = [abs(x) for x  in newList]
    allX = sum([(x > 0 and x <= 3) for x in values]) == len(values)
    if(allX and (allPos or allNeg)):
        return True
    return False

partOne()
partTwo()