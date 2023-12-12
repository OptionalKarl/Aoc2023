from common import import_csv

def getdifference(sequence):
    recurse = True
    increased = False
    differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

    while recurse:
        if len(set(differences)) == 1 or increased == True:
            recurse = False
            increased = False
            sequence.insert(0, sequence[0] - differences[0])
            return sequence
        else:
            recurse = True
            differences = getdifference(differences)
            increased = True



file_path = 'Data/LiveDataDay9.txt'
data = import_csv(file_path)
sequences = []
newsequences = []
for d in data:
    seq = d.split(" ")
    sequences.append(seq)

sequences = [list(map(int, array)) for array in sequences]
for seq in sequences:
    newsequences.append (getdifference(seq))
total = 0
for s in newsequences:
    total += s[0]

print (total)


    



