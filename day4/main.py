inp, cols = (lambda y: ("".join(["#"*(c:=len(y[0]))]+y+["#"*c]), c))([f"#{x}#" for x in open("input.txt", "r").read().strip().split("\n")])

def part1(board): return len([i for i,v in enumerate(board) if v == "@" and len([1 for j in range(-1,2) for k in range(-1,2) if j|k!=0 and board[i+j*cols+k] == "@"]) < 4])

def part2(board):
    while (accessible := {i for i,v in enumerate(board) if v == "@" and len([1 for j in range(-1,2) for k in range(-1,2) if j|k!=0 and board[i+j*cols+k] == "@"]) < 4}): board = "".join(["x" if i in accessible else c for i,c in enumerate(board)])
    return board.count("x")

print(f"Part 1: {part1(inp)}; Part 2: {part2(inp)}")