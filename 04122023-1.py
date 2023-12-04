from common import import_csv 
import unittest


def splitcard(card):

    halves = card.split('|')
    for half in halves:
        half = half.strip()
    return halves

def checkresults(data):
    winningnNums = []
    cardNumms = []
    total = 0
    for index,row in enumerate(data):
        row = row.replace('Card ' + str(index+1) +': ', '')
        winCounter = 0
        halves = splitcard(row)
        winningnNums = halves[0].split(' ')
        cardNums =  halves[1].split(' ')
        for num in cardNums:
            if num != '' and num in winningnNums:
                if winCounter == 0: winCounter = 1
                else: winCounter *=2
        total += winCounter
    return total

file_path = 'Data\AoC2023Day4.txt'
data = import_csv(file_path)

score = checkresults(data)

print(score)