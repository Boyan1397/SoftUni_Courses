def squares(n):
    start = 1
    while start <= n:
        yield start ** 2
        start += 1

print(list(squares(5)))
      #the list calls next automatically!!!