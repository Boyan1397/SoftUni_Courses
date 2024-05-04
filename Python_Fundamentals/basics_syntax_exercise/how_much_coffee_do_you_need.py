command = input()
count_of_coffees = 0
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "cat" \
            or command.lower() == "dog" \
            or command.lower() == "movie":
        if command.islower():
            count_of_coffees += 1
        else:
            count_of_coffees += 2
    command = input()
if count_of_coffees > 5:
    print("You need extra sleep")
else:
    print(count_of_coffees)