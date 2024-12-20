from queue import Queue

grid = {i+j*1j: c for i,r in enumerate(open('day20/input.txt'))
                  for j,c in enumerate(r) if c != '#' and c != '\n'}

start, = (p for p in grid if grid[p] in 'S')
end, = (p for p in grid if grid[p] in 'E')

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
for position, distance in dist.items():
    for cheatMovement in [2, -2, 2j, -2j]:
        newPosition = position + cheatMovement
        if newPosition in grid:
            savedPSeconds = dist[newPosition] - distance - 2
            if savedPSeconds >= 100:
                cheatCount += 1

print(cheatCount)