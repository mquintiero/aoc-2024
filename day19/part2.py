content = open('day19/input.txt', 'r').read().splitlines()
towels = content[0].split(', ')
designs = content[2:]

memo = {'': 1}

def countWays(design, towels):
    if design in memo:
        return memo[design]
    else:
        count = sum(countWays(design[len(towel):], towels) for towel in towels if design.startswith(towel))
        memo[design] = count
        return count

towelsSum = 0
for design in designs:
    towelsSum += countWays(design, towels)

print(towelsSum)