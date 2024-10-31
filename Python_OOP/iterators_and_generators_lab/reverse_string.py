def reverse_text(some_string):
    start = 0
    end = len(some_string) - 1

    while start <= end:
        yield some_string[end]
        end -= 1

for char in reverse_text("step"):
    print(char, end='')