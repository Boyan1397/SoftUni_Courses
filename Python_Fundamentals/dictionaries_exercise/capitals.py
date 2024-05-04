# 1
# countries = input().split(", ")
# capitals = input().split(", ")
# my_dict = dict(zip(countries, capitals))
# for country, capital in my_dict.items():
#     print(f"{country} -> {capital}")

# 2
countries = input().split(", ")
capitals = input().split(", ")
my_dict = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in my_dict.items():
    print(f"{country} -> {capital}")
