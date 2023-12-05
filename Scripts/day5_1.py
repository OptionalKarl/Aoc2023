from common import import_csv
def getseeds (data):
        seeds = data[0].replace('seeds: ', '')
        seeds = seeds.split(" ")
        return seeds

def getmap(mapname,data):
    mapcomplete = False
    startindex = data.index(mapname)
    map1 = []
    map2 = []
    while mapcomplete == False:
        convertrow = data[startindex +1]
        if convertrow == '' : mapcomplete = True
        else:
                maparray = convertrow.split(" ")
                for x in range(0, int(maparray[2])):
                        map1.append(int(maparray[1]) + x)
                        map2.append(int(maparray[0]) + x)
                startindex += 1
                if startindex == len(data) - 1: mapcomplete = True
    maps = [map1,map2]
    return maps

def mapper(input,map):
    output = 0
    input = int(input)
    if input in map[0]:
        outputindex = map[0].index(input)
        output = map[1][outputindex]
    else: output = input
    return output   
       







file_path = 'Data\TestDataDay5.txt'
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
    location = mapper(humidity,humiditytolocation)
    locationlist.append(location)

            
            
            

