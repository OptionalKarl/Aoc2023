from common import import_csv

file_path = 'Data/day8.txt'
data = import_csv(file_path)

instructions = data[0].replace('L','0').replace('R','1')
data = data[2:]
locations = []
mapping = []
currentlocation = 'AAA'
for row in data:
    parts = row.split(' = ')
    
    value1 = parts[0].strip()
    value2, value3 = parts[1][1:-1].split(',')
    locations.append(value1)
    mapping.append([value2.strip(),value3.strip()])
steps = 0
currentlocation = 'AAA'

while currentlocation != 'ZZZ':
    for instr in instructions:
        steps += 1
        nextindex = locations.index(currentlocation)
        locations = mapping[nextindex][int(instr)]
        if currentlocation == 'ZZZ': break

print(steps)