from collections import defaultdict

def rotate(dir):
    if dir == (0, -1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, -1)

def distinct_positions(lines):
    height = len(lines)
    width = len(lines[0])

    obstacles = []
    visited = set()

    for y in range(height):
        for x in range(width):
            if lines[y][x] == "^":
                guard_x = x
                guard_y = y
    
    x_move = 0
    y_move = -1

    while(0 <= guard_x < width and 0 <= guard_y < height):
        visited.add((guard_x, guard_y))

        next_x = guard_x + x_move
        next_y = guard_y + y_move

        if (0 <= next_x < width and 0 <= next_y < height) and lines[next_y][next_x] == "#":
            x_move, y_move = rotate((x_move, y_move))
        else:
            guard_x = next_x
            guard_y = next_y
    return visited

def part1(lines):
    return len(distinct_positions(lines))

def part2(lines):
    '''
    Loop detection:
    Instead of tracking just the positions the guard has walked, we are also
    noting which direction. If the guard walks on the same spot in the same 
    direction as before, then we know it's a loop.

    Which obstacle positions to test:
    We only test obstacles that would be in the guard's normal path.
    If an obstacle were placed elsewhere, the guard would never encounter it.
    '''
    height = len(lines)
    width = len(lines[0])
    obstacles = []
    for y in range(height):
        for x in range(width):
            if lines[y][x] == "^":
                start_pos = (x, y)
            elif lines[y][x] == "#":
                obstacles.append((x, y))
    
    original_path = distinct_positions(lines)
    count = 0
    
    for obstacle_pos in original_path:
        obstacles.append(obstacle_pos)
        visited = defaultdict(list)
        guard_pos = start_pos
        dir = (0, -1)

        while(0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height):
            if dir in visited[guard_pos]:
                count += 1
                break
            else:
                visited[guard_pos].append(dir)

            next_pos = (guard_pos[0] + dir[0], guard_pos[1] + dir[1])

            if (0 <= next_pos[0] < width and 0 <= next_pos[1] < height) and next_pos in obstacles:
                dir = rotate((dir[0], dir[1]))
            else:
                guard_pos = next_pos
        
        obstacles.remove(obstacle_pos)
    return count

def main():
    sample_input = False
    main_input = True
    part_two = True

    if sample_input:
        with open('example-input.txt') as f:
            lines = f.read().splitlines()
            print("---")
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))

    if main_input:
        with open('input.txt') as f:
            lines = f.read().splitlines()
            print("---")
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()