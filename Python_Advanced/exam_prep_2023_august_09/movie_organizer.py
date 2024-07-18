def movie_organizer(*args):
    movies_dict = {}
    for name, genre in args:
        if genre not in movies_dict.keys():
            movies_dict[genre] = []
        movies_dict[genre].append(name)

    sorted_dict = dict(sorted(movies_dict.items(), key= lambda x: (-len(x[1]), x[0])))

    output = ""
    for genres, names_lists in sorted_dict.items():
        sorted_names = sorted(names_lists)
        output += f"{genres} - {len(names_lists)}\n"
        for curr_name in sorted_names:
            output += f"* {curr_name}\n"
    return output






# print(movie_organizer(
#
# ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))



print(movie_organizer(
("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))






