def part1(lines):
    first_list = []
    second_list = []

    for line in lines:
        nums = line.split()
        first_list.append(int(nums[0]))
        second_list.append(int(nums[1]))
    first_list.sort()
    second_list.sort()

    sum = 0
    for i in range(len(first_list)):
        sum += abs(first_list[i] - second_list[i])

    return sum

def part2(lines):
    first_list = []
    second_list = []

    for line in lines:
        nums = line.split()
        first_list.append(int(nums[0]))
        second_list.append(int(nums[1]))
    
    sum = 0
    for n in first_list:
        sum += n * second_list.count(n)
    
    return sum

def main():
    sample_input = True
    second_part = True
    main_input = True

    if sample_input:
        with open('example-input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if second_part:
                print("Part 2 Example Answer: {}".format(part2(lines)))

    if main_input:
        with open('input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Answer: {}".format(part1(lines)))
            if second_part:
                print("Part 2 Answer: {}".format(part2(lines)))

        
if __name__ == "__main__":
    main()