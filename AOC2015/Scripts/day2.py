from common import import_csv
file_path = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day2.txt'



def getarea (l,w):
    return 2 * int(l) * int(w)

def totalpaper(areas):
    total = 0
    spare = min(areas)/2
    for element in areas:
        total += element
    return total + spare

def getpaper(dimensions):
# 0 = l, 1 = w, 2 = h
    areas = [getarea (dimensions[0],dimensions[1]),getarea(dimensions[0],dimensions[2]),getarea(dimensions[1],dimensions[2])]
    return totalpaper(areas)

wrappingpaper = 0
data = import_csv(file_path)

for present in data:
    dimensions = present.split('x')
    wrappingpaper += getpaper(dimensions)

print(wrappingpaper)

