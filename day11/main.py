from functools import cache

outputs = {}
for line in open("input.txt", "r").read().strip().split("\n"):
    key, vals = line.split(": ")
    outputs[key] = vals.split(" ")

def part1():
    return get_paths("you", "out")

@cache
def get_paths(start, end):
    return start == end or sum(get_paths(x, end) for x in outputs.get(start, []))

def part2():
    return get_paths("svr", "dac")*get_paths("dac", "fft")*get_paths("fft", "out") + get_paths("svr", "fft")*get_paths("fft", "dac")*get_paths("dac", "out")

print(f"Part 1: {part1()}; Part 2: {part2()}")