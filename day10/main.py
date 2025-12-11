from collections import deque
from scipy.optimize import linprog
import numpy as np

inp = open("input.txt", "r").read().strip().split("\n")
machines = []
for line in inp:
    target = [x=="#" for x in line.split("]")[0][1:]]
    buttons = [eval(x) if "," in x else (eval(x),) for x in line.split("] ")[1].split(" {")[0].split(" ")]
    joltage = eval(line.split("{")[1][:-1])
    machines.append((target, buttons, joltage))

def part1():
    total = 0
    for (target, buttons, _) in machines:
        seen=set()
        queue = deque([([False]*len(target), 0)])
        while queue:
            state, presses = queue.pop()
            if (temp:=tuple(state)) in seen:
                continue
            seen.add(temp)
            if state == target:
                total += presses
                break
            for button in buttons:
                new_state = state.copy()
                for index in button:
                    new_state[index] = not new_state[index]
                queue.appendleft((new_state, presses+1))
    return total

def part2():
    total = 0
    for (_, buttons, joltage) in machines:
        optimizer_c = [1] * len(buttons)
        b = []
        for button in buttons:
            b.append([1 if i in button else 0 for i in range(len(joltage))])
        # breakpoint()
        total += linprog(c=optimizer_c, A_eq=np.array(b).T, b_eq=joltage, integrality=optimizer_c).fun
    return int(total)

print(f"Part 1: {part1()}; Part 2: {part2()}")

# def recur(vector, basis, count=100):
#     if min(vector) < 0:
#         return float("inf")
#     if count <= 0:
#         return sum(vector)
#     total = sum(vector)
#     for c in range(basis.cols):
#         v = basis.col(c)
#         total = min(total, recur(vector+v, basis, count-1))
#     return total

# def part2():
#     total = 0
#     temp = 0
#     for (_, buttons, joltage) in machines:
#         temp += 1
#         print(temp)
#         res = []
#         array = []
#         for i in range(len(joltage)):
#             res.append([joltage[i]])
#             row = []
#             for b in buttons:
#                 row.append(1 if i in b else 0)
#             row.append(joltage[i])
#             array.append(row)
#         matrix = Matrix(array)
#         array, pivot_cols = matrix.rref()
#         matrix = matrix[:, :-1]
#         A = array[:, :-1]
#         sol = []
#         for i in range(A.cols):
#             if i not in pivot_cols:
#                 sol.append(0)
#             else:
#                 sol.append(array[pivot_cols.index(i), -1])
#         sol = Matrix(sol)
#         if len(pivot_cols) == array.cols-1:
#             total += sum(sol)
#             continue
#         basis = []
#         for i in range(A.cols):
#             if i not in pivot_cols:
#                 col = []
#                 for j in range(A.cols):
#                     if i==j:
#                         col.append(1)
#                         continue
#                     if j not in pivot_cols:
#                         col.append(0)
#                         continue
#                     row = pivot_cols.index(j)
#                     if (val:=A[row, i]):
#                         col.append(-val / A[row, pivot_cols[row]])
#                     else:
#                         col.append(0)
#                 basis.append(col)
#         basis = Matrix(basis).transpose() if isinstance(basis[0], list) else Matrix(basis)
#         for i in range(basis.cols):
#             col = basis.col(i)
#             vals = []
#             for x in col:
#                 if x%1:
#                     vals.append(x.denominator)
#             try:
#                 basis[:,i] = math.lcm(*vals) * basis[:,i]
#             except Exception as e:
#                 print(e)
#                 breakpoint()

#         vals = []
#         for x in sol:
#             if x%1:
#                 vals.append(x.denominator)
#         factor = math.lcm(*vals)

#         for t in itertools.permutations(range(100), basis.cols):
#             vec = sol
#             for (index,num) in enumerate(t):
#                 vec+=(num/factor)*basis.col(index)
#             if min(vec) >= 0:
#                 sol = vec
#                 break
#         else:
#             print("FAIL.")
#             breakpoint()

#         # breakpoint()
#         # if min(sol) < 0:
#         #     heap = [(-min(sol), sum(sol), sol)]
#         #     heapq.heapify(heap)
#         #     while heap:
#         #         minimum, sm, vec = heapq.heappop(heap)
#         #         minimum *= -1
#         #         if minimum > 0:
#         #             sol = vec
#         #             break
#         #         for c in range(basis.cols):
#         #             v = basis.col(c)
#         #             new_vec = vec+v
#         #             heapq.heappush(heap, (-min(new_vec), sum(new_vec), new_vec))
        

#         total += recur(sol, basis)
#     return total