import csv
modifiedlines = []
comparisonarray = [12,13,14]

def check_csv_file(file_path): 
    try:
        

        with open(file_path, 'r') as file:
            for index, line in enumerate(file):
                modifiedlines.append(line.replace('Game ' + str(index+1) +': ', ''))
   
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def check_game_win():
    totalgames = 0
    for index, game in enumerate(modifiedlines):
        rounds = game.split(';')
        cheatgame = False
        for round in rounds:
            colors = round.split(',')
            for color in colors:
                color = color.strip()
                if 'red' in color:
                    if int(color[0:2].strip()) > comparisonarray[0]:
                        cheatgame = True
                elif 'green' in color:
                    if int(color[0:2].strip()) > comparisonarray[1]:
                        cheatgame = True
                elif 'blue' in color:
                    if int(color[0:2].strip()) > comparisonarray[2]:
                        cheatgame = True
        if not cheatgame:
            totalgames += index+1
    return totalgames

            
            


file_path = 'VScode/AocSourceData/AoC2023Day2.txt'
check_csv_file(file_path)
output = check_game_win()



