import sys


from common import import_csv

def Loopandsum(Data):
    total = 0
    for item in Data:
            firstint = 0
            secondint = 0
            calibrationscore = 0
            for char in item:
                if char.isnumeric():
                    if firstint == 0:
                        firstint = char
                    else:
                        secondint = char
            if secondint == 0:
                secondint = firstint
            calibrationscore = int(str(firstint) + str(secondint))
            total += calibrationscore
    return total         

file_path = "D:/Storage/1 - Home Files/Solutions/Aoc2023/Data/AoC2023Day1.txt"
Data = import_csv(file_path)
output = Loopandsum(Data)
