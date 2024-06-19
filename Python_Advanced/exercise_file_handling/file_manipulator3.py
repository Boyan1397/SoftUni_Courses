import os

while True:
    command, *data = input().split("-")
    if command == "End":
        break
    elif command == "Create":
        with open(f"resources/{data[0]}", "w") as file:
            pass
    elif command == "Add":
        with open(f"resources/{data[0]}", "a") as file:
            file.write(f"{data[1]}\n")
    elif command == "Replace":
        try:
            with open(f"resources/{data[0]}", "r+") as file:
                text = file.read()
                text = text.replace(data[1], data[2])

                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"resources/{data[0]}")
        except FileNotFoundError:
            print("An error occurred")


# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End