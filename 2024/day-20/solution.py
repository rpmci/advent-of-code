from collections import defaultdict
import itertools
import math

def part1(lines):
    w, h = len(lines[0]), len(lines)
    for x,y in itertools.product(range(w), range(h)):
        if lines[y][x] == "S":
            start = (x,y)
        elif lines[y][x] == "E":
            end = (x,y)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    scores = defaultdict(lambda:math.inf)
    scores[end] = 0
    current = [end]
    while current:
        next = []
        for c in current:
            score = scores[c]
            for d in directions:
                n_x, n_y = c[0]+d[0], c[1]+d[1]
                if (0 <= n_x <= w and 0 <= n_y <= h
                    and lines[n_y][n_x] != "#"
                    and score+1 < scores[(n_x,n_y)]):
                    scores[(n_x,n_y)] = score+1
                    next.append((n_x,n_y))
        current = next.copy()

    base_score = scores[start]
    count = 0
    for x,y in itertools.product(range(w), range(h)):
        if lines[y][x] != "#":
            nearby = set([(x + (dx*n), y + (dy*(2-n))) for dx, dy in itertools.product([1, -1], repeat=2) for n in range(3)])
            for i in nearby:
                if (0 <= i[0] <= w and 0 <= i[1] <= h):
                    diff = scores[(x,y)] - scores[i] - 2
                    if diff >= 100:
                        count += 1
                        # print(f"({x},{y}) to {i}: save {scores[(x,y)]} - {scores[i]}")
    return count

def part2(lines):
    w, h = len(lines[0]), len(lines)
    for x,y in itertools.product(range(w), range(h)):
        if lines[y][x] == "S":
            start = (x,y)
        elif lines[y][x] == "E":
            end = (x,y)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]


    scores = defaultdict(lambda:math.inf)
    scores[end] = 0
    current = [end]
    while current:
        next = []
        for c in current:
            score = scores[c]
            for d in directions:
                n_x, n_y = c[0]+d[0], c[1]+d[1]
                if (0 <= n_x <= w and 0 <= n_y <= h
                    and lines[n_y][n_x] != "#"
                    and score+1 < scores[(n_x,n_y)]):
                    scores[(n_x,n_y)] = score+1
                    next.append((n_x,n_y))
        current = next.copy()

    base_score = scores[start]
    count = 0
    max_time = 20
    cheat = set()
    for t in range(1, max_time+1):
        for x,y in itertools.product(range(w), range(h)):
            if lines[y][x] != "#":
                nearby = set([(x + (dx*n), y + (dy*(t-n))) for dx, dy in itertools.product([1, -1], repeat=2) for n in range(t+1)])
                for i in nearby:
                    if (0 <= i[0] <= w and 0 <= i[1] <= h):
                        diff = scores[(x,y)] - scores[i] - t
                        if diff >= 100:
                            count += 1
                            cheat.add(((x,y), i))
                            # print(f"({x},{y}) to {i}: save {scores[(x,y)]} - {scores[i]}")
    return len(cheat)

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