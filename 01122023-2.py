import csv

numbers = ["one","two","three","four","five","six","seven","eight","nine"]

def getnum(startindex, string):
    
    for index, num in enumerate(numbers):
        trimstring = string[startindex:(startindex + len(num))]
        if  trimstring == num:
            return str(index +1)
    return ""

def check_csv_file(file_path): 
    try:
        my_list = []
        calibrationscore = 0
        total = 0

        with open(file_path, 'r') as file:
            for line in file:
                my_list.append(line.strip())
        convertedlist = []
        
        for item in my_list:
                converteditem = ""
                for index, char in enumerate(item):
                    if char.isnumeric():
                         converteditem = converteditem + str(char)
                    else:
                        converteditem = converteditem + getnum(index, item)              
                firstint = converteditem[0]
                if len(converteditem) == 0:
                    secondint = firstint
                else:
                     secondint = converteditem[len(converteditem) - 1]
                calibrationscore = int(str(firstint) + str(secondint))
                total += calibrationscore
        return total
             
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'VScode/AocSourceData/AoC2023Day1.txt'
print (check_csv_file(file_path))
