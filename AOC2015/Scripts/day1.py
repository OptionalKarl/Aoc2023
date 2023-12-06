from common import import_csv

file_path = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day1.txt'

data = import_csv(file_path)

floor = data[0].count("(") - data[0].count(")")
print(floor)