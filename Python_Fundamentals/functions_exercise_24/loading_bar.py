def loads(input_number):
    if input_number == 100:
        return "100% Complete!\n" \
               "[%%%%%%%%%%]"
    percentage = "%" * (input_number // 10)
    dots = "." * (10 - (input_number // 10))
    return f"{input_number}% [{percentage}{dots}]\n" \
           f"Still loading..."


number = int(input())
print(loads(number))