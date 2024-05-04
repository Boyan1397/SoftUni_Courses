numbers = [int(num) for num in input().split(", ")]
group = 10
while numbers:
    filtered_list = ([num for num in numbers if num <= group])
    print(f"Group of {group}'s: {filtered_list}")

    group += 10
    numbers =([number for number in numbers if number not in filtered_list])



