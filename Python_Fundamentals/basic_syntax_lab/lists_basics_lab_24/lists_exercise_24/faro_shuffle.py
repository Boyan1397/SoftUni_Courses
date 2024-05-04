deck_of_cards = input().split()
count_shuffles = int(input())
for shuffle in range(count_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]

    deck_after_shuffling = []
    for index in range(len(left_part)):
        deck_after_shuffling.append(left_part[index])
        deck_after_shuffling.append(right_part[index])
    deck_of_cards = deck_after_shuffling
print(deck_after_shuffling)