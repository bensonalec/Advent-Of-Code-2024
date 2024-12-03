import re


def partOne():
    regex = r"mul\((\d+),(\d+)\)"
    with open("sample.out", "r") as fi:
        test_str = fi.read().replace("\n", "")
        matches = re.finditer(regex, test_str, re.MULTILINE)
        theSum = 0
        for _, match in enumerate(matches, start=1):
            val = int(match.group(1)) * int(match.group(2))
            theSum += val
        print(theSum)

def partTwo():
    regex = r"mul\((\d+),(\d+)\)|don't|do"
    with open("sample.out", "r") as fi:
        test_str = fi.read().replace("\n", "")
        matches = re.finditer(regex, test_str, re.MULTILINE)
        theSum = 0
        count = True
        for _, match in enumerate(matches, start=1):
            if((match.group() != "do" and match.group() != "don't")):
                if(count):
                    val = int(match.group(1)) * int(match.group(2))
                    theSum += val
            else:
                count = not count            
        print(theSum)
