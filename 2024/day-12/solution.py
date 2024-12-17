from collections import defaultdict
import itertools
from operator import itemgetter


def check_plot(x, y):
    dirs = [(-1,0), (0,-1), (1,0), (0,1)]
    area, perimeter = 1, 0
    checked[y][x] = True

    for d in dirs:
        next_x = x+d[0]
        next_y = y+d[1]

        if (not (0 <= next_x < w and 0 <= next_y < h)
            or lines[next_y][next_x] != lines[y][x]):
            # if spot is out of bounds or a different letter
            perimeter += 1
        elif not checked[next_y][next_x]:
            result = check_plot(next_x, next_y)
            area += result[0]
            perimeter += result[1]

    return (area, perimeter)

def part1(lines):
    global h
    global w
    global checked

    h = len(lines)
    w = len(lines[0])
    checked = [[False for x in range(w)] for y in range(h)]
    total = 0

    for y in range(h):
        for x in range(w):
            if not checked[y][x]:
                area, perimeter = check_plot(x,y)
                total += area * perimeter

    return total

def find_connected_region(x, y):
    region = [(x, y)]
    sides = defaultdict(list)
    checked[y][x] = True

    up = (0,-1)
    down = (0,1)
    left = (-1,0)
    right = (1,0)
    dirs = [up, down, left, right]

    for d in dirs:
        next_x = x+d[0]
        next_y = y+d[1]
        
        if (not (0 <= next_x < w and 0 <= next_y < h)
            or lines[next_y][next_x] != lines[y][x]):
            sides[d].append((x,y))
        elif not checked[next_y][next_x]:
            result = find_connected_region(next_x, next_y)
            region += result[0]

            for dir in dirs:
                sides[dir] += result[1][dir]

    return (region, sides)

def find_distinct_sides(sides):
    up = (0,-1)
    down = (0,1)
    left = (-1,0)
    right = (1,0)
    dirs = [up, down, left, right]

    count = 0

    for d in dirs:
        if d in [left, right]:
            pos = 0
            diff = 1
        else: 
            pos = 1
            diff = 0

        d_count = len(sides[d])
        for pair in itertools.combinations(sides[d], 2):
            side = pair[0]
            other_side = pair[1]
            if abs(other_side[diff] - side[diff]) == 1 and other_side[pos] == side[pos]:
                d_count -=1
        count += d_count

    return count

def part2(lines):
    global checked
    checked = [[False for x in range(w)] for y in range(h)]

    total = 0

    for y in range(h):
        for x in range(w):
            if not checked[y][x]:
                region, sides = find_connected_region(x,y)
                n_sides = find_distinct_sides(sides) 
                
                total += len(region) * n_sides
    return total

def main():
    main_input = True
    part_two = True
    global lines

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