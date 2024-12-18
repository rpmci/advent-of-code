def calc_lowest_cost(ax,ay,bx,by,px,py):
    # Brute force
    cost_a = 3
    cost_b = 1
    for a_press in range(101):
        for b_press in range(101):
            x_pos = a_press * ax + b_press * bx
            y_pos = a_press * ay + b_press * by
            if x_pos == px and y_pos == py:
                return cost_a * a_press + cost_b * b_press
            elif x_pos > px or y_pos > py:
                break
    return False

def part1(lines):
    total_cost = 0

    for machine in lines.split('\n\n'):
        machine_lines = machine.split('\n')
        ax = int(machine_lines[0][machine_lines[0].index('X')+2:machine_lines[0].index(',')])
        ay = int(machine_lines[0][machine_lines[0].index('Y')+2:])
        bx = int(machine_lines[1][machine_lines[1].index('X')+2:machine_lines[1].index(',')])
        by = int(machine_lines[1][machine_lines[1].index('Y')+2:])
        px = int(machine_lines[2][machine_lines[2].index('X')+2:machine_lines[2].index(',')])
        py = int(machine_lines[2][machine_lines[2].index('Y')+2:])

        result = calc_lowest_cost(ax, ay, bx, by, px, py)
        if result:
            total_cost += result
    return total_cost

def lowest_cost(ax, ay, bx, by, px, py):
    '''
    System of linear equations
    1) a * ax + b * bx = px
    2) a * ay + b * by = py
    ---
    Isolate for a in 1)
    a = (px - b * bx) / ax
    ---
    Solve by substituting into 2)
    ((px - b * bx) / ax) * ay + b * by = py
    ---
    Isolate for b
    b = ax * py - ay * px / (ax * by - ay * bx)
    ---
    Sub value for b back into step 2
    a = (px - b * bx) / ax
    '''

    b, b_rem = divmod(ax * py - ay * px, ax * by - ay * bx)
    a, a_rem = divmod(px - b * bx, ax)
    
    if a_rem or b_rem:
        return 0
    return a*3 + b

def part2(lines):
    total_cost = 0
    # Same as part 1, but add 10000000000000 to the prize coordinates
    offset = 10000000000000

    for machine in lines.split('\n\n'):
        machine_lines = machine.split('\n')
        ax = int(machine_lines[0][machine_lines[0].index('X')+2:machine_lines[0].index(',')])
        ay = int(machine_lines[0][machine_lines[0].index('Y')+2:])
        bx = int(machine_lines[1][machine_lines[1].index('X')+2:machine_lines[1].index(',')])
        by = int(machine_lines[1][machine_lines[1].index('Y')+2:])
        px = offset + int(machine_lines[2][machine_lines[2].index('X')+2:machine_lines[2].index(',')])
        py = offset + int(machine_lines[2][machine_lines[2].index('Y')+2:])

        total_cost += lowest_cost(ax, ay, bx, by, px, py)
    return total_cost

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