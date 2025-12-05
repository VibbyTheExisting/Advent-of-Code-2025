jolts = [[int(x) for x in line] for line in open("input.txt", "r").read().strip().split("\n")]

def part1(): return sum((max_val:=max(line[:-1]))*10+max(line[line.index(max_val)+1:]) for line in jolts)


def part2(): return sum((helper := lambda ls, digs_remaining: max(ls) if digs_remaining==1 else (max(ls[:-digs_remaining+1]))*10**(digs_remaining-1)+helper(ls[ls.index(max(ls[:-digs_remaining+1]))+1:], digs_remaining-1))(line, 12) for line in jolts)

print(f"Part 1: {part1()}; Part 2: {part2()}")

# One-Liner
# # print(f"Part 1: {sum(max(line[:-1])*10+max(line[line.index(max(line[:-1]))+1:]) for line in [[int(x) for x in line] for line in open("input.txt", "r").read().strip().split("\n")])}; Part 2: {sum((helper := lambda ls, digs_remaining: max(ls) if digs_remaining==1 else (max(ls[:-digs_remaining+1]))*10**(digs_remaining-1)+helper(ls[ls.index(max(ls[:-digs_remaining+1]))+1:], digs_remaining-1))(line, 12) for line in [[int(x) for x in line] for line in open("input.txt", "r").read().strip().split("\n")])}")

# Readable solution:

def helper(ls, digs_remaining=12):
    if digs_remaining==1:
        return max(ls)
    return (val:=max(ls[:-digs_remaining+1]))*10**(digs_remaining-1)+helper(ls[ls.index(val)+1:], digs_remaining-1)

def part2():
    return sum(helper(line) for line in jolts)