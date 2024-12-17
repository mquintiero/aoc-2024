import re

content = []
with open('day17/input.txt', 'r') as file:
    for line in file:
        content.append((line.rstrip("\n")))

numbers = [int(s) for line in content for s in re.findall(r'\b\d+\b', line)]
a, b, c, instructions = numbers[0], numbers[1], numbers[2], numbers[3:]
ip = 0
output = []

def valueFor(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c

while ip < len(instructions):
    instruction = instructions[ip]
    ip += 1
    literalOperand = instructions[ip]
    comboOperand = valueFor(literalOperand)
    ip += 1
    match instruction:
        case 0: #adv -> division
            a = a // 2**comboOperand
        case 1: #bxl -> bitwise XOR
            b = b ^ literalOperand
        case 2: #bst -> modulo 8
            b = comboOperand % 8
        case 3: #jnz -> jump
            if a != 0: ip = literalOperand 
        case 4: #bxc -> bitwise XOR
            b = b ^ c
        case 5: #out -> output
            output.append(comboOperand % 8)
        case 6: #bdv -> division
            b = a // 2**comboOperand
        case 7: #cdv -> division
            c = a // 2**comboOperand

print(','.join(str(n) for n in output))
