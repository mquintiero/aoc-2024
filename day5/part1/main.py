import re
content = []
sum = 0
numbersAfterPage = dict()
with open('day5/input.txt', 'r') as file:
    for line in file:
        content.append(line.rstrip("\n"))

splitIndex = content.index('')
orderRules = content[:splitIndex]
updates = content[splitIndex+1:]

for rule in orderRules:
    tempRule = rule.split("|")
    numbersAfterPage.setdefault(tempRule[0], [])
    numbersAfterPage[tempRule[0]].append(tempRule[1])


k = 0
for update in updates:
    correctPage = True
    pages = re.findall(r'\d+',update)
    for i in range(len(pages)):
        for j in range(len(pages)):
            if (i == j): continue
            if (i < j):
                if (pages[i] in numbersAfterPage[pages[j]]):
                    correctPage = False
    if (correctPage):
        sum = sum + int(pages[int(len(pages)/2)])
    print("Page: {} Correct: {}".format(k, correctPage))
    k += 1

print(sum)