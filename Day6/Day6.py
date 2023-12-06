import re 

lines = []
with open("input.txt", "r") as f:
    for line in f:
        lines.append(re.findall("\d+", line))

def waysOfWinning(time, distance):
    count = 0
    for btnHold in range(time + 1):
        timeLeft = time - btnHold
        if timeLeft * btnHold > distance:
            count += 1
    return count


sum = 1
time = ""
distance = ""
for race in range(len(lines[0])):
    time += lines[0][race]
    distance += lines[1][race]
    sum *= waysOfWinning(int(lines[0][race]), int(lines[1][race]))
# Part 1
print(sum)
# Part 2
print('Total', waysOfWinning(int(time), int(distance)))