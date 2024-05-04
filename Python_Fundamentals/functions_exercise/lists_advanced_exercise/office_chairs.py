def check_the_rooms(number_of_rooms):
    free_chairs = 0

    for room in range(1, number_of_rooms + 1):
        current_chairs, current_visitors = input().split(" ")
        difference = len(current_chairs) - int(current_visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
        free_chairs += difference

    return free_chairs

count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")