ranges, nums = (lambda x: ([(int(z.split("-")[0]), int(z.split("-")[1])) for z in x[0].split("\n")], [int(n) for n in x[1].split("\n")]))(open("input.txt", "r").read().strip().split("\n\n"))

def part1(): return len([1 for n in nums if any([a<=n<=b for (a,b) in ranges])])

def unoverlap(range_set):
    new_ranges = set()
    for (a,b) in range_set:
        low, high = a-1, b-1
        while (low != a or high != b):
            low, high = a, b
            for (a2,b2) in range_set: a, b = (min(a, a2), max(b, b2)) if a<=a2<=b or a2<=a<=b2 or a<=b2<=b or a2<=b<=b2 else (a,b)
        new_ranges.add((low, high))
    return new_ranges


def part2(): return sum([(b+1-a) for (a,b) in unoverlap(ranges)])

print(f"Part 1: {part1()}; Part 2: {part2()}")