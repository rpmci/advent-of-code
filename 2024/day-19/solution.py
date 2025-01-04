from collections import defaultdict
from functools import cache

def part1(lines):
    lines = lines.split("\n\n")
    patterns = lines[1].split()
    towels = defaultdict(list)
    
    for t in lines[0].split(", "):
        towels[t[0]].append(t)

    @cache
    def can_make(p):
        results = []
        for chain in towels[p[0]]:
            if p == chain:
                return True
            elif p.startswith(chain):
                results.append(can_make(p[len(chain):]))
        return any(results)

    return sum([can_make(p) for p in patterns])
    
def part2(lines):
    lines = lines.split("\n\n")
    patterns = lines[1].split()
    towels = defaultdict(list)
    
    for t in lines[0].split(", "):
        towels[t[0]].append(t)

    @cache
    def can_make(p):
        results = []
        for chain in towels[p[0]]:
            if p == chain:
                results.append(True)
            elif p.startswith(chain):
                results.append(can_make(p[len(chain):]))
        return sum(results)

    return sum([can_make(p) for p in patterns])

def main():
    main_input = True
    part_two = True

    if not main_input:
        with open('example-input.txt') as f:
            lines = f.read()
            print("---")
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))
    else:
        with open('input.txt') as f:
            lines = f.read()
            print("---")
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()