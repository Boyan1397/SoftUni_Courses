from collections import deque
import operator


def print_board():
    [print(f"[ {', '.join(row)} ]") for row in board]

def put_circle():
    row = 0
    while row != ROWS and board[row][player_col] == "0":
        row += 1

    board[row - 1][player_col] = symbol
    return row - 1


def find_count(row, col, dx, dy, operator_func):
    count = 0
    for i in range(1, 4):
        new_row = operator_func(row, dx * i)
        new_col = operator_func(col, dy * i)
        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            break

        if board[new_row][new_col] != symbol:
            break
        count += 1
    return count


def find_win(row, col):
    for x, y in directions:
        count = find_count(row, col,x, y, operator.add) + find_count(row, col, x, y, operator.sub) + 1
        if count >= 4:
            return True

        if counter_for_rows == ROWS * COLS:
            print_board()
            raise SystemExit
    return False


ROWS, COLS = 6, 7
counter_for_rows = 0
board = [COLS * ["0"] for row in range(ROWS)]
turns = deque([[1, "1"], [2, "2"]])

directions = (
    (-1, -1),  # top left diagonal
    (-1, 0),  # top
    (-1, +1),  # top right diagonal
    (0, +1),  # right
)

win = False
while not win:
    print_board()
    player, symbol = turns[0]

    try:
        player_col = int(input(f"Player {player} a column : ")) - 1
    except ValueError:
        print("The column you enter must be from 1 to 7!")
        continue

    if not (0 <= player_col < COLS):
        print("The column you enter must be from 1 to 7!")
        continue

    if board[0][player_col] != "0":
        print("No more space at this column!")
        continue

    row = put_circle()
    counter_for_rows += 1
    win = find_win(row, player_col)

    turns.rotate()

print_board()
print(f"Player {turns[1][0]} wins!")