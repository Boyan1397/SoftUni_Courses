import os

ABS_DIR_PATH = os.path.join(os.path.abspath("."), "..") # ака достъпваме файлове в други папки на същата директория
path = os.path.join(ABS_DIR_PATH, "error_handling_exercise", "some_example_file")
file = open(path, "r")
print(file.read())


# file_name = "some_example_file"
# path = os.path.join("..", "error_handling_exercise", file_name)
# file = open(path, 'r')
# print(file.read())