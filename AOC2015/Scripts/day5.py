from common import import_csv
import re

file_path = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day5.txt'

data = import_csv(file_path)
                  
def exclusion(string):
    excludelist = ["ab", "cd", "pq", "xy"]

    for pair in excludelist:
        if pair in string: return True

def validvowels(string):
    vowels = ["a","e","i","o","u"]
    Total = 0
    for vowel in vowels:
        Total += string.count(vowel)
        if Total > 2 : return True

def validpairs(string):
    pattern = re.compile(r'(.)\1')

    return bool(pattern.search(string))


total = 0
for row in data:
    if validpairs(row) and validvowels(row)  and not exclusion(row): total +=  1

print(total)

    
