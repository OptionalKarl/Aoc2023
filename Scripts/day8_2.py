from common import import_csv

file_path = 'Data/day8.txt'
data = import_csv(file_path)

instructions = data[0].replace('L','0').replace('R','1')
data = data[2:]
locations = []
mapping = []
for row in data:
    parts = row.split(' = ')
    value2, value3 = parts[1][1:-1].split(',')
    locations.append(parts[0].strip())
    mapping.append([value2.strip(),value3.strip()])

currentlocation = []
for l in locations:
    if l[2] == 'A': 
        currentlocation.append(l)
steps = 0
home = False
while not home:
    for instr in instructions:
        steps += 1
        for index,l in enumerate(currentlocation):      
            nextindex = locations.index(l)
            l = mapping[nextindex][int(instr)]
            currentlocation[index] = l
        if all(l[-1] == 'Z' for l in currentlocation): 
            home = True
            break

print(steps)