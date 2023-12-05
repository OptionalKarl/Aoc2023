from common import import_csv
def getseeds (data):
        seeds = data[0].replace('seeds: ', '')
        seeds = seeds.split(" ")
        newseeds = [[int(seeds[i]), int(seeds[i]) + int(seeds[i+1])] for i in range(0, len(seeds), 2) if i+1 < len(seeds)]
        return newseeds

def getmap(mapname,data):
    startindex = data.index(mapname) + 1
    maps = []
    while startindex < len(data):
        convertrow = data[startindex]
        if not convertrow:
            break
        maparray = convertrow.split(" ")
        minval1 = int(maparray[1])
        maxval1 = minval1 + int(maparray[2]) - 1
        minval2 = int(maparray[0])
        maps.append([minval1, maxval1, minval2])
        startindex += 1
    return maps

def mapper(input_val, map_data):
    input_val = int(input_val)
    output = input_val
    for grid in map_data:
        if grid[0] <= input_val <= grid[1]:
            output = grid[2] + (input_val - grid[0])
            break
    return output 

def seedjourney(seed):
    location = seed
    for mapper_func in maps:
        location = mapper(location, mapper_func)
    return location

def process_seeds(seed_list, maps):
    for seed_pair in seed_list:
        for seed in range(seed_pair[0], seed_pair[1]):
            loc = seedjourney(seed, maps)

file_path = 'Data/AoC2023Day5.txt'
data = import_csv(file_path)
seedlist = getseeds(data)
minlocation = 0
seedtosoil = getmap('seed-to-soil map:', data)
soiltofertilizer = getmap('soil-to-fertilizer map:',data)
ferttowater = getmap('fertilizer-to-water map:',data)
watertolight= getmap('water-to-light map:',data)
lightotemp = getmap('light-to-temperature map:',data)
temptohumidity = getmap('temperature-to-humidity map:',data)
humiditytolocation = getmap('humidity-to-location map:',data)
maps = [seedtosoil, soiltofertilizer, ferttowater, watertolight, lightotemp, temptohumidity, humiditytolocation]

for seedpair in seedlist:
    for seed in range(int(seedpair[0]),int(seedpair[1])):
        loc = seedjourney(seed)
        if minlocation != 0: minlocation = min(loc, minlocation)
        else: minlocation = loc

print (minlocation)

