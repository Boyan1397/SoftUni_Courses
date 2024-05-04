my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
#first_sorted = sorted(my_dict.keys()) sorting the keys alphabetically


# sorting by value with lambda really good
sorted_dict = dict(sorted(my_dict.items(), key= lambda x:x[1]))
print(sorted_dict)

