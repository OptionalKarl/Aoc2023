from common import import_csv
def getseeds (data):
        seeds = data[0].replace('seeds: ', '').split(" ")
        return seeds
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



file_path = 'Data/AoC2023Day5.txt'
data = import_csv(file_path)
seedlist = getseeds(data)
seedtosoil = getmap('seed-to-soil map:', data)
soiltofertilizer = getmap('soil-to-fertilizer map:',data)
ferttowater = getmap('fertilizer-to-water map:',data)
watertolight= getmap('water-to-light map:',data)
lightotemp = getmap('light-to-temperature map:',data)
temptohumidity = getmap('temperature-to-humidity map:',data)
humiditytolocation = getmap('humidity-to-location map:',data)
locationlist = []


for seed in seedlist:
    soil = mapper(int(seed),seedtosoil)
    fert = mapper(soil,soiltofertilizer)
    water = mapper(fert,ferttowater)
    light = mapper(water,watertolight)
    temp = mapper(light,lightotemp)
    humidity = mapper(temp,temptohumidity)
    locationlist.append(mapper(humidity,humiditytolocation))

import time
start_time = time.time()



print (min(locationlist))
print("--- %s seconds ---" % (time.time() - start_time))
            
            
            

