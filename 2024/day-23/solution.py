from collections import defaultdict
import itertools


def part1(lines):
    network = defaultdict(list)
    for c in lines:
        c1, c2 = c.split("-")
        network[c1].append(c2)
        network[c2].append(c1)
    all_comp = itertools.combinations(network.keys(), 3)

    out = []
    for c1, c2, c3 in all_comp:
        if ((c1[0] == "t" or c2[0] == "t" or c3[0] == "t") and
            (c2 in network[c1] and c3 in network[c1]
            and c1 in network[c2] and c3 in network[c2]
            and c2 in network[c3] and c1 in network[c3])):
            out.append((c1, c2, c3))
    
    return len(out)

def part2(lines):
    network = defaultdict(list)
    edges = []
    for c in lines:
        c1, c2 = c.split("-")
        network[c1].append(c2)
        network[c2].append(c1)
        edges.append((c1, c2))
    
    best = []
    for c1, c2 in edges:
        current = [c1, c2]
        for edge in network[c1]:
            if all(edge in network[x] for x in current):
                current.append(edge)
                continue
        if len(current) > len(best):
            best = current
    best.sort()

    return ",".join(best)

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