from itertools import cycle

content = []
movements = [(-1,0), (0,1), (1,0), (0,-1)]
movementsCycle = cycle(movements)
guardMovement = next(movementsCycle)
guardOut = False
guardPosition = [0,0]

with open('day6/input.txt', 'r') as file:
    for line in file:
        content.append(list(line.rstrip("\n")))

rows = len(content)
cols = len(content[0])

for i in range(len(content)):
    for j in range(len(content[i])):
        if (content[i][j] == '^'):
            guardPosition = (i, j)
            break

print(guardPosition)

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

sum = 0
for line in content:
    sum += line.count('X')

print(sum)