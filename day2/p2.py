advent = []

with open("data/advent1.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        p1, p2 = line.strip().split()
        advent.append((p1, p2))

mappings = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y"
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z"
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X"
    }
}

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
scores1 = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

points = 0

for p1, p2 in advent:
    point = scores1.get(p2) + scores.get(mappings.get(p1).get(p2))
    points += point
    print(point, scores1.get(p2), scores.get(mappings.get(p1).get(p2)))

print(points)



