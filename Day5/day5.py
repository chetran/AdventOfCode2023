import re

info = []
with open("input.txt", "r") as input:
    section = []
    for i in input:
        line = i.strip()
        if line:
            section.append(line)
        else:
            info.append(section)
            section = []
    info.append(section)         

def seedInHere(arr, value):
    for row in arr:
        map = re.findall('\d+', row)
        if value in range(int(map[1]), int(map[1]) + int(map[2])):
            index = value - int(map[1])
            return int(map[0]) + index
    return value

def getLocation(seedNumber):
    searchingValue = seedNumber
    for i in range(1,len(info)):
        searchingValue = seedInHere(info[i][1:], searchingValue)
    #print(f'seednumber {seedNumber}, location {searchingValue}')
    return searchingValue


initial = re.findall('\d+', info[0][0])
locations = []
# Part 1 
for seed in initial:
    locations.append(getLocation(int(seed)))
print(min(locations))


# Part 2
locations = []
ranges = re.findall('\d+',info[0][0].split(':')[1])
for i in range(0, len(ranges), 2):
    #print(ranges[i], ranges[i+1])
    for j in range(int(ranges[i]), int(ranges[i]) + int(ranges[i+1])):
        locations.append(getLocation(j))
print(min(locations))




