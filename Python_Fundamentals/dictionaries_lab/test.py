my_dict = {"basics": {"for loops": "for loops in depth"}}
print(my_dict["basics"]["for loops"])
my_dict["basics"]["while loops"] = "while loops in depth"
print(my_dict)
my_dict.update({"fundamentals": {"dictionaries":"nested dicts"}})
my_dict["fundamentals"]= {"loop advanced": "new one"}
print(my_dict)