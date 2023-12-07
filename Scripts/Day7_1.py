from common import import_csv
import re
def gethands(data):
    hands = []
    for hand in data:
        hands.append(hand.split(' '))
    return hands



rankorder = ['2','3','4','5','6','7','8','9','10','J','Q','K']      
file_path = 'Data/LiveDataDay6.txt'
data = import_csv(file_path)
hands = gethands(data)



five = re.compile(r'^([a-zA-Z\d])\1{4}$')
four = re.compile(r'^(?:([a-zA-Z\d])(?!\1)){0,1}([a-zA-Z\d])\2{3}(?:([a-zA-Z\d])(?!\2))?')
three = re.compile(r'^(?:([a-zA-Z\d])(?!\1)){0,2}([a-zA-Z\d])\2{2}(?:([a-zA-Z\d])(?!\2))?')
twopairs = re.compile(r'^(?:(\w)\1)(?:(?:(?!\1)(\w))\2){2}(?:(?:(?!\1)(?!\2)(\w))\3)?')
onepair = re.compile(r'^.*(\w)\1.*$')


for each hand in hands



