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
print(flowerRegions)
def edges(region):
    edgesCount = 0
    for position in region:
        # Outer corners
        edgesCount += position - 1 not in region and position - 1j not in region
        edgesCount += position + 1 not in region and position - 1j not in region
        edgesCount += position - 1 not in region and position + 1j not in region
        edgesCount += position + 1 not in region and position + 1j not in region
        # Inner corners
        edgesCount += position - 1 in region and position - 1j in region and position - 1 - 1j not in region
        edgesCount += position + 1 in region and position - 1j in region and position + 1 - 1j not in region
        edgesCount += position - 1 in region and position + 1j in region and position - 1 + 1j not in region
        edgesCount += position + 1 in region and position + 1j in region and position + 1 + 1j not in region

    return edgesCount

print(sum(len(region) * edges(region) for region in flowerRegions))