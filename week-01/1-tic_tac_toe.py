board = [" "] * 9

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),  # diagonals
]


def print_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")


def check_winner(player):
    return any(board[a] == board[b] == board[c] == player for a, b, c in WIN_LINES)


def main():
    player = "X"
    print_board()

    while " " in board:
        pos = int(input(f"Player {player}, enter position (0-8): "))
        if board[pos] != " ":
            print("Cell taken, try again.")
            continue

        board[pos] = player
        print_board()

        if check_winner(player):
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print("It's a draw!")


main()
