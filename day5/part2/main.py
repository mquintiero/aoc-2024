import functools

sum = 0

with open("day5/input.txt") as f:
    ordering_rules, updates = f.read().split("\n\n")
    ordering_rules = [tuple(map(int, rule.split("|"))) for rule in ordering_rules.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

def compare(a, b):
    if (a, b) in ordering_rules: return -1
    elif (b, a) in ordering_rules: return 1
    else: return 0

for update in updates:
    new = sorted(update, key=functools.cmp_to_key(compare))
    if (new != update):
      sum += int(new[len(new) // 2])


print(sum)