from common import import_csv

import re
def gethands(data):
    hands = []
    for hand in data:
        hands.append(hand.split(' '))
    return hands

def fullhouse(string):
    unique_chars = set(string)
    if len(unique_chars) == 2:
        for char in unique_chars:
            if string.count(char) < 2:
                return False
        return True
    return False
def twopair(string):
    unique_chars = set(string)
    if len(unique_chars) == 3:
        for char in unique_chars:
            if string.count(char) > 3:
                return False
        return True
    return False

rankorder = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']      
file_path = 'Data/LiveDataDay7.txt'
data = import_csv(file_path)
hands = gethands(data)



five = re.compile(r'^([a-zA-Z\d])\1{4}$')
four = re.compile(r'^.*(\w).*\1.*\1.*\1.*$')
three = re.compile(r'^.*(\w).*\1.*\1.*$')
twopairs = re.compile(r'^.*(\w).*\1.*(\w).*\2.*$')
onepair = re.compile(r'^.*(\w).*\1.*$')


for index,hand in enumerate(hands):
    baserank = rankorder.index(hand[0][0])
    secondbaserank = rankorder.index(hand[0][1])
    thirdbaserank = rankorder.index(hand[0][2])
    fourthbaserank = rankorder.index(hand[0][3])
    fifthbaserank = rankorder.index(hand[0][4])
    winrank= 0
    if five.match(hand[0]): winrank = 7
    elif four.match(hand[0]): winrank = 6
    elif fullhouse(hand[0]): winrank = 5
    elif three.match(hand[0]): winrank = 4
    elif twopair(hand[0]): winrank = 3
    elif onepair.match(hand[0]): winrank = 2
    else: winrank = 1

    hands[index].append(winrank)
    hands[index].append(baserank)
    hands[index].append(secondbaserank)
    hands[index].append(thirdbaserank)
    hands[index].append(fourthbaserank)
    hands[index].append(fifthbaserank)

sortedhands = sorted(hands, key=lambda x: (x[2], x[3], x[4],x[5], x[6], ))  # Sort by y (index 2) and z (index 3)
total = 0
for index,hand in enumerate(sortedhands):
    total+= (index + 1) * int(hand[1])

print (total)




