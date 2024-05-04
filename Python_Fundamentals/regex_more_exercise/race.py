import re

my_dict = {}
participants = input().split(", ")

pattern_letters = r"[A-Za-z]"
pattern_nums = r"\d"

while True:
    text = input()
    if text == "end of race":
        break
    result_letters = re.findall(pattern_letters, text)
    full_name = ("".join(result_letters))
    result_numbers = re.findall(pattern_nums, text)
    if full_name in participants:
        if full_name not in my_dict:
            my_dict[full_name] = result_numbers
        else:
            my_dict[full_name].extend([int(num) for num in result_numbers])

for key,values in my_dict.items():
    my_list = [int(value) for value in values]
    my_dict[key] = sum(my_list)

sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
places = ["1st", "2nd", "3rd"]
for num, (key, value) in enumerate(sorted_dict[:3]):
    print(f"{places[num]} place: {key}")