import string

advent = []
temp = []

with open("advent.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        if len(temp) < 3:
            temp.append(line.strip())
        else:
            advent.append(temp.copy())
            temp.clear()
            temp.append(line.strip())

if len(temp) > 0:
    advent.append(temp.copy())

small = dict([(a, i) for i, a in enumerate(string.ascii_lowercase, start=1)])
cap = dict([(a, i) for i, a in enumerate(string.ascii_uppercase, start=len(small) + 1)])

points = 0

for ad in advent:
    badge = list(set.intersection(*list(map(set, ad))))[0]

    if badge.isupper():
        points += cap.get(badge)
    else:
        points += small.get(badge)

print(points)
