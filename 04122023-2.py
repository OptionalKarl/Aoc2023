from common import import_csv 
import unittest


def splitcard(card):

    halves = card.split('|')
    for half in halves:
        half = half.strip()
    return halves

def cleanData(data):
    winningnNums = []
    cardNumms = []
    total = 0
    tidydata = []
    for index,row in enumerate(data):
        row = row.replace('Card ' + str(index+1) +': ', '')
        winCounter = 0
        halves = splitcard(row)
        tidydata.append(halves)
    
    return tidydata
def checkresults(data):
    total = 0
    stoprun = len(data)
    for index,halves in enumerate(data):
        if index >= stoprun:
            break
        
        
        scratchruns = [x for x in data if x == halves]
        for halves in scratchruns:
            winCounter = 1
            winningNums = halves[0].split(' ')
            cardNums =  halves[1].split(' ')
            
            for num in cardNums:
                if num != '' and num in winningNums:
                    data.append(data[index + winCounter])
                    winCounter += 1

    
    return len(data)
file_path = 'Data/AoC2023Day4.txt'
data = import_csv(file_path)
data = cleanData(data)
score = 0
score = checkresults(data)

print(len(data))