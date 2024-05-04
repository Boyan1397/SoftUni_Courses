from collections import deque

bullet_price = int(input())
barrel_capacity = int(input())
current_capacity = barrel_capacity
#>
bullets_sizes = deque(int(el) for el in input().split())
#<
locks_sizes = deque(int(el) for el in input().split())
intelligence_value = int(input())

total_expenses = 0
is_broken = False
while locks_sizes:
        current_capacity -= 1
        current_bullet = bullets_sizes.pop()
        total_expenses += bullet_price
        current_lock = locks_sizes.popleft()
        if current_bullet > current_lock:
            locks_sizes.appendleft(current_lock)
            print("Ping!")
        elif current_bullet <= current_lock:
            print("Bang!")
        if current_capacity == 0:
            if not bullets_sizes:
                break
            else:
                current_capacity = barrel_capacity
                print("Reloading!")
        if not bullets_sizes:
            break


if not locks_sizes:
    print(f"{len(bullets_sizes)} bullets left. Earned ${intelligence_value - total_expenses}")

elif locks_sizes:
    print(f"Couldn't get through. Locks left: {len(locks_sizes)}")