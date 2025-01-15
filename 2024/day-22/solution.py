from collections import defaultdict
from functools import cache
import itertools
import numpy as np

import time

start_time = time.time()

@cache
def evolve(n):
    new_n = n * 64
    n = prune_mix(n, new_n)
    new_n = n // 32
    n = prune_mix(n, new_n)
    new_n = n * 2048
    n = prune_mix(n, new_n)
    return n

@cache
def prune_mix(n, new_n):
    new_n ^= n
    new_n %= 16777216
    return new_n

def part1(lines):
    sum = 0
    for secret_number in lines:
        secret_number = int(secret_number)
        for i in range(2000):
            secret_number = evolve(secret_number)
        sum += secret_number
    return sum

def sliding_window(prices, changes):
    out = defaultdict(int)
    for i in range(len(changes)-4):
        d = tuple(changes[i:i+4])
        if not out[d]:
            out[d] = prices[i+4]
    return out

def part2(lines):
    all_changes = []
    for n in lines:
        n = int(n)
        prices = [n % 10]

        for i in range(2000):
            n = evolve(n)
            prices.append(n % 10)
        diff_dict = sliding_window(prices, np.diff(prices))
        all_changes.append(diff_dict)

    x = []
    for c in all_changes:
        x += list(c.keys())
    x = set(x)

    return max((sum(changes[d] for changes in all_changes) for d in x))

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
    print("--- %s seconds ---" % (time.time() - start_time))
        
if __name__ == "__main__":
    main()