deck_of_cards = input().split()
count_of_shuffles = int(input())
for card_index in range(count_of_shuffles):
    mid_of_cards = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:mid_of_cards]
    right_part = deck_of_cards[mid_of_cards:]
    shuffled_deck = []
    for card in range(len(left_part)):
        shuffled_deck.append(left_part[card])
        shuffled_deck.append(right_part[card])
        deck_of_cards = shuffled_deck
print(deck_of_cards)