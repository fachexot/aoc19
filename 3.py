f = open('input3.txt')
wire1 = f.readline().strip().split(',')
wire2 = f.readline().strip().split(',')

def goLeft(path, distance):
    for step in range(0, distance):
        path.append([path[-1][0]-1,path[-1][1]])

def goRight(path, distance):
    for step in range(0, distance):
        path.append([path[-1][0]+1,path[-1][1]])

def goUp(path, distance):
    for step in range(0, distance):
        path.append([path[-1][0],path[-1][1]+1])

def goDown(path, distance):
    for step in range(0, distance):
        path.append([path[-1][0],path[-1][1]-1])

def calcManhattenDistance(coordinate):
    return abs(coordinate[0]) + abs(coordinate [1])
    

path1 = [[0,0]]
for command in wire1:
    direction = command[0]
    distance = int(command [1:])

    if direction == 'L':
        goLeft(path1, distance)
    elif direction == 'R':
        goRight(path1, distance)
    elif direction == 'U':
        goUp(path1, distance)
    elif direction == 'D':
        goDown(path1, distance)
    else:
        print("HALT AND CATCH FIRE: Directive " + direction + " for wire1 unknown.")
        break

path2 = [[0,0]]
for command in wire2:
    direction = command[0]
    distance = int(command [1:])

    if direction == 'L':
        goLeft(path2, distance)
    elif direction == 'R':
        goRight(path2, distance)
    elif direction == 'U':
        goUp(path2, distance)
    elif direction == 'D':
        goDown(path2, distance)
    else:
        print("HALT AND CATCH FIRE: Directive " + direction + " for wire2 unknown.")
        break

distances = list(map(calcManhattenDistance, set(map(tuple, path1)).intersection(map(tuple,path2))))
distances.remove(0)
mindistance = min(distances)

print(mindistance)