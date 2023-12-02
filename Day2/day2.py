import re

sum = 0
with open('input.txt', 'r') as input:
    for row in input:
        cubes = {
            'red' : 12,
            'green' : 13, 
            'blue' : 14
        }
        validGame = True
        game = re.split(':', row)
        turn = re.split('\s', game[1].strip()) # cubes from each game
        for eachGrab in range(0, len(turn), 2):
            revealedCubes = int(turn[eachGrab])
            cubeColor = turn[eachGrab + 1]
            cubesLeft = cubes.get(cubeColor.replace(',', "").replace(';', "")) - revealedCubes
            if cubesLeft < 0:
                validGame = False
                break
            else: 
                cubes[cubeColor] = cubesLeft
        if (validGame):
            sum += int(game[0].split()[1])

print(sum)

sum = 0
with open('input.txt', 'r') as input:
    for row in input:
        cubes = {
            'red' : 0,
            'green' : 0, 
            'blue' : 0
        }
        validGame = True
        game = re.split(':', row)
        turn = re.split('\s', game[1].strip()) # cubes from each game
        for eachGrab in range(0, len(turn), 2):
            revealedCubes = int(turn[eachGrab])
            cubeColor = turn[eachGrab + 1].replace(',', "").replace(';', "")
            if cubes.get(cubeColor) < revealedCubes:
                cubes[cubeColor] = revealedCubes
        power = 1
        for color in cubes:
            power *= cubes.get(color)
        sum += power
print(sum)