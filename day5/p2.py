"""
Stack based approach
"""
from stack import Stack
from collections import defaultdict
import re

tower = defaultdict(Stack)
moves = []
temp = []

with open("advent.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while "1" not in line:
        temp.append(line.replace("     ", " [~] ").replace("    ", "[~] ").replace("[", "").replace("]", "").split())
        line = file.readline()

    temp.append(line.strip().replace("[", "").replace("]", "").split())

    # adding alphabets to stack
    for i, pos in enumerate(temp[-1]):
        for j in range(len(temp) - 2, -1, -1):
            if i < len(temp[j]) and temp[j][i] != "~" and temp[j][i] != "~~":
                tower[int(pos)].push(temp[j][i])

    for line in file.readlines():
        if line.strip():
            nums = list(map(int, re.findall(r"[\d]+", line.strip())))
            moves.append(nums)

for ele, from_, to_ in moves:
    from_stack = tower[from_]
    to_stack = tower[to_]

    i = 0

    new_stack = Stack()

    while i != ele:
        new_stack.push(from_stack.pop)
        i += 1

    while new_stack.height != 0:
        to_stack.push(new_stack.pop)

    # to_stack.push(from_stack.pop)

print("".join(map(lambda x: x.pop, tower.values())))
