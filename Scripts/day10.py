from common import import_csv
from matplotlib.path import Path
import math

# Function to calculate the angle of a point with respect to the reference point
def angle_with_ref(point, ref_point):
    return math.atan2(point[1] - ref_point[1], point[0] - ref_point[0])

# Function to get the centroid of a list of points
def centroid(points):
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)
    return x, y

def sort_points_counterclockwise(grid_refs):
    ref = centroid(grid_refs)
    return sorted(grid_refs, key=lambda point: angle_with_ref(point, ref), reverse=True)


def get_points_inside_polygon(grid_refs):
    # Extract X, Y coordinates
    vertices = [(point[0], point[1]) for point in grid_refs]

    # Create a Path object from the vertices
    path = Path(vertices)

    # Get the bounding box to iterate through
    min_x = min(coord[0] for coord in vertices)
    max_x = max(coord[0] for coord in vertices)
    min_y = min(coord[1] for coord in vertices)
    max_y = max(coord[1] for coord in vertices)

    points_inside_polygon = []
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if path.contains_point((x, y)):
                points_inside_polygon.append([x, y])

    return points_inside_polygon

def dotsbetweenpairs(array):
    dot_count = 0
    pair_started = False

    for char in array:
        if char == "P": 
            pair_started = not pair_started
        if char == "." and pair_started:
            dot_count += 1
    
    return dot_count
                

    return sum(dot_counts)

def vertical(prev_y, current_x, current_y):
    new_y = current_y - 1 if prev_y > current_y else current_y + 1
    Newlocation = [current_x, new_y]
    return Newlocation

def horizontal (prev_x, current_x, current_y):
    new_x = current_x - 1 if prev_x > current_x else current_x + 1
    Newlocation = [new_x, current_y]
    return Newlocation

def NorthEast(prev_cord,current_cord):
    if prev_cord[0] != current_cord[0]:
        Newlocation = [current_cord[0], current_cord[1]-1]
    else: Newlocation = [current_cord[0]+1, current_cord[1]]
    return Newlocation

def NorthWest(prev_cord,current_cord):
    if prev_cord[0] != current_cord[0]:
        Newlocation = [current_cord[0], current_cord[1]-1]
    else: Newlocation = [current_cord[0]-1, current_cord[1]]
    return Newlocation

def SouthWest(prev_cord,current_cord):
    if prev_cord[0] == current_cord[0]:
        Newlocation = [current_cord[0]-1, current_cord[1]]
    else: Newlocation = [current_cord[0], current_cord[1]+1]
    return Newlocation

def SouthEast(prev_cord,current_cord):
    if prev_cord[0] == current_cord[0]:
        Newlocation = [current_cord[0]+1, current_cord[1]]
    else: Newlocation = [current_cord[0], current_cord[1]+1]
    return Newlocation

def findstart(ref, map):
    next = []
    if map[ref[1]-1][ref[0]] in ['F','|','7']: next.append([ref[0],ref[1]-1])
    if map[ref[1]][ref[0]+1] in ['J','-','7']: next.append([ref[0]+1,ref[1]])
    if map[ref[1]+1][ref[0]] in ['J','|','L']: next.append([ref[0],ref[1]+1])
    if map[ref[1]][ref[0]-1] in ['L','-','F']: next.append([ref[0]-1,ref[1]])

    return next

file_path = 'Data/LiveDataDay10.txt'
data = import_csv(file_path)

map = []
for index,row in enumerate(data):
    if 'S' in row: Start = [row.index('S'),index]
    map.append(list(row))


NextPos = findstart(Start,map)
distance = 1
prevPos = []
matched = False
prevPos.append(Start)
prevPos.append(Start)
References = []
while matched == False:
    distance += 1
    for index,Pos in enumerate(NextPos):
        
        if map[Pos[1]][Pos[0]] == "|":NextPos[index] = vertical(prevPos[index][1],Pos[0],Pos[1])
        if map[Pos[1]][Pos[0]] == "-":NextPos[index] = horizontal(prevPos[index][0],Pos[0],Pos[1])
        if map[Pos[1]][Pos[0]] == "L":NextPos[index] = NorthEast(prevPos[index],Pos)
        if map[Pos[1]][Pos[0]] == "J":NextPos[index] = NorthWest(prevPos[index],Pos)
        if map[Pos[1]][Pos[0]] == "7":NextPos[index] = SouthWest(prevPos[index],Pos)
        if map[Pos[1]][Pos[0]] == "F":NextPos[index] = SouthEast(prevPos[index],Pos)
        map[Pos[1]][Pos[0]] = "P"
        prevPos[index] = Pos
        if NextPos[0] == NextPos[1]:
            matched = True
            break
total = 0
polyrefs = []
for index,row in enumerate(map):
    yaxis = index
    for index,char in enumerate(row):
       if char == "P":
           polyrefs.append([index,yaxis])

sortedpoly = sort_points_counterclockwise(polyrefs)
points_inside = get_points_inside_polygon(sortedpoly)
total = 0
for point in points_inside:
    if map[point[1]][point[0]] == ".":  total += 1

print (total)


        
