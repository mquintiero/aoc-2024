import re
from fractions import Fraction

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
    content.append(machine) # Agrego el ultimo manualmente porque no va a haber un salto de linea final

tokens = 0
for machine in content:
    a1, a2, b1, b2, x, y = machine
    x = x + 10000000000000
    y = y + 10000000000000
    bButtonCount = Fraction(y * a1 - x * a2, b2 * a1 - b1 * a2)
    aButtonCount = Fraction(x - bButtonCount * b1, a1)
    if aButtonCount == int(aButtonCount) and bButtonCount == int(bButtonCount):
        tokens += bButtonCount + 3 * aButtonCount

print(tokens)