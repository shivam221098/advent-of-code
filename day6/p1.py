advent = ""

with open("advent.txt", "r", encoding="utf-8") as file:
    advent += file.read().strip()

index = None
for i in range(0, len(advent)):
    print(advent[i:i + 4])
    if len(set(advent[i:i + 4])) == len(advent[i:i + 4]):
        index = i
        break

print(index + 4)