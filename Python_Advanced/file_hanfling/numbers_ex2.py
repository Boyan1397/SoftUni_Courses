import os.path

path = os.path.join("resources", "numbers.txt")

file = open(path)

total = 0
for line in file.readlines():
    line = int(line.strip())
    total += line
print(total)