reports = []
safeCount = 0

with open('day2/input.txt', 'r') as file:
    for line in file:
        numbers = [int(s) for s in line.split() if s.isdigit()]
        reports.append(numbers)

def allIncreasing(report):
    res = True
    for i in range(len(report) - 1):
        res = res and report[i] < report[i+1]
    return res

def allDecreasing(report):
    res = True
    for i in range(len(report) - 1):
        res = res and report[i] > report[i+1]
    return res

def validDiffer(level1, level2):
    differ = abs(level1 - level2)
    return differ >= 1 and differ <= 3

def validDifferings(report):
    res = True
    for i in range(len(report) - 1):
        res = res and validDiffer(report[i], report[i+1])
    return res    

def isValidReport (report):
    return (allIncreasing(report) or allDecreasing(report)) and validDifferings(report)

for report in reports:
    if (isValidReport(report)):
        safeCount += 1
    else:
        for i in range(len(report)):
            tempReport = report.copy()
            tempReport.pop(i)
            if (isValidReport(tempReport)):
                safeCount += 1
                break

print(safeCount)