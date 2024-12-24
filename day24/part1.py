from queue import Queue
import operator

ops = {
    "AND": operator.and_,
    "XOR": operator.xor,
    "OR": operator.or_,
}
wires = {}
pending = Queue()
f = open('day24/input.txt', 'r').read().splitlines()
split = f.index('')
for wire in f[:split]:
    wireName, value = wire.split(": ")
    wires[wireName] = int(value)

for operation in f[split+1:]:
    pending.put(operation)

while not pending.empty():
    operation = pending.get()
    #print(operation)
    first, instruction, second, _, output = operation.split()
    #print('{} {} {} {}'.format(first, instruction, second, output))
    if first in wires and second in wires:
        wires[output] = ops[instruction](wires[first], wires[second])
    else:
        pending.put(operation)


zs = [value for key, value in enumerate(wires.items()) if value[0].startswith('z')]
zs.sort(reverse=True)
binary = ''.join(str(x) for x in [value[1] for key, value in enumerate(zs)])
print(int(binary, 2))