import re

def part1(lines):
    total_sum = 0

    for line in lines:
        valid = re.findall("mul[(][0-9]+,[0-9]+[)]", line)
        for mul in valid:
            nums = [int(x) for x in mul[4:-1].split(',')]
            total_sum += nums[0] * nums[1]

    return total_sum

def part2(lines):
    total_sum = 0
    enabled = True

    for line in lines:
        valid = re.findall("mul[(][0-9]+,[0-9]+[)]|do(?:n't)?[(][)]", line)
        for mul in valid:
            if "don't" in mul:
                enabled = False
            elif "do" in mul:
                enabled = True
            elif enabled:
                nums = [int(x) for x in mul[4:-1].split(',')]
                total_sum += nums[0] * nums[1]

    return total_sum

def main():
    sample_input = True
    main_input = True
    part_two = True

    if sample_input:
        with open('example-input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))

    if main_input:
        with open('input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()