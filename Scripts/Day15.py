from common import import_csv



def runhash( item, cv = 0):
    mult = 17
    mod = 256
    for i in item:
        cv += ord(i)
        cv *= mult
        cv = cv%mod
    return cv




filepath = "Data/LiveDataDay15.txt"
data = import_csv(filepath)
total = 0
inputs = data[0].split(",")

for input in inputs:
    total += runhash(input)

print (total)

