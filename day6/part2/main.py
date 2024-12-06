from itertools import cycle

content = []
movements = [(-1,0), (0,1), (1,0), (0,-1)]
movementsCycle = cycle(movements)
guardMovement = next(movementsCycle)
guardOut = False
guardPosition = [0,0]
initialPosition = (0,0)

with open('day6/input.txt', 'r') as file:
    for line in file:
        content.append(list(line.rstrip("\n")))

rows = len(content)
cols = len(content[0])

for i in range(len(content)):
    for j in range(len(content[i])):
        if (content[i][j] == '^'):
            guardPosition = initialPosition = (i, j)
            break

def outOfArea(aPosition):
    return aPosition[0] < 0 or aPosition[0] >= rows or aPosition[1] < 0 or aPosition[1] >= cols

def move():
    global guardPosition, guardMovement, guardOut, content
    newPosition = (guardPosition[0] + guardMovement[0], guardPosition[1] + guardMovement[1])
    if (outOfArea(newPosition)): 
        guardOut = True
        content[guardPosition[0]][guardPosition[1]] = 'X'
        return
    if (content[newPosition[0]][newPosition[1]] == '#'):
        guardMovement = next(movementsCycle)
    if (content[newPosition[0]][newPosition[1]] == '.' or content[newPosition[0]][newPosition[1]] == 'X'):
        content[guardPosition[0]][guardPosition[1]] = 'X'
        guardPosition = newPosition
        

while (not guardOut):
    move()

def resetInitialVariables():
    global guardPosition, guardMovement, movementsCycle, initialPosition
    movementsCycle = cycle(movements)
    guardMovement = next(movementsCycle)
    guardPosition = initialPosition
    

def moveGuardWithObstacleIn(area, row, col):
    area[row][col] = '#'
    looped = out = False
    accessedFrom = dict()
    resetInitialVariables()

    while (not out and not looped):
        global guardPosition, guardMovement
        newPosition = (guardPosition[0] + guardMovement[0], guardPosition[1] + guardMovement[1])
        if (outOfArea(newPosition)): 
            out = True
        else:
            if (area[newPosition[0]][newPosition[1]] == '#'):
                guardMovement = next(movementsCycle)
            if (area[newPosition[0]][newPosition[1]] == '.' or area[newPosition[0]][newPosition[1]] == 'X'):
                #Si llego a la misma casilla desde el mismo lugar que alguna otra vez anterior, entonces estoy en un loop
                accessedFrom.setdefault(newPosition, [])
                if(guardPosition in accessedFrom[newPosition]):
                    looped = True
                accessedFrom[newPosition].append(guardPosition)
                guardPosition = newPosition

    area[row][col] = 'X'
    if (looped): return 1
    else: return 0

sum = 0
for i in range(len(content)):
    for j in range(len(content[i])):
        if (content[i][j] == 'X'):
            print("{}, {}".format(i,j))
            area = content.copy()
            sum += moveGuardWithObstacleIn(area, i, j)

print(sum)