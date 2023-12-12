from common import import_csv

def manhattandistance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

file_path = 'Data/LiveDataDay11.txt'
data = import_csv(file_path)

transposeddata = list(zip(*data))
arrayinsert = []
for i, col in enumerate(transposeddata):
    if '#' not in col:
        arrayinsert.append(i + 1)  # Store the index to insert after

# Inserting columns without '#' after the iteration
for index in reversed(arrayinsert):
    transposeddata.insert(index, transposeddata[index-1])

restoreddata = list(zip(*transposeddata))

arrayinsert = []
for i,row in enumerate(restoreddata):
    if '#' not in row:
        arrayinsert.append(i + 1)

for index in reversed(arrayinsert):
    restoreddata.insert(index, restoreddata[index-1])

galaxies = []
for y, row in enumerate(restoreddata):
    for x, char in enumerate(row):
        if char == '#':
            galaxies.append((x, y))  

distances = {}
for i, gal1 in enumerate(galaxies):
    for j, gal2 in enumerate(galaxies):
        if i < j:  
            dist = manhattandistance(gal1, gal2)
            distances[f"Galaxy {i+1} to Galaxy {j+1}"] = dist

print (sum(distances.values()))



