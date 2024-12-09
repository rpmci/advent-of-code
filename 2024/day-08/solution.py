from collections import defaultdict 
from itertools import combinations

def calc_antinode(pair):
    p1 = pair[0]
    p2 = pair[1]

    dif = (p2[0] - p1[0], p2[1] - p1[1])

    return [(p1[0] - dif[0], p1[1] - dif[1]), (p2[0] + dif[0], p2[1] + dif[1])]

def part1(lines):
    height = len(lines)
    width = len(lines[0])

    antennas = defaultdict(list)
    for y in range(height):
        for x in range(width):
            c = lines[y][x]
            if c != '.':
                antennas[c].append((x,y))

    antinodes = set()

    for freq in antennas:
        pairs = combinations(antennas[freq], 2)
        
        for pair in pairs:
            for coord in calc_antinode(pair):
                if 0 <= coord[0] < width and 0 <= coord[1] < height:
                    antinodes.add(coord)
    return len(antinodes)

def calc_line(pair, width, height):
    p1 = pair[0]
    p2 = pair[1]

    out = []
    out.append(pair[0])
    out.append(pair[1])

    dif = (p2[0] - p1[0], p2[1] - p1[1])
    new_x = p1[0] - dif[0]
    new_y = p1[1] - dif[1]
    while 0 <= new_x < width and 0 <= new_y < height:
        out.append((new_x, new_y))
        new_x -= dif[0]
        new_y -= dif[1]

    new_x = p2[0] + dif[0]
    new_y = p2[1] + dif[1]
    while 0 <= new_x < width and 0 <= new_y < height:
        out.append((new_x, new_y))
        new_x += dif[0]
        new_y += dif[1]

    return set(out)

def part2(lines):
    height = len(lines)
    width = len(lines[0])

    antennas = defaultdict(list)
    for y in range(height):
        for x in range(width):
            c = lines[y][x]
            if c != '.':
                antennas[c].append((x,y))

    antinodes = set()

    for freq in antennas:
        pairs = combinations(antennas[freq], 2)
        
        for pair in pairs:
            antinodes.update(calc_line(pair, width, height))
    return len(antinodes)

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