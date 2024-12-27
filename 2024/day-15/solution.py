def next_step(direction):
    if direction == "^":
        return 0, -1
    elif direction == "v":
        return 0, 1
    elif direction == "<":
        return -1, 0
    elif direction == ">":
        return 1, 0

def print_grid(grid):
    out = ""
    for row in grid:
        for cell in row:
            out += cell
        out += "\n"
    print(out)

def part1(lines):
    map, moves = lines.split("\n\n")
    map = map.split()
    moves = moves.replace("\n", "")

    h, w = len(map), len(map[0])

    grid = [[cell for cell in row] for row in map]

    for y in range(h):
        for x in range(w):
            if map[y][x] == "@":
                robot = [x,y]
    
    for m in moves:
        # print_grid(grid)
        dx, dy = next_step(m)
        n = 0
        x,y = robot
        next_space = grid[y+dy][x+dx]

        if next_space == "#":
            continue
        elif next_space == "O":
            while next_space == "O":
                n += 1
                next_space = grid[y+(n*dy)][x+(n*dx)]
                
            if next_space != "#":
                grid[robot[1]][robot[0]] = "."
                robot = [x+dx, y+dy]
                grid[robot[1]][robot[0]] = "@"
                grid[y+(n*dy)][x+(n*dx)] = "O"
        else:
            grid[robot[1]][robot[0]] = "."
            robot = [x+dx, y+dy]
            grid[robot[1]][robot[0]] = "@"
    
    total = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "O":
                total += 100 * y + x
    return total

def part2(lines):
    map, moves = lines.split("\n\n")
    map = map.split()
    moves = moves.replace("\n", "")

    h, w = len(map), len(map[0])

    grid = [["" for cell in range(2*w)] for row in range(h)]  

    for y in range(h):
        for x in range(w):
            if map[y][x] == "@":
                robot_position = [2*x,y]
                grid[y][2*x] = "@"
                grid[y][2*x+1] = "."
            elif map[y][x] == "O":
                grid[y][2*x] = "["
                grid[y][2*x+1] = "]"
            elif map[y][x] == "#":
                grid[y][2*x] = "#"
                grid[y][2*x+1] = "#"
            elif map[y][x] == ".":
                grid[y][2*x] = "."
                grid[y][2*x+1] = "."
    
    for m in moves:
        # print_grid(grid)
        dx, dy = next_step(m)
        n = 0
        x,y = robot_position
        next_x, next_y = x+dx, y+dy
        next_cell = grid[next_y][next_x]
        boxes_pushed = set()

        clear_old = set()
        clear_old.add((x,y))

        check = set()
        check.add((x,y))

        wall = False

        while(check and not wall):
            check_next = set()
            for cell in check:
                next_x, next_y = cell[0]+dx, cell[1]+dy
                next_cell = grid[cell[1]+dy][cell[0]+dx]
                if next_cell == "#":
                    wall = True
                    break
                elif next_cell == "[" or next_cell == "]":
                    if m == "^" or m == "v":
                        if next_cell == "[":
                            check_next.add((next_x+1, next_y)) # Add right side of box 
                        elif next_cell == "]":
                            check_next.add((next_x-1, next_y)) # Add left side of box
                    check_next.add((next_x, next_y))
                boxes_pushed.add(((cell[0]+dx, cell[1]+dy), grid[cell[1]][cell[0]]))
                clear_old.add((cell))
            check = check_next.copy()

        if not wall:
            for cell in clear_old:
                grid[cell[1]][cell[0]] = "."
            for box in boxes_pushed:
                cell_x, cell_y = box[0]
                char = box[1]
                grid[cell_y][cell_x] = char
            robot_position[0] += dx
            robot_position[1] += dy
    
    # print_grid(grid)
    total = 0
    for y in range(h):
        for x in range(2*w):
            if grid[y][x] == "[":
                total += 100 * y + x
    return total

def main():
    main_input = True
    part_two = True

    if not main_input:
        with open('example-input.txt') as f:
            lines = f.read().strip()
            print("---")
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))
    else:
        with open('input.txt') as f:
            lines = f.read().strip()
            print("---")
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()