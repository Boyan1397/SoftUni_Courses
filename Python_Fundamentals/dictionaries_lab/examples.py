translation = {"apple": "ябълка", "banana":  "банан", "moron": "тъпак"}
searched_num = input()
print(translation.get(searched_num, "no such key"))
                      #if               #else
if translation.get(searched_num):  #if ползваме със  get() !!!!
    print("key found")
else:
    print("key doesnt exist")

del translation["apple"]
print(translation)