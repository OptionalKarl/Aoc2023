
import numpy as np

def getdata(file_path):
    with open(file_path, 'r') as f:
        arraystr = f.read().strip().split('\n\n')
    sets = [np.array([list(row) for row in set.split('\n')]) for set in arraystr]
    return [np.where(set == '#', 1, 0) for set in sets]


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

def rowcheck(modset,columnsmudge = 0, rowsmudge = 0,first = 0,type=1):

    max = len(modset)-1
    symfound = 0
    for index, row in enumerate (modset):
        if index == max: break
        if row == set[index+1]:
            symfound = symcheck(index,modset,columnsmudge = 0, rowsmudge = 0)
        if symfound != 0 and first*type != symfound*type:
                return symfound*type
    return symfound



def symcheck(mirror1,set,columnsmudge = 0, rowsmudge = 0):
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
    if columnsmudge > 0:
        if not mirror1 <= columnsmudge <= mirror2: symfound = 0
    if rowsmudge > 0:
        if not mirror1 <= rowsmudge <= mirror2: symfound = 0
    return symfound 

def getanswers(set,columnsmudge = 0, rowsmudge = 0, first = 0):
    temptotal = 0
    temptotal += rowcheck(set,columnsmudge, 0,first,100)
    if temptotal == 0:
        transposedset = list(zip(*set))
        cleantranspose = []
        for set in transposedset:
            cleantranspose.append(''.join(set))
        temptotal += rowcheck(set,0, rowsmudge,cleantranspose,first)
    
    return temptotal
def findsmudge(array):
    for i in range(1, array.shape[0]):
        if i <= array.shape[0] // 2:
            diff = array[:i, :] - array[i:2*i, :][::-1]
            if np.count_nonzero(diff) == 1: 
                return i
        else:
            diff = array[i:, :] - array[2*i-array.shape[0]:i, :][::-1]
            if np.count_nonzero(diff) == 1:  
                return i

    return None

def process(arrays):
    summary = 0
    for array in arrays:
        horizontal_result = findsmudge(array)
        if horizontal_result is not None:
            summary += 100 * horizontal_result

        vertical_result = findsmudge(array.T)
        if vertical_result is not None:
            summary += vertical_result

    return summary


file_path = 'Data/TestDataDay13.txt'
datasets = getdata(file_path)

result = process(datasets)
print (result)


    



