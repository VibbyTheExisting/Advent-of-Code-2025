from shapely.geometry import Polygon

blocks = Polygon((inp := tuple(map(lambda x: [int(q) for q in x.split(",")], open("input.txt", "r").read().strip().split("\n")))))

def part1():
    return max([(abs(x1-x2)+1)*(abs(y1-y2)+1) for i,(x1,y1) in enumerate(inp) for (x2,y2) in inp[i+1:]])

def part2():
    return max((abs(x1-x2)+1)*(abs(y1-y2)+1) for i,(x1,y1) in enumerate(inp) for (x2,y2) in inp[i+1:] if blocks.contains(Polygon(((x1,y1),(x1,y2),(x2,y2),(x2,y1)))))

print(f"Part 1: {part1()}; Part 2: {part2()}")