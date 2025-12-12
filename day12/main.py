inp, blocks, regions = open("input.txt", "r").read().strip().split("\n\n"), [], []
[blocks.append(tuple([(i,j) for i,ls in enumerate(entry.split(":\n")[1].split("\n")) for j,v in enumerate(ls) if v == "#"])) if ":\n" in entry else [regions.append((tuple(map(int, region.split(": ")[0].split("x"))), tuple([int(x) for x in region.split(": ")[1].split(" ")]))) for region in entry.split("\n")] for entry in inp]

print(f"Part 1: {sum([x*y>=9*sum(z) for ((x,y), z) in regions])}")