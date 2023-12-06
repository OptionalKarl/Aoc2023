from common import import_csv

def get_durations(row):
    row = row.replace('Time:      ','')
    durations = row.split(' ')
    distances = list(filter(bool, durations))
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
total2 = 1
file_path = 'Data/LiveDataDay6.txt'
data = import_csv(file_path)
durations = get_durations(data[0])
distance = get_times(data[1])

for index,duration in enumerate(durations):

    total1 *= calcvalidtimes(int(duration),int(distance[index]))


print(total1)




