rows_size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(rows_size)]

primary = [matrix[r][r] for r in range(rows_size)]
secondary = [matrix[r][rows_size - r - 1] for r in range(rows_size)]
#[rows_size - r - 1] фрмула на обратен диагонал  за квадратна матрица

difference = abs(sum(primary) - sum(secondary))
print(difference)

