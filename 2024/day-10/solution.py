def print_grid(grid):
    outstr = ""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if type(grid[y][x]) == int:
                outstr += str(grid[y][x])
            else:
                outstr += str(len(grid[y][x]))
        outstr += "\n"
    print(outstr)
    return

def part1(lines):
    width = len(lines[0])
    height = len(lines)

    grid = []
    paths = [[set() for w in range(width)] for h in range(height)]

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    total_count = 0

    for y in range(height):
        row = []
        for x in range(width):
            row.append(int(lines[y][x]))
            if int(lines[y][x]) == 9:
                paths[y][x].add((x,y))
        grid.append(row)
    
    # print("---\nGrid:\n")
    # print_grid(grid)
    # print_grid(paths)

    for i in range(8, -1, -1):
        for y in range(height):
            for x in range(width):
                if grid[y][x] == i:
                    for d in directions:
                        neighbour_x = x + d[0]
                        neighbour_y = y + d[1]
                        if (0 <= neighbour_x < width and 0 <= neighbour_y < width
                            and grid[neighbour_y][neighbour_x]==i+1):
                            paths[y][x].update(paths[neighbour_y][neighbour_x])
                    if i == 0:
                        total_count += len(paths[y][x])
        # print_grid(paths)

    return total_count

def part2(lines):
    width = len(lines[0])
    height = len(lines)

    grid = []
    paths = [[[0, set()] for w in range(width)] for h in range(height)]

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    total_count = 0

    for y in range(height):
        row = []
        for x in range(width):
            row.append(int(lines[y][x]))
            if int(lines[y][x]) == 9:
                paths[y][x][1].add((x,y))
                paths[y][x][0] = 1
        grid.append(row)

    for i in range(8, -1, -1):
        for y in range(height):
            for x in range(width):
                if grid[y][x] == i:
                    for d in directions:
                        neighbour_x = x + d[0]
                        neighbour_y = y + d[1]
                        if (0 <= neighbour_x < width and 0 <= neighbour_y < width
                            and grid[neighbour_y][neighbour_x]==i+1):
                            paths[y][x][0] += paths[neighbour_y][neighbour_x][0]
                            paths[y][x][1].update(paths[neighbour_y][neighbour_x][1])

                    if i == 0:
                        total_count += paths[y][x][0]

    return total_count

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