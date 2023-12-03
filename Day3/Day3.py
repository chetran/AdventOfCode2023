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