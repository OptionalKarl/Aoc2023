from common import import_csv
file_path = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day2.txt'



def getribbon (l,w,h):
    bow = h * l * w
    wrap = (h + l + w - max([h,l,w])) * 2
    return int(bow) + int(wrap)


data = import_csv(file_path)
ribbon = 0
for present in data:
    dimensions = present.split('x')
    ribbon += getribbon(int(dimensions[0]),int(dimensions[2]),int(dimensions[1]))

print(ribbon)

