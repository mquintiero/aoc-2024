content = []
with open('day15/input.txt', 'r') as file:
    for line in file:
        content.append(list(line.rstrip("\n")))

def flatten(xss):
    return [x for xs in xss for x in xs]

splitIndex = content.index([])
map = content[:splitIndex]
movements = flatten(content[splitIndex+1:])
robotPosition = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if (map[i][j] == '@'):
            robotPosition = (i, j)
            break

for move in movements:
    match move:
        case '^':
            i = robotPosition[0] - 1
            subMap = []
            while map[i][robotPosition[1]] != '.' and map[i][robotPosition[1]] != '#':
                subMap.append((i, robotPosition[1]))
                i -= 1
            if (map[i][robotPosition[1]] == '.'):
                map[i][robotPosition[1]] = 'O'
                map[robotPosition[0]][robotPosition[1]] = '.'
                map[robotPosition[0] - 1][robotPosition[1]] = '@'
                robotPosition = (robotPosition[0] - 1, robotPosition[1])
        case '>':
            i = robotPosition[1] + 1
            subMap = []
            while map[robotPosition[0]][i] != '.' and map[robotPosition[0]][i] != '#':
                subMap.append((robotPosition[0], i))
                i += 1
            if (map[robotPosition[0]][i] == '.'):
                map[robotPosition[0]][i] = 'O'
                map[robotPosition[0]][robotPosition[1]] = '.'
                map[robotPosition[0]][robotPosition[1] + 1] = '@'
                robotPosition = (robotPosition[0], robotPosition[1] + 1)
        case 'v':
            i = robotPosition[0] + 1
            subMap = []
            while map[i][robotPosition[1]] != '.' and map[i][robotPosition[1]] != '#':
                subMap.append((i, robotPosition[1]))
                i += 1
            if (map[i][robotPosition[1]] == '.'):
                map[i][robotPosition[1]] = 'O'
                map[robotPosition[0]][robotPosition[1]] = '.'
                map[robotPosition[0] + 1][robotPosition[1]] = '@'
                robotPosition = (robotPosition[0] + 1, robotPosition[1])
        case '<':
            i = robotPosition[1] - 1
            subMap = []
            while map[robotPosition[0]][i] != '.' and map[robotPosition[0]][i] != '#':
                subMap.append((robotPosition[0], i))
                i -= 1
            if (map[robotPosition[0]][i] == '.'):
                map[robotPosition[0]][i] = 'O'
                map[robotPosition[0]][robotPosition[1]] = '.'
                map[robotPosition[0]][robotPosition[1] - 1] = '@'
                robotPosition = (robotPosition[0], robotPosition[1] - 1)

coordsSum = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'O':
            coordsSum += i * 100 + j

print(coordsSum)
