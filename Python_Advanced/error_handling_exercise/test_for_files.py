import os.path

path = os.path.join("file_hanfling", "resources", "numbers")
with open(path, "r") as file:
    print(file.read())