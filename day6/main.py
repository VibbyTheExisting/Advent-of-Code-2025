inp = open("input.txt", "r").read().strip().split("\n")
nums, ops = (lambda ls: ([[line[i] for line in ls[:-1]] for i,v in enumerate(ls[0])], ls[-1]))([x.split() for x in inp])

def part1(): return sum([eval(op.join(n)) for op,n in zip(ops, nums)])

def part2():
    total, digs = 0, []
    for i,v in enumerate(inp[0]):
        if (val := "".join([line[i] for line in inp[:-1] if line[i].strip()])): digs.append(val)
        elif digs: total, digs = total + eval(ops.pop(0).join(digs)), []
    return total + eval(ops[0].join(digs))

print(f"Part 1: {part1()}; Part 2: {part2()}")