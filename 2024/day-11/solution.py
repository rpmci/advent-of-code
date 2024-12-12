from collections import defaultdict

rule_memo = dict()

def rule(stone):
    if stone == 0:
        output = [1]
    elif (len(str(stone)) % 2 == 0):
        half = len(str(stone))//2
        r1 = int(str(stone)[:half])
        r2 = int(str(stone)[half:])
        output = [r1, r2]
    else:
        output = [stone * 2024]
    return output

def part1(lines):
    stones = [int(x) for x in lines[0].split()]
    blinks = 25

    for n in range(blinks):
        new_stones = []
        n_zeros = 0
        for stone in stones:
            new_stones += rule(stone)
        stones = new_stones[:]
        
    return len(stones)

def rule2(stone):
    if stone in rule_memo.keys():
        output = rule_memo[stone]
    else:
        if stone == 0:
            output = [1]
        elif (len(str(stone)) % 2 == 0):
            half = len(str(stone))//2
            r1 = int(str(stone)[:half])
            r2 = int(str(stone)[half:])
            output = [r1, r2]
        else:
            output = [stone * 2024]
        rule_memo[stone] = output
    return output

def part2(lines):
    blinks = 75
    stones = defaultdict(int)
    for x in lines[0].split():
        stones[int(x)] += 1

    for n in range(blinks):
        new_stones = defaultdict(int)
        for stone in stones:
            for result in rule2(stone):

                new_stones[result] += stones[stone]
        stones = new_stones.copy()
        
    return sum(stones.values())

def main():
    main_input = True
    part_two = True

    if not main_input:
        with open('example-input.txt') as f:
            lines = f.read().splitlines()
            print("---")
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))
    else:
        with open('input.txt') as f:
            lines = f.read().splitlines()
            print("---")
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()