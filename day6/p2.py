advent = ""

with open("advent.txt", "r", encoding="utf-8") as file:
    advent += file.read().strip()

index = None
for i in range(0, len(advent)):
    print(advent[i:i + 14])
    if len(set(advent[i:i + 14])) == len(advent[i:i + 14]):
        index = i
        break

print(index + 14)