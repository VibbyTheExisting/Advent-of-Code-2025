from collections import deque

inp = open("input.txt", "r").read()
cols = len(inp.split("\n")[0])+1

def part1(return_indices=False):
    queue = deque([inp.index("S")])
    total = 0
    seen = set()
    while queue:
        index = queue.popleft()
        if index in seen:
            continue
        seen.add(index)
        if index+cols>=len(inp):
            continue
        if inp[index] == "." or inp[index] == "S":
            queue.append(index+cols)
        else:
            total += 1
            queue.append(index+cols+1)
            queue.append(index+cols-1)
    return (total, seen) if return_indices else total

def part2():
    _, seen = part1(True)
    dependents = {}
    for index in sorted(seen, reverse=True):
        if inp[index] == "^":
            if index not in dependents:
                dependents[index]=tuple()
            i = index
            while i in seen:
                i-=cols
                if i+1 in seen:
                    dependents[i+1] = dependents.get(i+1, tuple()) + (index,)
                if i-1 in seen:
                    dependents[i-1] = dependents.get(i-1, tuple()) + (index,)
    values = {}
    for key in sorted(dependents, reverse=True):
        if len(dependents[key]) == 0:
            values[key] = 2
        elif len(dependents[key]) == 1:
            values[key] = 1+values[dependents[key][0]]
        else:
            values[key] = sum(values[x] for x in dependents[key])
    return max(values.values())


print(f"Part 1: {part1()}; Part 2: {part2()}")