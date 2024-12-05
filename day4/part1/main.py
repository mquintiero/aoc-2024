content = []
with open('day4/input.txt', 'r') as file:
    for line in file:
        content.append(line.rstrip("\n"))

print(content)

for line in content:
    print(len(line))