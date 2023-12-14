from common import import_csv
import numpy as np

file_path = "Data/LiveDataDay14.txt"
data = import_csv(file_path)

mapping = {'O': 1, '.': 0, '#': -1}

# Convert each string to a NumPy array using the mapping
rocks = [np.array([mapping[c] for c in s]) for s in data]


def roll(rocks, i, i2, inverse = False):
    rolling = True
    pos = i
    while rolling:
        if not inverse:
            if rocks[pos - 1][i2] == 0 and pos - 1 > -1:
                pos -= 1
            else:
                rocks[pos][i2] = 1
                if pos != i:
                    rocks[i][i2] = 0
                rolling = False
        elif inverse:
            if rocks[pos + 1][i2] == 0 and pos + 1 < len(rocks):
                pos += 1
            else:
                rocks[pos][i2] = 1
                if pos != i:
                    rocks[i][i2] = 0
                rolling = False


for i, row in enumerate(rocks):
    if i != 0:
        for i2, rock in enumerate(row):
            if rock == 1: roll(rocks, i,i2)

modifier = len(rocks) 

score = 0
for row in rocks:
    score += np.count_nonzero(row == 1) * modifier
    modifier -= 1

print (score)
    

            
