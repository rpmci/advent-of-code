from collections import defaultdict
import math


def part1(lines):
    w, h = len(lines[0]), len(lines)
    for y in range(h):
        for x in range(w):
            if lines[y][x] == "S":
                start = (x,y)
            elif lines[y][x] == "E":
                end = (x,y)

    scores = defaultdict(lambda:math.inf)
    scores[(x, y, 1, 0)] = 0

    current_positions = [(start[0], start[1], 1, 0, 0)] # start facing east
    while(current_positions):
        next_positions = []
        for x, y, dx, dy, score in current_positions:
            if lines[y+dy][x+dx] != "#":
                if score+1 < scores[(x+dx, y+dy, dx, dy)]:
                    next_positions.append((x+dx, y+dy, dx, dy, score+1))
                    scores[(x+dx, y+dy, dx, dy)] = score+1

            next_score = score+1000
            if dx == 1 or dx == -1:
                rotations = [(0, 1), (0, -1)]
            else:
                rotations = [(1, 0), (-1, 0)]

            for r_x, r_y in rotations:
                if next_score < scores[(x, y, r_x, r_y)]:
                    next_positions.append((x, y, r_x, r_y, next_score))
                    scores[(x, y, r_x, r_y)] = next_score
            
        current_positions = next_positions.copy()

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    end_score = min([scores[(end[0], end[1], dx, dy)] for dx, dy in directions])
    
    return end_score

def part2(lines):
    w, h = len(lines[0]), len(lines)
    for y in range(h):
        for x in range(w):
            if lines[y][x] == "S":
                start = (x,y)
            elif lines[y][x] == "E":
                end = (x,y)

    score_path = defaultdict(lambda:[math.inf, set()])
    starting_path = set()
    starting_path.add(start)
    score_path[(start[0], start[1], 1, 0)] = [0, starting_path]

    current_positions = [(start[0], start[1], 1, 0)] # start facing east
    while(current_positions):
        next_positions = []
        for x, y, dx, dy in current_positions:
            score, path = score_path[(x, y, dx, dy)]
            if lines[y+dy][x+dx] != "#":
                next_path = path.copy()
                next_path.add((x+dx, y+dy))
                if score+1 < score_path[(x+dx, y+dy, dx, dy)][0]:
                    next_positions.append((x+dx, y+dy, dx, dy))
                    score_path[(x+dx, y+dy, dx, dy)] = [score+1, next_path]
                elif score+1 == score_path[(x+dx, y+dy, dx, dy)][0]:
                    score_path[(x+dx, y+dy, dx, dy)][1].update(next_path)


            next_score = score+1000
            if dx == 1 or dx == -1:
                rotations = [(0, 1), (0, -1)]
            else:
                rotations = [(1, 0), (-1, 0)]
            
            for r_x, r_y in rotations:
                next_path = path.copy()
                if next_score < score_path[(x, y, r_x, r_y)][0]:
                    next_positions.append((x, y, r_x, r_y))
                    score_path[(x, y, r_x, r_y)] = [next_score, next_path]
                elif next_score == score_path[(x, y, r_x, r_y)][0]:
                    score_path[(x, y, r_x, r_y)][1].update(next_path)
            
        current_positions = next_positions.copy()

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    end_score = min([score_path[(end[0], end[1], dx, dy)][0] for dx, dy in directions])
    end_cells = set()
    for dx, dy in directions:
        if score_path[(end[0], end[1], dx, dy)][0] == end_score:
            end_cells.update(score_path[(end[0], end[1], dx, dy)][1])

    # out = ""
    # for y in range(h):
    #     for x in range(w):
    #         if (x,y) in end_cells:
    #             out += "O"
    #         else:
    #             out += lines[y][x]
    #     out += "\n"
    # print(out)
    
    return len(end_cells)

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