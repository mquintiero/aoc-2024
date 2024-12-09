file = open('day9/input.txt', 'r')
content = list(file.read())
blockMap = []
currentId = 0

for i in range(len(content)):
    if (i % 2 == 0):
        for k in range(int(content[i])):
            blockMap.append(str(currentId))
        currentId += 1
    else:
        for k in range(int(content[i])):
            blockMap.append('.')

while '.' in blockMap:
    dotIndex = blockMap.index('.')
    blockMap[dotIndex] = blockMap.pop()

sum = 0
for i in range(len(blockMap)):
    sum += i * int(blockMap[i])


print(sum)