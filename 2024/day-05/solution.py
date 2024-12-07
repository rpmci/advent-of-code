from collections import defaultdict

def part1(lines):
    total = 0

    lines = lines.split("\n\n")
    rules = lines[0].splitlines()
    pages = lines[1].splitlines()

    rule_dict = defaultdict(list)

    for rule in rules:
        n1 = int(rule[:rule.index("|")])
        n2 = int(rule[rule.index("|")+1:])
        rule_dict[n1].append(n2)

    for page in pages:
        page_list = [int(x) for x in page.split(",")]
        printed_pages = defaultdict(bool)
        bad_order = False
        for p in page_list:
            printed_pages[p] = True
            if p in rule_dict and True in [printed_pages[x] for x in rule_dict[p]]:
                bad_order = True
                break
        if not bad_order:
            total += page_list[len(page_list)//2]
    return total

def is_valid_order(page_list, rule_dict):
    # Returns (bool, list)
    # If False, it swaps the position of the two pages that cause issue
    # By repeating this process, pages will eventually end up in a valid order

    printed_pages = defaultdict(bool)

    for p in page_list:
        printed_pages[p] = True
        if p in rule_dict:
            for x in rule_dict[p]:
                if printed_pages[x] == True: 
                    page_list[page_list.index(p)], page_list[page_list.index(x)] = x, p
                    return False, page_list

    return True, page_list


def part2(lines):
    total = 0
    lines = lines.split("\n\n")
    rules = lines[0].splitlines()
    pages = lines[1].splitlines()

    rule_dict = defaultdict(list)

    for rule in rules:
        n1 = int(rule[:rule.index("|")])
        n2 = int(rule[rule.index("|")+1:])
        rule_dict[n1].append(n2)

    for page in pages:
        page_list = [int(x) for x in page.split(",")]

        valid, page_list = is_valid_order(page_list, rule_dict)
        if not valid:
            while not valid:
                valid, page_list = is_valid_order(page_list, rule_dict)
            total += page_list[len(page_list)//2]

    return total

def main():
    sample_input = True
    main_input = True
    part_two = True

    if sample_input:
        with open('example-input.txt') as f:
            lines = f.read()
            print("---\nPart 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))

    if main_input:
        with open('input.txt') as f:
            lines = f.read()
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()