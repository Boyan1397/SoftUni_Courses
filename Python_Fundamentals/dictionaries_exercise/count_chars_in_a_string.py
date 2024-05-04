my_string = input()
my_dict = {}
for letter in my_string:
    if letter != " ":
        if letter not in my_dict.keys():
            my_dict[letter] = 0
        my_dict[letter] += 1
for key, value in my_dict.items():
    print(f"{key} -> {value}")