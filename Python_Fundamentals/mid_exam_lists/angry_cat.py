price_ratings = ([int(num) for num in input().split(", ")])
entry_point = int(input())
command = input()
right_damage = []
left_damage = []
if command == 'cheap':
    for num in range(1,entry_point):
        if price_ratings[num] < price_ratings[entry_point]:
            left_damage.append(price_ratings[num])
    for num in range(entry_point + 1,len(price_ratings)-1):
        if price_ratings[num] < price_ratings[entry_point]:
            right_damage.append(price_ratings[num])
elif command == "expensive":
    for num in range(1, entry_point):
        if price_ratings[num] >= price_ratings[entry_point]:
            left_damage.append(price_ratings[num])
    for num in range(entry_point + 1, len(price_ratings) - 1):
        if price_ratings[num] >= price_ratings[entry_point]:
            right_damage.append(price_ratings[num])