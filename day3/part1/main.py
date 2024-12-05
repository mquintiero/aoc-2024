import re

file = open('day3/input.txt', 'r')
content = file.read()
sum = 0

pattern = r"mul\(\d+,\d+\)"
numbers = r"\d+,\d+"

result = re.findall(pattern, content)

for mul in result:
    presentNumbers = re.findall(numbers, mul)
    presentNumbers = re.split(",", presentNumbers[0])
    firstNumber = int(presentNumbers[0])
    secondNumber = int(presentNumbers[1])
    sum = sum + (firstNumber * secondNumber)

print (sum)