def fibonacci():
    f_num = 0
    s_num = 1

    while True:
        yield f_num
        f_num, s_num = s_num, f_num + s_num


generator = fibonacci()

for i in range(5):
    print(next(generator))
