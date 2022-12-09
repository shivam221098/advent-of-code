import string

advent = []

with open("advent.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        advent.append(line.strip())

small = dict([(a, i) for i, a in enumerate(string.ascii_lowercase, start=1)])
cap = dict([(a, i) for i, a in enumerate(string.ascii_uppercase, start=len(small) + 1)])

points = 0

for ad in advent:
    score = 0
    mid = len(ad) // 2
    m1, m2 = ad[:mid], ad[mid:]
    m1.isupper()
    for i in set(m1).intersection(set(m2)):
        if i.isupper():
            score += cap.get(i)
        else:
            score += small.get(i)
    points += score

print(points)