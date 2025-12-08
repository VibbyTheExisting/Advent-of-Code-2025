inp = [tuple(map(int, (line.split(",")))) for line in open("input.txt", "r").read().strip().split("\n")]

distances = {}
for i,v in enumerate(inp):
    for i2 in range(i+1, len(inp)):
        distances[(i, i2)] = sum((x1-x2)**2 for (x1,x2) in zip(v,inp[i2]))

ordered_indices = sorted(distances, key=lambda x: distances[x])

def part1():
    connections = {i: {i} for i,v in enumerate(inp)}
    for i in range(1000):
        index1, index2 = ordered_indices[i]
        if index2 in connections[index1]:
            continue
        connections[index1].update(connections[index2])
        connections[index1].add(index2)
        for i in connections[index1]:
            for i2 in connections[index1]:
                connections[i].add(i2)

    circuits = []
    while connections:
        index, connects = connections.popitem()
        circuits.append(connects)
        for x in connects:
            if x != index:
                connections.pop(x)

    s = sorted(circuits, key=lambda v: len(v), reverse=True)
    return len(s[0])*len(s[1])*len(s[2])

def part2():
    last_connect = None
    connections = {i: {i} for i,v in enumerate(inp)}
    for index1, index2 in ordered_indices:
        if len(connections[0]) == 1000:
            return inp[last_connect[0]][0]*inp[last_connect[1]][0]
        if index2 in connections[index1]:
            continue
        last_connect = (index1, index2)
        connections[index1].update(connections[index2])
        connections[index1].add(index2)
        for i in connections[index1]:
            for i2 in connections[index1]:
                connections[i].add(i2)

print(f"Part 1: {part1()}; Part 2: {part2()}")