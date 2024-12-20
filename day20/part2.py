from queue import Queue
from itertools import combinations

grid = {i+j*1j: c for i,r in enumerate(open('day20/input.txt'))
                  for j,c in enumerate(r) if c != '#' and c != '\n'}

start, = (p for p in grid if grid[p] in 'S')

dist = {start: 0}
todo = Queue()  
todo.put(start)

while not todo.empty():
    pos = todo.get()
    for dir in [1, -1, 1j, -1j]:
        new = pos + dir
        if new in grid and new not in dist:
            todo.put(new)
            dist[new] = dist[pos] + 1

cheatCount = 0
for (position1, distance1), (position2, distance2) in combinations(dist.items(), 2):
    d = abs(position1.real - position2.real) + abs(position1.imag - position2.imag)
    if d < 21:
        savedPSeconds = distance2 - distance1 - d
        if savedPSeconds >= 100:
            cheatCount += 1

print(cheatCount)