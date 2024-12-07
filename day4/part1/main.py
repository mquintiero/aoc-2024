#Credit to r/Betadam whom I copied the code because I was too lazy to implement it
file = open("day4/input.txt", "r")
line = []
wordsFormed = ['']*8
total = 0

for i in file:
    line.append('ZZZ' + i.strip() + 'ZZZ')

topAndBottomPadding = 'Z' * (len(line[0])+6)
    
for i in range(3):
    line.insert(0, topAndBottomPadding)
    line.append(topAndBottomPadding)

for y in range(len(line)):
    for x in range(len(line[y])):
        if line[y][x] == 'X':
            wordsFormed[0] = line[y][x:x+4] #Left to right
            wordsFormed[1] = line[y][x]+line[y+1][x+1]+line[y+2][x+2]+line[y+3][x+3] #Left to right - top to bottom diagonal
            wordsFormed[2] = line[y][x]+line[y+1][x]+line[y+2][x]+line[y+3][x] #Top to bottom
            wordsFormed[3] = line[y][x]+line[y+1][x-1]+line[y+2][x-2]+line[y+3][x-3] #Right to left - top to bottom diagonal
            wordsFormed[4] = line[y][x]+line[y][x-1]+line[y][x-2]+line[y][x-3] #Right to left
            wordsFormed[5] = line[y][x]+line[y-1][x-1]+line[y-2][x-2]+line[y-3][x-3] #Right to left - bottom up diagonal
            wordsFormed[6] = line[y][x]+line[y-1][x]+line[y-2][x]+line[y-3][x] #Bottom up
            wordsFormed[7] = line[y][x]+line[y-1][x+1]+line[y-2][x+2]+line[y-3][x+3] #Left to right - bottom up diagonal
            total += wordsFormed.count('XMAS')    
            
print(total)