inp = open("input.txt", "r").read().strip().split("\n")

def part1():
    dial = 50
    p1zeros = 0
    for inst in inp:
        dial = (dial+{"R":1,"L":-1}[inst[0]]*int(inst[1:])%100)%100
        p1zeros += dial == 0
    return p1zeros


def part2():
    dial = 50
    p2zeros = 0
    for inst in inp:
        new_dial = dial + {"R":1,"L":-1}[inst[0]]*((dist:=int(inst[1:]))%100)
        p2zeros += (new_dial < 1 and dial != 0 or new_dial >= 100 and inst[0]=="R") + dist//100
        dial = (new_dial) % 100
    return p2zeros

print(f"Part 1: {part1()}; Part 2: {part2()}")