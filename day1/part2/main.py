leftList = []
rightList = []
sum = 0

with open('day1/input.txt', 'r') as file:
    for line in file:
        numbers = [int(s) for s in line.split() if s.isdigit()]
        leftList.append(numbers[0])
        rightList.append(numbers[1])

for number in leftList:
    sum = sum + number * rightList.count(number)

print(sum)