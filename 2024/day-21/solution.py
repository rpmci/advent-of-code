import itertools
import numpy as np

from functools import cache
from itertools import pairwise

# Reference: https://www.reddit.com/r/adventofcode/comments/1hj2odw/2024_day_21_solutions/m4ui1sy/

dpad = ("X^A","<v>")
numpad = ("789", "456", "123", "X0A")

def walk(x, y, dir, pad):
    directions = {
        "^": (0, -1),
        "v": (0, 1),
        ">": (1, 0),
        "<": (-1, 0)
    }

    for d in dir:
        dx, dy = directions[d]
        x += dx
        y += dy
        yield pad[y][x]


def paths_between(pad, start, end):
    x1, y1 = next((x, y) for y, row in enumerate(pad)
                         for x, key in enumerate(row) if key == start)
    x2, y2 = next((x, y) for y, row in enumerate(pad)
                         for x, key in enumerate(row) if key == end)

    up = y1 - y2
    left = x1 - x2
    up_seq = up*"^" if up > 0 else abs(up)*"v"
    left_seq = left*"<" if left > 0 else abs(left)*">"

    paths = {"".join(p) for p in itertools.permutations(left_seq + up_seq)}
    return tuple(path + 'A' for path in paths
                 if "X" not in walk(x1, y1, path, pad))

@cache
def cost_between(pad, start, end, depth):
    return min(cost(dpad, path, depth - 1)
            for path in paths_between(pad, start, end)) if depth else 1

@cache
def cost(pad, code, depth):
    return sum(cost_between(pad, a, b, depth) for a,b in pairwise("A" + code))

def part1(lines):
    return sum(cost(numpad, code, 3) * int(code[:-1]) for code in lines)

def part2(lines):
    return sum(cost(numpad, code, 26) * int(code[:-1]) for code in lines)

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