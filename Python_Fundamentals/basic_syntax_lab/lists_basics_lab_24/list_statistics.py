count_positives = []
sum_negatives = []
n = int(input())
for _ in range(n):
    current_num = int(input())
    if current_num >= 0:
        count_positives.append(current_num)
    else:
        sum_negatives.append(current_num)
print(count_positives)
print(sum_negatives)
print(f"Count of positives: {len(count_positives)}")
print(f"Sum of negatives: {sum(sum_negatives)}")