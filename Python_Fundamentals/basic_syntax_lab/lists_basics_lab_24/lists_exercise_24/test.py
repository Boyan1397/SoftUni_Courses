my_list = [2, 7, 1, 3, 5, 19 , 23]
my_list_with_strings = ["Sofia", "Pesho", "tarator", "Tosho", 'tosho']

#Sort. works with integer and string
#my_list.sort(reverse= True)
#print(my_list)

#my_list_with_strings.sort()
#print(my_list_with_strings)

#.Pop removes last index when alone(VRUSHTA STOINOST)
#deleted_number = my_list.pop()
#print(deleted_number)
#my_list.pop(0)
#print(my_list)

#.remove premahva element
#element = 2
#my_list.remove(element)
#print(my_list)

#Insert + element
#index = 2
#element = "Banan"
#my_list.insert(index, element)
#print(my_list)


#Index namira indexa na daden element
#index = my_list.index(7)
#print(index)

#del premahva index
#index = 2
#del my_list[index]
#print(my_list)

# indexirane bez da gurmi
for index in range(len(my_list_with_strings) - 1,-1,-1): #vurvi otzad napred sus stupka -1
    if index % 2 == 0:
        my_list_with_strings.pop(index)
print(my_list_with_strings)