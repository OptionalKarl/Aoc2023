from common import import_csv, print_grid


def blanktile (pos,dir):
    if dir == "r": pos[0] += 1
    elif dir == "l": pos[0] += -1
    elif dir == "u": pos[1] += -1
    elif dir == "d": pos[1] += 1
    return pos
def forwardangle(pos,dir):
    if dir == "l":
            pos[1] += 1
            dir = "d"
    elif dir == "u":
        pos[0] += 1
        dir = "r"
    elif dir == "d":
        pos[0] -= 1
        dir = "l"
    elif dir == "r":
        pos[1] += -1
        dir = "u"
    return pos, dir
def backangle(pos,dir):
    if dir == "l":
        pos[1] += -1
        dir = "u"
    elif dir == "u":
        pos[0] += -1
        dir = "l"
    elif dir == "d":
        pos[0] += 1
        dir = "r"
    elif dir == "r":
        pos[1] += 1
        dir = "d"
    return pos, dir

def beam (poweredtiles, x = 0, y = 0,dir = "r"):

    pos = [int(x),int(y)]
    while 0 <= int(pos[0]) < len(grid[0]) and 0 <= pos[1] < len(grid):
        current = grid[pos[1]][pos[0]]
        ref = tuple(pos)
        if ref in poweredtiles:
          poweredtiles[ref] += 1
        else: 
            poweredtiles[ref] = 1
        if current == "|" and dir in ["l","r"]:
            if poweredtiles[ref] > 1: return
            beam(poweredtiles, pos[0],pos[1] + -1,"u")
            pos[1] += 1
            dir = "d"
        elif current == "-" and dir in ["u","d"]:
            if poweredtiles[ref] > 1: return
            beam(poweredtiles,pos[0]+1,pos[1],"r")
            pos[0] += -1
            dir = "l"
        elif current == "/": pos, dir = forwardangle(pos,dir)
        elif current == "\\" : pos, dir = backangle(pos,dir)
        else: pos = blanktile(pos,dir)
        # print_grid(len(grid[0]),len(grid),pos,grid)

def Multibeam(x,y,dir):

    poweredtiles = {}

    beam(poweredtiles,x,y,dir)

    return len(poweredtiles)

filepath = "Data/LiveDataDay16.txt"
grid = import_csv(filepath)

inputstart = {}

for i in range(len(grid)):
    score = Multibeam(0,i,"r")
    inputstart["0," + str(i)] = score
    score = Multibeam(len(grid) - 1,i,"l")
    inputstart[str(len(grid) - 1) + "," + str(i)] = score
for i in range(len(grid[0])):
    score = Multibeam(i,0,"d")
    inputstart["0," + str(i)] = score
    score = Multibeam(i,len(grid[0])-1,"u")
    inputstart[str(len(grid[0])-1)+"," + str(i)] = score

highestinput = max(inputstart, key=lambda k: inputstart[k])
print (highestinput)






        




