def a():
    print("a")

    def b():
        print("g")
    return b

res = a()
res()