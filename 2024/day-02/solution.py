def is_ascending(lst):
    lst_copy = lst[:]
    lst_copy.sort()

    if lst_copy == lst:
        return True
    
    lst_copy.reverse()
    if lst_copy == lst:
        return True

    return False

def is_safe_gap(lst):
    for i in range(len(lst) - 1):
        if not (1 <= abs(lst[i] - lst[i+1]) <= 3):
            return False
    return True

def part1(lines):
    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))

        if is_ascending(levels) and is_safe_gap(levels):
            safe_count += 1
    return safe_count

def part2(lines):
    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))

        # Generate all versions of the list after removing a single element
        removed = [levels[:i] + levels[i+1:] for i in range(len(levels))]

        for lst in removed:
            if is_ascending(lst) and is_safe_gap(lst):
                safe_count += 1
                break

    return safe_count

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