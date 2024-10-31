def first_n(n):
    start = 1
    while start <= n:
        yield start
        start += 1

res = first_n(4)
for num in res:
    print(num)
