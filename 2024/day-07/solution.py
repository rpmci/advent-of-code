import operator
from itertools import product

def part1(lines):
    all_ops = [operator.add, operator.mul]
    total = 0

    for line in lines:
        line = line.split()
        goal = int(line[0][:-1])
        nums = [int(x) for x in line[1:]]

        # Create the possible combinations of operators for the given numbers
        op_combinations = product(all_ops, repeat=len(nums) - 1)
        
        for ops in op_combinations:
            result = nums[0]

            '''
            Zip() is used for parallel iteration
            eg zip([2,3], [add, mul]) produces ((2,add), (3,mul))
            '''
            for num, op in zip(nums[1:], ops):
                result = op(result, num)
            if result == goal:
                total += goal
                break
    return total

def concat(num1, num2):
    return int(str(num1)+str(num2))

def part2(lines):
    all_ops = [operator.add, operator.mul, concat]
    total = 0

    for line in lines:
        line = line.split()
        goal = int(line[0][:-1])
        nums = [int(x) for x in line[1:]]

        # Create the possible combinations of operators for the given numbers
        op_combinations = product(all_ops, repeat=len(nums) - 1)
        
        for ops in op_combinations:
            result = nums[0]

            '''
            Zip() is used for parallel iteration
            eg zip([2,3], [add, mul]) produces ((2,add), (3,mul))
            '''
            for num, op in zip(nums[1:], ops):
                result = op(result, num)
            if result == goal:
                total += goal
                break
    return total

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