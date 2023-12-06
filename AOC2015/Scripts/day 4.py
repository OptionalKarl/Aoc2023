from common import import_csv
import hashlib

file_path = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day4.txt'

leading0 = False
str2hash = "ckczppom"
x = 1
while leading0 == False:
    tohash = str2hash + str(x)
    result = hashlib.md5(tohash.encode())
    if result.hexdigest()[0:6] == '000000':
        leading0 = True
        print (x)
    else :
        x += 1






