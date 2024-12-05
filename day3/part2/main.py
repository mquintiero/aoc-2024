import re

file = open('day3/input.txt', 'r')
content = file.read()
sum = 0
mulEnabled = 1

pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
numbers = r"\d+,\d+"

result = re.findall(pattern, content)
for mul in result:
    if (mul == 'do()'):
        mulEnabled = 1
        continue
    if (mul == "don't()"):
        mulEnabled = 0
        continue
    presentNumbers = re.findall(numbers, mul)
    presentNumbers = re.split(",", presentNumbers[0])
    firstNumber = int(presentNumbers[0])
    secondNumber = int(presentNumbers[1])
    sum = sum + (firstNumber * secondNumber * mulEnabled)

print (sum)