from collections import deque

all_money = [int(el) for el in input().split()] #last
prices = deque(int(el) for el in input().split()) #first

foods_count = 0

while all_money and prices:
    curr_money = all_money[-1]
    curr_price = prices[0]

    if curr_money == curr_price:
        foods_count += 1
        all_money.pop()
        prices.popleft()

    elif curr_money > curr_price:
        foods_count += 1
        change = curr_money - curr_price
        all_money.pop()
        prices.popleft()
        if all_money:
            all_money[-1] += change

    elif curr_money < curr_price:
        all_money.pop()
        prices.popleft()

if foods_count >= 4:
    print(f"Gluttony of the day! Henry ate {foods_count} foods.")

elif 1 < foods_count < 4:
    print(f"Henry ate: {foods_count} foods.")

elif foods_count == 1:
    print(f"Henry ate: {foods_count} food.")

elif foods_count == 0:
    print("Henry remained hungry. He will try next weekend again.")