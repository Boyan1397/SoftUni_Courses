n = int(input())
starting_list = []
filtered_list = []
for _ in range(n):
    current_numbers = int(input())
    starting_list.append(current_numbers)
    command = input()

    if command == "even":
        for number in starting_list:
            if number % 2 == 0:
                filtered_list.append(number)

    elif command == "odd":
        for number in starting_list:
            if number % 2 != 0:
                filtered_list.append(number)

    elif command == "positive":
        for number in starting_list:
            if number >= 0:
                filtered_list.append(number)

    elif command == "negative":
        for number in starting_list:
            if number < 0:
                filtered_list.append(number)
    print(filtered_list)