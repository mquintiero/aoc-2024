import re
from collections import defaultdict
from queue import Queue

grid = {}
for i in range(71):
    for j in range(71):
        grid[i + j * 1j] = 1

positions = []
with open('day18/input.txt', 'r') as file:
    for line in file:
        numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
        positions.append(numbers)

for i in range(1024):
    grid[positions[i][0] + positions[i][1] * 1j] = 0

def validPos(position):
    if position.real >= 0 and position.real < 71 and position.imag >= 0 and position.imag < 71:
        return grid[position] == 1
    else:
        return False

start = 0+0j

visited = defaultdict(bool)
dist = defaultdict(int)
todo = Queue()
todo.put(start)

while not todo.empty():
    pos = todo.get()
    for dir in [1, -1, 1j, -1j]:
        new = pos + dir
        if validPos(new) and not visited[new]:
            todo.put(new)
            visited[new] = True
            dist[new] = dist[pos] + 1

print(dist[70 + 70j])
