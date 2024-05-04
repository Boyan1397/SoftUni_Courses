n = int(input())
total_orders = 0
for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    price = price_per_capsule * days * capsules_needed_per_day

    print(f"The price for the coffee is: ${price:.2f}")

    total_orders = total_orders + price
print(f"Total: ${total_orders:.2f}")
