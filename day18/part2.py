import re
from collections import defaultdict
from queue import Queue
import copy

start = 0 + 0j
end = 70 + 70j
grid = {}
for i in range(71):
    for j in range(71):
        grid[i + j * 1j] = 1

positions = []
with open('day18/input.txt', 'r') as file:
    for line in file:
        numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
        positions.append(numbers)

def validPos(position, grid):
    if position.real >= 0 and position.real < 71 and position.imag >= 0 and position.imag < 71:
        return grid[position] == 1
    else:
        return False

def exitPathLength(start, end, grid):
    visited = defaultdict(bool)
    dist = defaultdict(int)
    todo = Queue()
    todo.put(start)

    while not todo.empty():
        pos = todo.get()
        for dir in [1, -1, 1j, -1j]:
            new = pos + dir
            if new == end: return dist[pos] + 1
            if validPos(new, grid) and not visited[new]:
                todo.put(new)
                visited[new] = True
                dist[new] = dist[pos] + 1
    return 0

def binary_search(grid, low, high):
    if high >= low:
        mid = (high + low) // 2
        gridCopy = copy.deepcopy(grid)
        for i in range(mid):
            gridCopy[positions[i][0] + positions[i][1] * 1j] = 0
        if exitPathLength(start, end, gridCopy) == 0:
            return binary_search(grid, low, mid - 1)
        else:
            return binary_search(grid, mid + 1, high)
    else:
        return positions[high]

print(binary_search(grid, 0, len(positions) - 1))