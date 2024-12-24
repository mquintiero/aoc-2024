def evolveNumber(number):
    number = ((number * 64) ^ number) % 16777216
    number = (round(number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number

total = 0
with open('day22/input.txt', 'r') as file:
    for number in file:
        currentNumber = int(number)
        for i in range(2000):
            currentNumber = evolveNumber(currentNumber)
        total += currentNumber
    
print(total)