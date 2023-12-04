

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# It should be a symbol if its not a digit or a period
def isSymbol(arr, i, j):
    if (i >= 0 and i < len(arr) and j >= 0 and j < len(arr[i])):
        return arr[i][j] != '.' and not arr[i][j].isdigit()
    return False

# Checks the surroundings of character for a symbol
def hasAdjacentSymbol(arr, row, col):
    for i in range(-1,2):
        for j in range(-1,2):
            if isSymbol(arr, row+i, col+j) and arr[row][col].isdigit():
                return True
    return False

# Solution 1
sum = 0
numbers = []
for i in range(len(lines)):
    number = ""
    numberHasSymbol = False
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            number += lines[i][j]
        if not lines[i][j].isdigit() or j == len(lines[i])-1:
            if numberHasSymbol:
                sum += int(number)
            number = ""
            numberHasSymbol = False
        if hasAdjacentSymbol(lines, i, j):
            numberHasSymbol = True

print(sum)

class gearNum:
    def __init__(self, number, span, row) -> None:
        self.number = number 
        self.span = span 
        self.row = row 
    
    def __repr__(self) -> str:
        return f'{self.number}, {self.span[0]}, {self.span[1]}, {self.row}'
    
    def equal(self, object):
        return self.number == object.number and self.span == object.span and self.row == object.row

def getNumber(arr, row, col):
    length = len(arr[row])
    goLeft = col - 1
    goRight = col + 1
    left = ""
    right = ""
    while(goLeft >=  0 and goLeft < length and arr[row][goLeft].isdigit()):
        left = arr[row][goLeft] + left
        goLeft -= 1
    while(goRight >=  0 and goRight < length and arr[row][goRight].isdigit()):
        right += arr[row][goRight]
        goRight += 1
    return gearNum(int(left + arr[row][col] + right), (goLeft+1, goRight+1), row)
        

def getGearRatio(arr, row, col):
    gearRatio = 1
    gearNums = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (arr[row+i][col+j].isdigit()):
                adding = True
                number = getNumber(arr, row+i, col+j)
                for gN in gearNums:
                    if gN.equal(number):
                        adding = False
                if adding:
                    gearNums.append(number)
                    gearRatio *= number.number
    return gearRatio if len(gearNums) == 2 else 0

sum = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '*':
            sum += getGearRatio(lines, i, j)

print(sum)