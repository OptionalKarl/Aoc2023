from common import import_csv

file_path = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day3.txt'

uniqueCoOrds = []
visitedCoOrds = []

def getmovement(input):
    xy = [0,0]
    if input == ">": xy = [1,0]
    elif input == "<": xy = [-1,0] 
    elif input == "^": xy = [0,1] 
    elif input == "v": xy = [0,-1] 
    return xy

def updatecords(currentLoc):
    
    visitedCoOrds.append([currentLoc[0],currentLoc[1]])
    if not currentLoc in uniqueCoOrds: uniqueCoOrds.append([currentLoc[0],currentLoc[1]])

data = import_csv(file_path)
directions = data[0]

santaloc = [0,0]
roboloc = [0,0]
issanta = True
for d in directions:
    movement = getmovement(d)
    if issanta:
        santaloc[0] += movement[0]
        santaloc[1] += movement[1]
        updatecords(santaloc)

    else:
        roboloc[0] += movement[0]
        roboloc[1] += movement[1]
        updatecords(roboloc)
    issanta = not issanta


print(len(uniqueCoOrds))





