from common import import_csv

def manhattandistance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

file_path = 'Data/LiveDataDay11.txt'
data = import_csv(file_path)

transposeddata = list(zip(*data))
colmod = []
for i, col in enumerate(transposeddata):
    if '#' not in col:
        colmod.append(i + 1)  # Store the index to insert after


restoreddata = list(zip(*transposeddata))

rowmod = []
for i,row in enumerate(restoreddata):
    if '#' not in row:
        rowmod.append(i + 1)

galaxies = []
for y, row in enumerate(restoreddata):
    for x, char in enumerate(row):
        if char == '#':
            galaxies.append((x, y))  

spacemodifier = 999999
distances = {}
for i, gal1 in enumerate(galaxies):
    for j, gal2 in enumerate(galaxies):
        if i < j:  
            dist = manhattandistance(gal1, gal2)
            for col_index in colmod:
                if min(gal1[0], gal2[0]) < col_index <= max(gal1[0], gal2[0]):
                    dist += spacemodifier  # Add 9 if path passes through modified column
            
            for row_index in rowmod:
                if min(gal1[1], gal2[1]) < row_index <= max(gal1[1], gal2[1]):
                    dist += spacemodifier  # Add 9 if path passes through modified row

            distances[f"Galaxy {i+1} to Galaxy {j+1}"] = dist

print (sum(distances.values()))