class vowels:
    all_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def __init__(self, some_string):
        self.some_string = some_string
        self.start = -1
        self.vowels_values = [el for el in self.some_string if el in vowels.all_vowels]


    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start < len(self.vowels_values):
            return self.vowels_values[self.start]

        raise StopIteration



my_string = vowels('Abcedifuty0o')

for char in my_string:

    print(char)