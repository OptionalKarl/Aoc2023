from common import import_csv
import time
start_time = time.time()
def get_durations(row):
    row = row.replace('Time:      ','')
    distances = list(filter(bool, row.replace().split('')))
    return distances
def get_times(row):
       newtimes = []
       row = row.replace('Distance:  ','')
       times = row.split('  ')
       for time in times:
            newtime = time.strip()
            newtimes.append(newtime)
            

       return newtimes

def calcvalidtimes(Raceduration,Topscore):
    Validtimes = 0
    for z in range(1,(int(Raceduration)-1)):
        timeleft = Raceduration - z
        distance = z*timeleft
        if distance > Topscore : Validtimes +=1
    return Validtimes

def calcvalidtimes2(race_duration, top_score):
    valid_times = max(0, race_duration - top_score // race_duration)
    return valid_times

total1 = 1

file_path = 'Data/LiveDataDay6.txt'
data = import_csv(file_path)


distance = 377117112241505
duration = 51699878

total1 = calcvalidtimes(duration,distance)

print("--- %s seconds ---" % (time.time() - start_time))
print(total1)




