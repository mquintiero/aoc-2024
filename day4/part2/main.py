file = open("day4/input.txt", "r")
line = []
wordsFormed = ['']*2
total = 0

for i in file:
    line.append('Z' + i.strip() + 'Z')

topAndBottomPadding = 'Z' * (len(line[0])+2)
    
for i in range(3):
    line.insert(0, topAndBottomPadding)
    line.append(topAndBottomPadding)

for y in range(len(line)):
    for x in range(len(line[y])):
        if line[y][x] == 'A':
            wordsFormed[0] = line[y - 1][x - 1] + line[y][x] + line[y + 1][x + 1] #Left to right - top to bottom diagonal
            wordsFormed[1] = line[y + 1][x - 1] + line[y][x] + line[y - 1][x + 1] #Left to right - bottom up diagonal
            if (wordsFormed.count('MAS') + wordsFormed.count('SAM') == 2):
                total += 1
            
print(total)