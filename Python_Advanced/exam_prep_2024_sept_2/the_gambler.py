size = int(input())

amount = 100

matrix = [list(input()) for r in range(size)]
gambler_pos = []

directions ={"up": [-1, 0],
             "down": [1, 0],
             "right": [0, 1],
             "left": [0, -1],
}

for r in range(size):
    for c in range(size):
        if matrix[r][c] == "G":
            gambler_pos = [r, c]
            matrix[r][c] = "-"


command = input()
jackpot = False
while command != "end":
    new_row = gambler_pos[0] + directions[command][0]
    new_col = gambler_pos[1] + directions[command][1]
    if not (0 <= new_row < size and 0 <= new_col < size):
        amount = 0
        print("Game over! You lost everything!")
        break
    gambler_pos = [new_row, new_col]

    if matrix[new_row][new_col] == "W":
        amount += 100
        matrix[new_row][new_col] = "-"
    elif matrix[new_row][new_col] == "P":
        amount -= 200
        matrix[new_row][new_col] = "-"
        if amount <= 0:
            print("Game over! You lost everything!")
            break
    elif matrix[new_row][new_col] == "J":
        amount += 100000
        matrix[new_row][new_col] = "-"
        jackpot = True
        break

    command = input()

matrix[gambler_pos[0]][gambler_pos[1]] = "G"

if jackpot:
    print("You win the Jackpot!\n"
          f"End of the game. Total amount: {amount}$")
    print(*[''.join(row) for row in matrix], sep="\n")
elif not jackpot and amount > 0:

    print(f"End of the game. Total amount: {amount}$")
    print(*[''.join(row) for row in matrix], sep="\n")





# ['W', '-', 'G', 'W']
# ['W', '-', '-', 'W']
# ['-', '-', 'P', '-']
# ['-', '-', '-', '-']