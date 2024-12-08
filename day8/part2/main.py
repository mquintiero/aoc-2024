content = []
antennaLocations = dict()
with open('day8/input.txt', 'r') as file:
    for line in file:
        content.append(list(line.rstrip("\n")))

rows = len(content)
cols = len(content[0])

def outOfArea(aPosition):
    return aPosition[0] < 0 or aPosition[0] >= rows or aPosition[1] < 0 or aPosition[1] >= cols

for y in range(len(content)):
    for x in range(len(content[y])):
        if (content[y][x] != '.'):
            antennaLocations.setdefault(content[y][x], [])
            antennaLocations[content[y][x]].append((y, x))

antinodes = set()
for locations in antennaLocations.values():
    for i in range(len(locations)):
        j = i + 1
        while(j < len(locations)):
            distance = (locations[i][0] - locations[j][0], locations[i][1] - locations[j][1])
            antinodeLocation1 = (locations[i][0] + distance[0], locations[i][1] + distance[1])
            antinodeLocation2 = (locations[i][0] - distance[0], locations[i][1] - distance[1])
            antinodes.add(locations[i]) #Como en los ciclos no contemplo como antinodo a la antena que uso para iterar, la agrego manualmente
            while (not outOfArea(antinodeLocation1)):
                antinodes.add(antinodeLocation1)
                antinodeLocation1 = (antinodeLocation1[0] + distance[0], antinodeLocation1[1] + distance[1])
            while (not outOfArea(antinodeLocation2)):
                antinodes.add(antinodeLocation2)
                antinodeLocation2 = (antinodeLocation2[0] - distance[0], antinodeLocation2[1] - distance[1])
            j += 1

print(len(antinodes))