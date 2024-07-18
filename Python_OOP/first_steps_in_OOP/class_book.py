class Book:
    def __init__(self, name, author, pages): #__instrcutor__(parameters)
        self.name = name  # закачи към instance(object).property(name)
        self.author = author #закачи към instance(object).property(author)
        self.pages = pages # закачи към instance(object).property(pages)

    def readit(self):
        return "Boyan is reading..."

    def stop_reading(self):
        return "Boyan stopped reading and right after that he fell asleep!"


book = Book("Godfather", "Mario Puzo", 400) #arguments
book2 = Book("Interstellar", "Mario Puzo", 400) #arguments
print(book.name)
print(book.author)
print(book.pages)

print(f"{book.readit()}")
print(book.stop_reading())