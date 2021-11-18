board = []


def init():
    create_board()


def main():
    init()

    current_player = "X"
    game_over = False

    # main loop
    while game_over == False:
        display()
        player_turn(current_player)
        game_over = board_check(game_over)
        if (game_over == False):
            current_player = next_player(current_player)


def create_board():
    for i in range(0, 3):
        board.append([])
        for j in range(0, 3):
            board[i].append(" ")


def display_board():
    print("0", "|", "1", "|", "2")
    print("-", "-", "-", "-", "-")
    for i in range(0, 3):
        print(board[i][0], "|", board[i][1], "|", board[i][2])

    print("-", "-", "-", "-", "-", "\n")


def display():
    display_board()


def player_turn(current_player):
    valid_trun = True

    print("Player ", current_player, ", enter a number between 0 and 2")
    x = int(input())
    print("Player ", current_player, ", enter a number between 0 and 2")
    y = int(input())

    if (valid_input(x, y) == False):
        print("Invalid input")
        valid_trun = False

    if (validate_position(x, y) == False):
        print("That space is taken")
        valid_trun = False

    if (valid_trun == True):
        place_marker_at(x, y, current_player)
    else:
        player_turn(current_player)


def place_marker_at(x, y, current_player):
    board[x][y] = current_player


def validate_position(x, y):
    if board[x][y] == " ":
        return True
    else:
        return False


def valid_input(x, y):
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        return True
    else:
        return False


def board_check(game_over):
    print("Checking board")
    if board[0][0] == board[0][1] == board[0][2] == "X":
        print("Player X wins!")
        game_over = True
    elif board[0][0] == board[0][1] == board[0][2] == "O":
        print("Player O wins!")
        game_over = True
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        print("Player X wins!")
        game_over = True
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        print("Player O wins!")
        game_over = True
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        print("Player X wins!")
        game_over = True
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        print("Player O wins!")
        game_over = True
    elif board[0][0] == board[1][0] == board[2][0] == "X":
        print("Player X wins!")
        game_over = True
    elif board[0][0] == board[1][0] == board[2][0] == "O":
        print("Player O wins!")
        game_over = True
    elif board[0][1] == board[1][1] == board[2][1] == "X":
        print("Player X wins!")
        game_over = True
    elif board[0][1] == board[1][1] == board[2][1] == "O":
        print("Player O wins!")
        game_over = True
    elif board[0][2] == board[1][2] == board[2][2] == "X":
        print("Player X wins!")
        game_over = True

    return check_if_diagonal_win(game_over)


def check_if_diagonal_win(game_over):
    if board[0][0] == board[1][1] == board[2][2] == "X":
        print("Player X wins!")
        game_over = True
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        print("Player O wins!")
        game_over = True
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        print("Player X wins!")
        game_over = True
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        print("Player O wins!")
        game_over = True

    return game_over


def next_player(current_player):
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    return current_player


main()

exit(0)