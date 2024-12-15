import re
robots = []
with open('day14/input.txt', 'r') as file:
    for line in file:
        numbers = [int(d) for d in re.findall(r'-?\d+', line)]
        robots.append(numbers)

for i in range(100):
    for robot in robots:
        xPosition, yPosition, xSpeed, ySpeed = robot
        robot[0] = (xPosition + xSpeed) % 101
        robot[1] = (yPosition + ySpeed) % 103

quadrantCount = [0, 0, 0, 0]
for robot in robots:
    xPosition, yPosition, xSpeed, ySpeed = robot
    if(xPosition < 50 and yPosition < 51):
        quadrantCount[0] += 1
    if(xPosition > 50 and yPosition < 51):
        quadrantCount[1] += 1
    if(xPosition < 50 and yPosition > 51):
        quadrantCount[2] += 1
    if(xPosition > 50 and yPosition > 51):
        quadrantCount[3] += 1

safetyFactor = quadrantCount[0] * quadrantCount[1] * quadrantCount[2] * quadrantCount[3]
print(safetyFactor)