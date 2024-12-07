import re

content = []
with open('day7/input.txt', 'r') as file:
    for line in file:
        numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
        content.append(numbers)

def possibleEquation(numbers, accumulated, index, total):
    if (index == len(numbers)):
        return accumulated == total
    
    resultAdding = possibleEquation(numbers, accumulated + numbers[index], index + 1, total)
    resultMult = possibleEquation(numbers, accumulated * numbers[index], index + 1, total)

    return (resultAdding or resultMult)


sum = 0
for equation in content:
    total = equation[0]
    firstNumber = equation[1]
    equation.pop(0)
    equation.pop(0)
    numbers = equation
    if (possibleEquation(numbers, firstNumber, 0, total)):
        sum += total

print(sum)