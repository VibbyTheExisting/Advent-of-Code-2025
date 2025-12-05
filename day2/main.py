inp = tuple(map(lambda x: (int(x.split("-")[0]), int(x.split("-")[1])), open("input.txt", "r").read().strip().split(",")))

def part1(): sum([num for start, end in inp for num in range(start, end+1) if not len((snum := str(num)))%2 and snum[:len(snum)//2] == snum[len(snum)//2:]])
def part2(): sum([num for start, end in inp for num in range(start, end+1) if num>9 and (snum := str(num)) and any([all([snum[new_start:new_start+length] == snum[:length] for new_start in range(length, len(snum)+1-length, length)]) for length in range(len(set(snum)), len(snum)) if not (len(snum) % length)])])

print(f"Part 1: {part1()}; Part 2: {part2()}")