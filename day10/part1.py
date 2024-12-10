with open('day10/input.txt', 'r') as f:
    lines = f.read().splitlines()

grid = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[x + y * 1j] = int(char)

trailheads = [key for key, value in grid.items() if value == 0]

score = 0
for trailhead in trailheads:
    queue = [trailhead]
    encountered_positions = set()
    while len(queue) > 0:
        position = queue.pop()
        if position in encountered_positions:
            continue
        elevation = grid[position]
        encountered_positions.add(position)
        if (elevation == 9):
            score += 1
            continue
        surrounding_positions = [position + direction for direction in [1, -1, 1j, -1j] 
                                if position + direction in grid and grid[position + direction] == elevation + 1]
        queue.extend(surrounding_positions)

print(score)