import re
content = []
with open('day13/input.txt', 'r') as file:
    machine = []
    for line in file:
        if (line.rstrip("\n") == ''):
            content.append(machine)
            machine = []
        else:
            numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
            machine.extend(numbers)
    content.append(machine)


tokens = 0
for machine in content:
    a1, a2, b1, b2, x, y = machine
    bButtonCount = (y * a1 - x * a2) / (b2 * a1 - b1 * a2)
    aButtonCount = (x - bButtonCount * b1) / a1
    #print('{} {}'.format(aButtonCount, bButtonCount))
    if aButtonCount == int(aButtonCount) and bButtonCount == int(bButtonCount):
        tokens += bButtonCount + 3 * aButtonCount

print(tokens)