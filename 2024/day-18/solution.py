from collections import defaultdict
import heapq
import math

def print_grid(grid):
    out = ""
    for row in grid:
        for cell in row:
            if cell == "O":
                out += "O"
            elif cell:
                out += "."
            else:
                out += "#"
        out += "\n"
    print(out)

def part1(lines):
    w, h = (71, 71) if main_input else (7,7)

    grid = [[True for cell in range(w)] for row in range(h)]
    distances = defaultdict(lambda:math.inf)
    num_bytes = 1024 if main_input else 12

    for n in range(num_bytes):
        line = lines[n]
        x,y = map(int, line.split(','))
        grid[y][x] = False
    # print_grid(grid)
    # example
    # grid coordinates from 0-6 (w h = 7)
    # Main from 0-70, w=71

    start = (0,0)
    exit = (70,70) if main_input else (6,6)
    distances[start] = 0
    priority_queue = [(0, start)]
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if node == exit:
            return dist
        if dist > distances[node]:
            continue

        dist += 1
        for d in dirs:
            x, y = node[0]+d[0], node[1]+d[1]
            if (0 <= x < w and 0 <= y < h 
                and grid[y][x]
                and dist < distances[(x, y)]):
                distances[(x,y)] = dist
                heapq.heappush(priority_queue, (dist, (x,y)))

    return distances[exit]

def part2(lines):
    def path_exists():
        distances = defaultdict(lambda:math.inf)
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            dist, node = heapq.heappop(priority_queue)
            if node == exit:
                return dist
            if dist > distances[node]:
                continue

            dist += 1
            for x,y in edges[node]:
                if (0 <= x < w and 0 <= y < h 
                    and grid[y][x]
                    and dist < distances[(x, y)]):
                    distances[(x,y)] = dist
                    heapq.heappush(priority_queue, (dist, (x,y)))

        return distances[exit] != math.inf

    w, h = (71, 71) if main_input else (7,7)
    grid = [[True for cell in range(w)] for row in range(h)]
    start = (0,0)
    exit = (70,70) if main_input else (6,6)
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    edges = defaultdict(list)

    for y in range(h):
        for x in range(w):
            for d in dirs:
                x2, y2 = x+d[0], y+d[1]
                if (0 <= x2 < w and 0 <= y2 < h):
                    edges[(x,y)].append((x2,y2))


    for line in lines:
        x,y = map(int, line.split(','))
        grid[y][x] = False

        for e in edges[(x,y)]:
            edges[e].remove((x,y))
        edges[(x,y)] = []

        if not path_exists():
            return((x,y))

    return 

def main():
    global main_input 
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