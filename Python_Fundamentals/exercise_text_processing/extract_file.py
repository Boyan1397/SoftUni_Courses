my_file = input().split("\\")
for words in my_file:
    if "." in words:
        template, extension = words.split(".")
        print(f"File name: {template}")
        print(f"File extension: {extension}")