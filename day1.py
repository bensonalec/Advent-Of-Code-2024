
def partOne():
    with open("sample.out", "r") as fi:
        content = fi.readlines()
        content = [x.split("   ") for x in content]
        content = [[int(y) for y in x] for x  in content]
        listOne = sorted([x[0] for x in content])
        listTwo = sorted([x[1] for x in content])
        finalList = []
        for i in range(len(listOne)):
            finalList.append(abs(listOne[i] - listTwo[i]))
        print(sum(finalList))

def partTwo():
    with open("sample.out", "r") as fi:
        content = fi.readlines()
        content = [x.split("   ") for x in content]
        content = [[int(y) for y in x] for x  in content]
        listOne = [x[0] for x in content]
        listTwo = [x[1] for x in content]
        finalList = []
        for x in listOne:
            finalList.append(listTwo.count(x) * x)
        print(sum(finalList))
