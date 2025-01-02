from re import findall


def part1(lines):
    regs, instr = lines.split("\n\n")
    reg_a, reg_b, reg_c = [int(x) for x in findall(r"\d+", regs)]
    instr = [int(x) for x in findall(r"\d+", instr)]
    end_of_program = len(instr) - 1
    instr_pointer = 0
    pointer_increase = 2
    out = []

    def combo(operand):
        if operand in range(4):
            return operand
        elif operand == 4:
            return reg_a
        elif operand == 5:
            return reg_b
        elif operand == 6:
            return reg_c

    def op(opcode, operand):
        nonlocal reg_a
        nonlocal reg_b
        nonlocal reg_c
        nonlocal instr_pointer
        nonlocal out

        if opcode == 0:
            reg_a = reg_a // (2 ** combo(operand))
        elif opcode == 1:
            reg_b = reg_b ^ operand
        elif opcode == 2:
            reg_b = combo(operand) % 8
        elif opcode == 3:
            if reg_a != 0:
                instr_pointer = operand - 2
        elif opcode == 4:
            reg_b = reg_b ^ reg_c
        elif opcode == 5:
            out.append(str(combo(operand) % 8))
        elif opcode == 6:
            reg_b = reg_a // (2 ** combo(operand))
        elif opcode == 7:
            reg_c = reg_a // (2 ** combo(operand))
    while instr_pointer < end_of_program:
        opcode, operand = instr[instr_pointer], instr[instr_pointer+1]
        op(opcode, operand)
        instr_pointer += pointer_increase
    return ",".join(out)

def part2(lines):
    '''
    The program is a single loop, where each iteration divides A // 8
    The values of B, C and output are based on A
    '''

    reg_a, reg_b, reg_c, *instr = map(int, findall(r'\d+',lines))
    n = len(instr)

    def run(reg_a, reg_b, reg_c):
        i=0
        r=[]
        while i in range(len(instr)):
            combo = [0, 1, 2, 3, reg_a, reg_b, reg_c]
            opcode, operand = instr[i:i+2]

            match opcode:
                case 0: reg_a >>= combo[operand]
                case 1: reg_b ^= operand
                case 2: reg_b = combo[operand] & 7 # equivalent combo[operand] % 8
                case 3: i = operand - 2 if reg_a else i    
                case 4: reg_b ^= reg_c
                case 5: r = r + [combo[operand] & 7]
                case 6: reg_b = reg_a >> combo[operand]
                case 7: reg_c = reg_a >> combo[operand]
            i += 2
        return r

    reg_a = 0
    for i in reversed(range(n)):
        reg_a <<= 3
        while run(reg_a, reg_b, reg_c) != instr[i:]:
            reg_a += 1
                    
    return reg_a

def main():
    main_input = True
    part_two = True

    if not main_input:
        with open('example-input.txt') as f:
            lines = f.read().strip()
            print("---")
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))
    else:
        with open('input.txt') as f:
            lines = f.read().strip()
            print("---")
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()