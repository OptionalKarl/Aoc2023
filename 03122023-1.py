import csv
import re
compareset = []
total = 0
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
    comparerow = compareset[rowindex]
    startindex = 0
    for index,char in enumerate(row):
        if char.isnumeric() and found == False:
            startindex = index
            found = True
        if not char.isnumeric() and found == True:
            endindex = index-1
            validnumber = checkcompare(startindex, endindex,rowindex)
            found = False
        if validnumber:
            total += int(row[startindex:endindex])
            validnumber = False

def checkcompare(startindex,endindex,rowindex):
    if startindex > 0:
        startindex -= 1
    if endindex < 9:
        endindex += 1
    if rowindex > 0:
        comparerow = compareset[rowindex-1]
        if 's' in comparerow[startindex:endindex]:
            return True
    if rowindex < len(compareset):
        comparerow = compareset[rowindex+1]
        if 's' in comparerow[startindex:endindex]:
            return True
    comparerow = compareset[rowindex]
    if 's' in comparerow[startindex:endindex]:
        return True
    return False

dataset = get_csv_file('Data/AoC2024Day3.txt')
get_compare_set(dataset)

# First item logic
for index,row in enumerate(dataset):
    checkchar(index,row)