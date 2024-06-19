def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"

print(get_info(**{"name": "Bobo", "town": "Turnovo", "age": 16})) #когато разопаковаме взимаме само value bez key
