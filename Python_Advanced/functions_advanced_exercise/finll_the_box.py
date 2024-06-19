from collections import deque
def fill_the_box(height, length, width, *cubes):
    space = height * length * width
    cubes = deque(cubes)
    while cubes[0] != "Finish":
        cube = cubes.popleft()
        space -= cube
        if space <= 0:
            free_space = [el for el in cubes if el != "Finish"]
            return f"No more free space! You have {sum(free_space) + abs(space)} more cubes."
    return f"There is free space in the box. You could put {space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5,"Finish"))
print(fill_the_box(5, 5,2, 40, 11, 7, 3, 4, 5,"Finish"))