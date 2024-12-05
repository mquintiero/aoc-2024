import re
"Very inefficient solution but it works... Took around 6 minutes to print result"
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

for update in updates:
    correctPage = True
    pages = re.findall(r'\d+',update)
    i = 0
    while i < len(pages):
        j = 0
        while j < len(pages):
            if (i < j):
                if (pages[i] in numbersAfterPage[pages[j]]):
                    correctPage = False
                    pages.insert(j+1, pages[i])
                    pages.pop(i)
                    i = j = 0
                    continue
            j += 1
        i += 1
    if (not correctPage):
        sum = sum + int(pages[int(len(pages)/2)])


print(sum)