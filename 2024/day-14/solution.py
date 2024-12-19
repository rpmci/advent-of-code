import re

def part1(lines):
    robot_positions = []
    
    # sample = 11 wide, 7 tall
    # regular = 101 wide, 103 tall
    w = 101
    h = 103
    seconds = 100

    for line in lines:
        line = line.split()
        pos = line[0]
        v = line[1]

        px = int(pos[pos.index('=')+1:pos.index(',')])
        py = int(pos[pos.index(',')+1:])

        vx = int(v[v.index('=')+1:v.index(',')])
        vy = int(v[v.index(',')+1:])

        robot_positions.append(((px + seconds * vx) % w, (py + seconds * vy) % h))

    q1, q2, q3, q4 = 0, 0, 0, 0
    for r in robot_positions:
        if r[0] < w//2:
            if r[1] < h//2:
                q1 += 1
            elif r[1] > h//2:
                q2 += 1
        elif r[0] > w//2:
            if r[1] < h//2:
                q3 += 1
            elif r[1] > h//2:
                q4 += 1

    return q1 * q2 * q3 * q4


def part2(lines):
    ## Referencing https://www.reddit.com/r/adventofcode/comments/1hdvhvu/comment/m1z7h5g/
    w = 101
    h = 103

    robots = [[*map(int, re.findall(r'-?\d+',l))]
                   for l in lines]
    
    def calc_positions(t):
        q1 = q2 = q3 = q4 = 0
        w = 101
        h = 103

        for px, py, vx, vy in robots:
            x = (px + t * vx) % w
            y = (py + t * vy) % h
            if x < w//2:
                if y < h//2:
                    q1 += 1
                elif y > h//2:
                    q2 += 1
            elif x > w//2:
                if y < h//2:
                    q3 += 1
                elif y > h//2:
                    q4 += 1
        return q1 * q2 * q3 * q4
    
    # Looking for the timestamp with the lowest score, 
    # since robots are gathered around the middle
    return min(range(10_000), key=calc_positions)

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