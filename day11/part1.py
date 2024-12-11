import re
from collections import defaultdict

stones = []
f = open('day11/input.txt', 'r')
input = f.read()
stones = {int(s): 1 for s in re.findall(r'\b\d+\b', input)}

def splitStone(stone):
   return stone[:len(stone)//2], stone[len(stone)//2:]

def blink(stones):
    newStones = defaultdict(int)
    for stone, count in stones.items():
        if (stone == 0):
            newStones[1] += count
        elif (len(str(stone)) % 2 == 0):
            firstHalf, secondHalf = splitStone(str(stone))
            newStones[int(firstHalf)] += count
            newStones[int(secondHalf)] += count
        else:
            newStones[stone * 2024] += count
    return newStones

lastStones = stones.copy()
for k in range(25):
    lastStones = blink(lastStones)

print(sum(lastStones.values()))