def is_index_in_range(index, some_list):
    if 0 <= index < len(some_list):
        return True
    return False


def is_valid(first_index, second_index, some_list):
    if is_index_in_range(first_index, some_list) and is_index_in_range(second_index, some_list) and first_index != second_index:
        return True
    return False


cards = input().split()

command = input()
moves = 0
while command != "end":
    moves += 1
    index1, index2 = [int(el) for el in command.split()]
    if is_valid(index1, index2, cards):
        if cards[index1] == cards[index2]:
            element = cards[index1]
            cards.remove(element)
            cards.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
    else:
        middle = len(cards) // 2
        cards.insert(middle,f"-{moves}a")
        cards.insert(middle,f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    if not cards:
        print(f"You have won in {moves} turns!")
        break

    command = input()
if command == "end":
    print("Sorry you lose :(")
    print(" ".join(cards))



