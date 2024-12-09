file = open('day9/input.txt', 'r')
content = list(file.read())
memoryMap = []
currentId = 1

for i in range(len(content)):
    if (i % 2 == 0):
        memoryMap.append((currentId, int(content[i])))
        currentId += 1
    else:
        memoryMap.append((0, int(content[i])))

for i in range(len(memoryMap))[::-1]:
    i_data, i_size = memoryMap[i]
    j = i_data and next((j for j in range(i) if not memoryMap[j][0] and memoryMap[j][1] >= i_size), 0)
    if j:
        j_data, j_size = memoryMap[j]
        memoryMap[i] = (0, i_size)
        memoryMap[j] = (0, j_size - i_size)
        memoryMap.insert(j, (i_data, i_size))

def blockTotal(aBlock, index):
    if (aBlock[0] == 0): return (0, index + aBlock[1])
    total = 0
    for k in range(aBlock[1]):
        total += (aBlock[0] - 1) * index
        index += 1
    return (total, index)

sum = 0
index = 0
for block in memoryMap:
    result = blockTotal(block, index)
    sum += result[0]
    index = result[1]

print(sum)