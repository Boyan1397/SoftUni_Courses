def team_lineup(*args):
    countries_pls_dict = {}
    for tup in args:
        if tup[1] not in countries_pls_dict.keys():
            countries_pls_dict[tup[1]] = []
        countries_pls_dict[tup[1]].append(tup[0])
    sorted_dict = sorted(countries_pls_dict.items(), key= lambda x: (-len(x[1]), x[0]))
    output = ""
    for country, names in sorted_dict:
        output += f"{country}:\n"
        for name in names:
            output += f"  -{name}\n"
    return output

print(team_lineup(

("Harry Kane", "England"),

("Manuel Neuer", "Germany"),

("Raheem Sterling", "England"),

("Toni Kroos", "Germany"),

("Cristiano Ronaldo", "Portugal"),

("Thomas Muller", "Germany")))


print(team_lineup(

("Harry Kane", "England"),

("Manuel Neuer", "Germany"),

("Raheem Sterling", "England"),

("Toni Kroos", "Germany"),

("Cristiano Ronaldo", "Portugal"),

("Thomas Muller", "Germany"),

("Bruno Fernandes", "Portugal"),

("Bernardo Silva", "Portugal"),

("Harry Maguire", "England")))