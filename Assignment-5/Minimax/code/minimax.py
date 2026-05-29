import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def check_winner():
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        a,b,c = combo

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

def minimax(is_maximizing):
    result = check_winner()

    if result == "X":
        return 1

    if result == "O":
        return -1

    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "X"

board[0] = "X"
board[1] = "X"
board[3] = "O"
board[4] = "O"

print("Before AI Move:")
print_board()

best_move()

print("\nAfter AI Move:")
print_board()

print("\nWinner:", check_winner())
