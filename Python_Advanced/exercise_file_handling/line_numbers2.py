from string import punctuation
with open("resources/text.txt2", "r") as file:
    text = file.readlines()


for row in range(len(text)):
    letters, signs = 0, 0
    text[row] = text[row].replace("\n", "")
    for element in text[row]:
        if element.isalpha():
            letters += 1
        elif element in punctuation:
            signs += 1
    with open("resources/output.txt2", "a") as file:
        file.write(f"Line {row+1}: {text[row]}. ({letters})({signs})\n")
