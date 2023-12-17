import csv
import sys

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # Reset to default color

def print_grid(x,y, current,gridyx):
    for j in range(y):
        for i in range(x):
            coord = gridyx[j][i]
            if i == current[0] and j == current[1]:
                color = Color.BLUE
                 # Highlight current position with [*]
            else:
                color = Color.RED
            print(f"{color}{coord}", end=" ")    
        print()  # Move to the next line after each row
    print("________________________")
    print()
    print()

def import_csv(filepath):
    mylist = []
    with open(filepath, 'r') as file:
            for line in file:
                mylist.append(line.strip())
    return mylist
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



