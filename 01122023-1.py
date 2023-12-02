import csv

def check_csv_file(file_path):
    try:
        my_list = []
        calibrationscore = 0
        total = 0

        with open(file_path, 'r') as file:
            for line in file:
                my_list.append(line.strip())
        
        for item in my_list:
                firstint = 0
                secondint = 0
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

                         
                         
                    
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'VScode/AocSourceData/AoC2023Day1.txt'
print (check_csv_file(file_path))
