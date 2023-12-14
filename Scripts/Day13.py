from common import import_csv




def orgdata(data):
    datasets = []
    temp_array = []

    for item in data:
        if len(item) == 0:
            if len(temp_array) > 0:
                datasets.append(temp_array)
                temp_array = []
        else:
            temp_array.append(item)

    if len(temp_array) > 0:
        datasets.append(temp_array)
    return datasets

def rowcheck(set):
    max = len(set)-1
    symfound = 0
    for index, row in enumerate (set):
        if index == max: break
        if row == set[index+1]:
            symfound = symcheck(index,set)
        if symfound != 0: break
    return symfound



def symcheck(mirror1,set):
    mirror2 = mirror1 + 1
    max = len(set) -1
    loop = True
    symfound = mirror1
    while loop == True:
        if set[mirror1] == set[mirror2]:
            mirror1-=1
            mirror2+=1
            
            if mirror1 < 0 or mirror2 > max: 
                loop = False
                symfound +=1
        else:
            symfound = 0
            loop = False
    
    return symfound 




file_path = 'Data/LiveDataDay13.txt'
datasets = orgdata(import_csv(file_path))

total = 0
for set in datasets:
    total += 100 * rowcheck(set)
    transposedset = list(zip(*set))
    total += rowcheck(transposedset)

print (total)


    



