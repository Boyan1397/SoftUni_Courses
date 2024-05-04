number_of_rooms = int(input())
total_free_chairs = 0
are_chairs = True
for room in range(1,number_of_rooms + 1):
    chairs, people = input().split()
    visitors = int(people)
    if visitors > len(chairs):
        are_chairs = False
        needed_chairs = visitors - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
    elif len(chairs) > visitors:
        free_chairs = len(chairs) - visitors
        total_free_chairs += free_chairs
if are_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")














































