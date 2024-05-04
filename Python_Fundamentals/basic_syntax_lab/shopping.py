budget = int(input())
total = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    price = int(command)
    if total + price > budget:
        print("You went in overdraft!")
        break
    total += price