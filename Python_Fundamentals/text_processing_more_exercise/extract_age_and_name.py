number_of_lines = int(input())
age = ""
for _ in range(number_of_lines):
    text = input()
    start_of_name = text.index("@")
    end_of_name = text.index("|")
    name = text[start_of_name+1:end_of_name]
    start_of_age = text.index("#")
    end_of_age = text.index("*")
    age = text[start_of_age+1:end_of_age]
    print(f"{name} is {age} years old.")
