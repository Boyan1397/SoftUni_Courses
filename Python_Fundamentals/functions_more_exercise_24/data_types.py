def data_type(text, num):
    new_num = 0
    if text == "int":
        new_num = int(num) * 2
        return new_num
    elif text == "real":
        new_num = float(num) * 1.5
        return (f"{new_num:.2f}")
    elif text == "string":
        new_num = "$" + str(num) + "$"
        return new_num


text_input = input()
number = input()
print(data_type(text_input, number))
