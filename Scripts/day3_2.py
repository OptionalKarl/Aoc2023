import csv
import re
compareset = []
totalparts = 0
def get_csv_file(file_path):
    try:
        mylist = []
        with open(file_path, 'r') as file:
            for line in file:
                mylist.append(line.strip())
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return mylist

def check_for_star(dataset):
    total = 0
    for index,row in enumerate(dataset):
        rowindex = index
        if '*' in row:
            for index,char in enumerate(row):
                if char == '*': total += findratio(index,row, rowindex)
                
    return total

def findratio(starlocation,row, rownumber):
    result = 0
    numbers = []
    numbers.extend(rowcheck(starlocation,row))
    
    if rownumber > 0:
        row = dataset[rownumber-1]
        numbers.extend(rowcheck(starlocation,row))
        

    if rownumber < len(dataset):
        row = dataset[rownumber+1]
        numbers.extend(rowcheck(starlocation,row))
    if len(numbers) > 1: 
        result = 1
        for num in numbers:
            result *= num
    return result

def rowcheck(starlocation, row):
    numbers=[]
    number = 0
    if row[starlocation].isnumeric():
        number = middlenumber(row,starlocation)
        if number > 0 : numbers.append(number)
        return numbers
    if starlocation > 0 and row[starlocation -1].isnumeric():
        number = backwardsnumber(row,starlocation-1)
        if number > 0 : numbers.append(number)
    if starlocation +1 < len(row) and row[starlocation +1].isnumeric():
        number = 0
        number= forwardsnumber(row, starlocation+1)
        if number > 0 : numbers.append(number)
       
    
    
    return numbers


def backwardsnumber(row, start):
    number = ''
    isnumber = True
    while isnumber:
        number = str(row[start]) + number
        start -= 1
        if start < 0 : isnumber = False
        if not row[start].isnumeric(): isnumber = False
    
    return int(number)

def forwardsnumber(row,start):
    number = ''
    isnumber = True
    while isnumber:
        number = number +  str(row[start])
        start += 1
        if start >= len(row) : isnumber = False
        if isnumber == True:
            if not row[start].isnumeric(): isnumber = False
    return int(number)

def middlenumber(row,start):
    back = start
    forward = start + 1
    number = ''
    isnumber = True
    while isnumber:
        number = str(row[back]) + number
        back -= 1
        if back < 0 : isnumber = False
        if not row[back].isnumeric(): isnumber = False
    if forward < len(row) and row[forward].isnumeric(): isnumber = True
    while isnumber:
        number = number +  str(row[forward])
        forward += 1
        if forward > len(row) : isnumber = False
        if not row[forward].isnumeric(): isnumber = False
    return int(number)


    
dataset = get_csv_file('Data/AoC2024Day3.txt')
print (check_for_star(dataset))

