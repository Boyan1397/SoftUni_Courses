versions = ([int(el) for el in input().split(".")])
versions[-1] += 1
for index in range(len(versions) -1, -1, -1):
    if versions[index] > 9:
        versions[index] = 0
        if index -1 >= 0:
            versions[index - 1] += 1

print(".".join(str(number) for number in versions))