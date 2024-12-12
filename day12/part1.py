grid = {i+j*1j: c for i,r in enumerate(open('day12/input.txt'))
                  for j,c in enumerate(r.strip())}

flowerRegions = {position: {position} for position in grid}

for position in grid:
    for adjacent in position+1, position-1, position+1j, position-1j:
        if adjacent in grid and grid[position] == grid[adjacent]:
            flowerRegions[position] |= flowerRegions[adjacent]
            for x in flowerRegions[position]: 
                flowerRegions[x] = flowerRegions[position]

flowerRegions = {tuple(s) for s in flowerRegions.values()}

def edges(region):
    P = {(position,adjacentDirection) for position in region for adjacentDirection in (+1,-1,+1j,-1j) if position+adjacentDirection not in region}
    return P

print(sum(len(region) * len(edges(region)) for region in flowerRegions))