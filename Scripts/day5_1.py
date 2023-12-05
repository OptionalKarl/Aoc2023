from common import import_csv
def getseeds (data):
        seeds = data[0].replace('seeds: ', '')
        seeds = seeds.split(" ")
        return seeds

def getmap(mapname,data):
    mapcomplete = False
    startindex = data.index(mapname) + 1
    maps = []
    while mapcomplete == False:
        convertrow = data[startindex]
        if convertrow == '' : mapcomplete = True
        else:
                maparray = convertrow.split(" ")
                minval1 = int(maparray[1])
                maxval1 = int(maparray[1]) + int(maparray[2]) - 1
                minval2 = int(maparray[0])
                maxval2 = int(maparray[0]) + int(maparray[2]) - 1
                map = [minval1,maxval1,minval2,maxval2]
                maps.append(map)
                startindex += 1
                if startindex == len(data) - 1: mapcomplete = True

    return maps

def mapper(input,map):
    output = 0
    input = int(input)
    for grid in map:
        if input >= grid[0] and input <= grid[1]:
             increase = input - grid[0]
             output = grid[2] + increase
             break
    if output == 0: output = input 
    return output     

def seedjourney(seed):
    soil = mapper(int(seed),seedtosoil)
    fert = mapper(soil,soiltofertilizer)
    water = mapper(fert,ferttowater)
    light = mapper(water,watertolight)
    temp = mapper(light,lightotemp)
    humidity = mapper(temp,temptohumidity)
    location = mapper(humidity,humiditytolocation)
    return location

print("running")
file_path = 'Data/AoC2023Day5.txt'
data = import_csv(file_path)
seedlist = getseeds(data)
locationlist = []
seedtosoil = getmap('seed-to-soil map:', data)

soiltofertilizer = getmap('soil-to-fertilizer map:',data)

ferttowater = getmap('fertilizer-to-water map:',data)

watertolight= getmap('water-to-light map:',data)

lightotemp = getmap('light-to-temperature map:',data)

temptohumidity = getmap('temperature-to-humidity map:',data)

humiditytolocation = getmap('humidity-to-location map:',data)

for seed in seedlist:
    locationlist.append(seedjourney(seed))

print (min(locationlist))

            
            
            
