words = input().split(" ")
special_words = ([word for word in words if len(word) % 2 == 0])
print("\n".join(special_words))