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


def get_compare_set(dataset):

    for data in dataset:
        row  = ''
        for char in data:
            if char.isnumeric():
                row = row + str('1')
            elif re.match(r'[^\d.]', char) and char != '.':
                row = row + str('s')
            else:
                row = row + str('.')
        compareset.append(row)
                
def checkchar (rowindex,row):
    validnumber = False
    found = False
    startindex = 0
    total = 0
    for index,char in enumerate(row):
        if char.isnumeric() and found == False:
            startindex = index
            found = True
        if not char.isnumeric() and found == True:
            endindex = index
            validnumber = checkcompare(startindex, endindex,rowindex)
            found = False
        if index == len(row)-1 and found == True:
            endindex = index
            validnumber = checkcompare(startindex, endindex,rowindex)
            found = False
        if validnumber:
            num = row[startindex:endindex]
            total = total + int(num)
            validnumber = False
    return total
def checkcompare(startindex,endindex,rowindex):
    length = len(compareset[0])
    if startindex > 0:
        startindex -= 1
    if endindex < length-1:
        endindex += 1
    if rowindex > 0:
        comparerow = compareset[rowindex-1]
        comparestring = comparerow[startindex:endindex]
        if 's' in comparerow[startindex:endindex]:
            return True
    if rowindex < len(compareset) -1:
        comparerow = compareset[rowindex+1]
        comparestring = comparerow[startindex:endindex]
        if 's' in comparerow[startindex:endindex]:
            return True
    comparerow = compareset[rowindex]
    comparestring = comparerow[startindex:endindex]
    if 's' in comparerow[startindex:endindex]:
        return True
    return False

dataset = get_csv_file('Data/AoC2024Day3.txt')
get_compare_set(dataset)

# First item logic
for index,row in enumerate(dataset):
    totalparts += checkchar(index,row)
print(totalparts)