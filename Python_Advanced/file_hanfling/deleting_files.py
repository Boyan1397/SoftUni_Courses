# import os.path
#
# path = os.path.join("resources", "numbers.txt")
# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("Alredy deleted that")
import os.path

path = os.path.join("..", "error_handling_exercise","some_example_file") #relative path
with open(path, "r") as file:
    print(file.read())