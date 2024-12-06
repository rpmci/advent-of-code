def check_all_directions(x, y, lines):
    count = 0
    max_y = len(lines)
    max_x = len(lines[0])
    s = "XMAS"

    left = x >= 3
    right = x <= max_x - 4
    up = y >= 3
    down = y <= max_y - 4

    lst = []
    if right:
        lst.append(lines[y][x:x+4])
        if up:
            lst.append(lines[y][x] + lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3])
        if down:
            lst.append(lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3])
    if left:
        lst.append(lines[y][x] + lines[y][x-1] + lines[y][x-2] + lines[y][x-3])
        if up:
            lst.append(lines[y][x] + lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3])
        if down:
            lst.append(lines[y][x] + lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3])
    if up: 
        lst.append(lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x])
    if down:
        lst.append(lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x])

    return lst.count(s)

def check_part2(x, y, lines):
    count = 0
    max_y = len(lines)
    max_x = len(lines[0])
    s = "XMAS"

    lst = []
    lst.append(lines[y-1][x-1] + lines[y][x] + lines[y+1][x+1])
    lst.append(lines[y-1][x+1] + lines[y][x] + lines[y+1][x-1])
    
    return lst.count("MAS") + lst.count("SAM") == 2

def part1(lines):
    count = 0
    search = ["XMAS", "SAMX"]
    print("------")

    for y in range (len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "X":
                count += check_all_directions(x, y, lines)

    return count

def part2(lines):
    count = 0
    print("------")

    for y in range (1, len(lines)-1):
        for x in range(1, len(lines[0])-1):
            if lines[y][x] == "A":
                count += check_part2(x, y, lines)
    return count

def main():
    sample_input = True
    main_input = True
    part_two = True

    if sample_input:
        with open('example-input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Example Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Example Answer: {}".format(part2(lines)))

    if main_input:
        with open('input.txt') as f:
            lines = f.read().splitlines()
            print("Part 1 Answer: {}".format(part1(lines)))
            if part_two:
                print("Part 2 Answer: {}".format(part2(lines)))
        
if __name__ == "__main__":
    main()