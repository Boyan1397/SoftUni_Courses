rows = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

primary = [matrix[r][r] for r in range(rows)]
secondary = [matrix[r][rows - r -1] for r in range(rows)]
print(f"Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}")