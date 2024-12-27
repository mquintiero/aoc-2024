schematic = []
locks = []
keys = []

def lockHeights(schematic):
    heights = [0] * len(schematic[0])
    for j in range(len(schematic[0])):
        i = 1
        while (i < len(schematic) and schematic[i][j] != '.'):
            heights[j] += 1
            i += 1
    return heights

def keyHeights(schematic):
    heights = [0] * len(schematic[0])
    for j in range(len(schematic[0])):
        i = len(schematic) - 2
        while (i >= 0 and schematic[i][j] != '.'):
            heights[j] += 1
            i -= 1
    return heights

def fit(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True

with open('day25/input.txt', 'r') as file:
    for line in file:
        if line == '\n':
            if schematic[0] == ['#', '#', '#', '#', '#']:
                locks.append(lockHeights(schematic))
            else:
                keys.append(keyHeights(schematic))
            schematic = []
            continue
        schematic.append(list(line.rstrip('\n')))

#Chequeo el ultimo esquema manualmente porque no hay un salto de linea
if schematic[0] == ['#', '#', '#', '#', '#']:
    locks.append(lockHeights(schematic))
else:
    keys.append(keyHeights(schematic))

fits = 0
for lock in locks:
    for key in keys:
        if fit(key, lock):
            fits += 1

print(fits)
