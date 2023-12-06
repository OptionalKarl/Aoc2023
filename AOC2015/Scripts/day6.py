from common import import_csv
day = 6
file_path = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day' + str(day) + '.txt'

data = import_csv(file_path)

Instructions = []
action = [] 
rows = 999
columns = 999

# Method 1: Using list comprehension
lights = [[False for _ in range(columns)] for _ in range(rows)]

for row in data:
    inst = []
    if "turn on" in row: action.append(True)
    elif "turn off" in row: action.append(False)
    elif "toggle" in row: action.append("switch")
    references = row.replace('turn on ','').replace('through ','').replace('turn off ','').replace('toggle ','').split(' ')
    for ref in references:
        inst.extend(map(int, ref.split(',')))
    Instructions.append(inst)

def count_instances(array_2d, element):
    count = 0
    for row in array_2d:
        count += row.count(element)
    return count


for index,instr in enumerate(Instructions):
    x = int(0)
    y = int(0)
    for x in range(instr[0],instr[2]+1):
        for y in range(instr[1],instr[3]+1):
            if action[index] != "switch": lights[x][y] = bool(action[index])
            else: lights[x][y] = not lights[x][y]

countTrue = count_instances(lights,True)

print(countTrue)