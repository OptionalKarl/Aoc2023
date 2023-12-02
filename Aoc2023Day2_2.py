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

def checkcolor (checkvalue, color, colortotal, colortally):
    if checkvalue in color and (colortotal > colortally):
        colortally = colortotal
    return colortally

def check_game_win():
    totalgames = 0
    for index, game in enumerate(modifiedlines):
        rounds = game.split(';')
        minred = 0
        mingreen = 0
        minblue = 0
        for round in rounds:
            colors = round.split(',')
            for color in colors:
                color = color.strip()
                minred = checkcolor('red',color,int(color[0:2].strip()),minred)
                mingreen = checkcolor('green',color,int(color[0:2].strip()),mingreen)
                minblue = checkcolor('blue',color,int(color[0:2].strip()),minblue)
        totalgames += (minred * mingreen * minblue)
    return totalgames

            
            


file_path = 'VScode/AocSourceData/AoC2023Day2.txt'
check_csv_file(file_path)
output = check_game_win()



