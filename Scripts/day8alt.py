from common import import_csv
import math

file_path = 'Data/day8.txt'
data = import_csv(file_path)

instructions = data[0].translate(str.maketrans('LR', '01'))
data = data[2:]
locations = {}
mapping = []

for index, row in enumerate(data):
    parts = row.split(' = ')
    value2, value3 = parts[1][1:-1].split(',')
    location = parts[0].strip()
    locations[location] = index
    mapping.append([value2.strip(), value3.strip()])

currentlocation = [location for location in locations if location.endswith('A')]
home = False
totalsteps = []

for index, l in enumerate(currentlocation):
    steps = 0
    home = False
    while not home:
        for instr in instructions:
            steps += 1
            nextindex = locations[l]
            l = mapping[nextindex][int(instr)]
            currentlocation[index] = l
            if currentlocation[index].endswith('Z'): 
                totalsteps.append(steps)
                home = True
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b) if a and b else 0

def lcm_of_list(numbers):
    lcm_result = 1
    for num in numbers:
        lcm_result = lcm(lcm_result, num)
    return lcm_result




# Calculate the LCM of the list
result = lcm_of_list(totalsteps)

print(result)
