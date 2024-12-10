def part1(lines):
    id = 0
    diskmap = []
    line = [int(x) for x in lines[0]]

    for i in range(len(line)):
        if i % 2 == 0:
            diskmap += [id]*line[i]
            id += 1
        else:
            diskmap += [None]*line[i]

    front = 0
    back = len(diskmap) - 1

    while(front<back):
        if diskmap[back] == None:
            back -= 1
        elif diskmap[front] != None:
            front += 1
        else:
            diskmap[front], diskmap[back] = diskmap[back], diskmap[front]
            back -= 1
            front += 1

    out = 0
    for i in range(len(diskmap)):
        if diskmap[i]:
            out += i * diskmap[i]
    return out

def print_diskmap(diskmap):
    out = ""
    for c in diskmap:
        if c != None:
            out += str(c)
        else:
            out += '.'
    print(out)

def part2(lines):
    id = 0
    line = [int(x) for x in lines[0]]
    spaces = {}
    diskmap = []

    for i in range(len(line)):
        if i % 2 == 0:
            diskmap += [id]*line[i]
            id += 1
        else:
            pos = len(diskmap)
            spaces[pos] = line[i] # spaces [Start of space] = length of space
            diskmap += [None]*line[i]

    back = len(diskmap) - 1
    id -= 1
    while(back>0 and id>0):
        if diskmap[back] == None or diskmap[back] != id:
            back -= 1
        else:
            file_pos = back
            file_size = 0

            while (diskmap[file_pos]!=None and diskmap[file_pos] == id):
                file_size += 1
                file_pos -= 1
            
            for front in sorted(spaces):
                if spaces[front] >= file_size and front<back:
                    # Keep track of where the spaces are
                    spaces[file_pos+1] = spaces[front]
                    if spaces[front] != file_size:
                        spaces[front+file_size] = spaces[front] - file_size
                    del spaces[front]
                    # Swap values
                    for i in range(file_size):
                        diskmap[front+i], diskmap[back-i] = diskmap[back-i], diskmap[front+i]
                    break
            back -= file_size
            id -= 1
    
    # print_diskmap(diskmap)
    out = 0
    for i in range(len(diskmap)):
        if diskmap[i]:
            out += i * diskmap[i]
    return out

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