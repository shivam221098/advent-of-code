advent = []

with open("advent.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        p1, p2 = line.strip().split(",")
        s1, e1 = p1.split("-")
        s2, e2 = p2.split("-")

        advent.append((
            (int(s1), int(e1)),
            (int(s2), int(e2))
        ))

count = 0

for p1, p2 in advent:
    s1, e1 = p1
    s2, e2 = p2

    st1 = [i for i in range(s1, e1 + 1)]
    st2 = [i for i in range(s2, e2 + 1)]

    intersection = set(st1).intersection(set(st2))

    if len(intersection) > 0:
        count += 1

print(count)
