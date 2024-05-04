number = int(input())
positives = []
negatives = []
for index in range(number):
    nm = int(input())
    if nm >= 0:
        positives.append(nm)
    elif nm < 0:
        negatives.append(nm)
print(positives)
print(negatives)