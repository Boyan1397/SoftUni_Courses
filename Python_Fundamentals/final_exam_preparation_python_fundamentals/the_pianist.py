my_dict = {}
n_lines = int(input())
for _ in range(n_lines):
    data = input()
    piece = data.split("|")[0]
    composer = data.split("|")[1]
    piano_key = data.split("|")[2]
    my_dict[piece] = {"composer": composer, "key": piano_key}

command = input()
while command != "Stop":
    if "Add" in command:
        piece = command.split("|")[1]
        composer = command.split("|")[2]
        piano_key = command.split("|")[3]
        if piece in my_dict.keys():
            print(f"{piece} is already in the collection!")
        elif piece not in my_dict.keys():
            my_dict[piece] = {"composer": composer, "key": piano_key}
            print(f"{piece} by {composer} in {piano_key} added to the collection!")
    elif "Remove" in command:
        piece = command.split("|")[1]
        if piece not in my_dict.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        elif piece in my_dict.keys():
            print(f"Successfully removed {piece}!")
            del my_dict[piece]
    elif "ChangeKey" in command:
        piece = command.split("|")[1]
        new_key = command.split("|")[2]
        if piece not in my_dict.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        elif piece in my_dict.keys():
            my_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    command = input()

for name_piece in my_dict.keys():
    print(f"{name_piece} -> Composer: {my_dict[name_piece]['composer']}, Key: {my_dict[name_piece]['key']}")