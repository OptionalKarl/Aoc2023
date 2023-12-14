from common import import_csv
import numpy as np

file_path = "Data/TestDataDay14.txt"
data = import_csv(file_path)

mapping = {'O': 1, '.': 0, '#': -1}

# Convert each string to a NumPy array using the mapping
rocks = [np.array([mapping[c] for c in s]) for s in data]


def rollnorth(arr, i, i2):
    rolling = True
    pos = i
    while rolling:
        if arr[pos - 1][i2] == 0 and pos - 1 > -1:
            pos -= 1
        else:
            rolling = False
    arr[pos][i2] = 1
    if pos != i:
        arr[i][i2] = 0    


def rollsouth(arr,i,i2):
    rolling = True
    pos = i
    while rolling and pos +1 < len(arr):
        if arr[pos + 1][i2] == 0:
            pos += 1
        else:
            rolling = False
    arr[pos][i2] = 1
    if pos != i:
        arr[i][i2] = 0


def cycle(rocks):         
# Roll all rocks north
    for i, row in enumerate(rocks):
        if i != 0:
            for i2, rock in enumerate(row):
                if rock == 1:
                    rollnorth(rocks, i, i2)
    #roll west
    trocks = np.transpose(rocks)
    for i, row in enumerate(trocks):
        if i != 0:
            for i2, rock in enumerate(row):
                if rock == 1:
                    rollnorth(trocks, i, i2)
    rocks = np.transpose(trocks)

    # roll south
    for i, row in reversed(list(enumerate(rocks))):
        if i != len(rocks) - 1:
            for i2, rock in enumerate(row):
                if rock == 1:
                    rollsouth(rocks, i, i2)
        
    # roll east
    trocks = np.transpose(rocks)
    for i, row in reversed(list(enumerate(trocks))):
        if i != len(trocks) - 1:
            for i2, rock in enumerate(row):
                if rock == 1:
                    rollsouth(trocks, i, i2)  
    rocks = np.transpose(trocks)
    return rocks

maxcycles = 1000000000
rockpatterns = []
cyclenumber = 0
repeatfound = False
while not repeatfound:
    rocks = cycle(rocks)
    rockpattern = []
    for row in rocks:
        rockpattern.append(tuple(row))
    if rockpattern in rockpatterns:
        remainder = maxcycles%cyclenumber
        repeatfound = True
    else: 
        rockpatterns.append(rockpattern)
        cyclenumber +=1

if remainder != 0:
    for i in range(1, remainder + 1):
        rocks = cycle(rocks)

modifier = len(rocks) 
score = 0
for row in rocks:
    score += np.count_nonzero(row == 1) * modifier
    modifier -= 1

print (score)