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

def heuristic():
    score = 0

    for cell in board:
        if cell == "X":
            score += 1
        elif cell == "O":
            score -= 1

    return score

def alphabeta(depth, is_maximizing, alpha, beta):
    result = check_winner()

    if result == "X":
        return 100

    if result == "O":
        return -100

    if result == "Draw":
        return 0

    if depth == 0:
        return heuristic()

    if is_maximizing:
        value = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                value = max(
                    value,
                    alphabeta(depth - 1, False, alpha, beta)
                )

                board[i] = " "

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

        return value

    else:
        value = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                value = min(
                    value,
                    alphabeta(depth - 1, True, alpha, beta)
                )

                board[i] = " "

                beta = min(beta, value)

                if alpha >= beta:
                    break

        return value

def best_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            score = alphabeta(
                3,
                False,
                -math.inf,
                math.inf
            )

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
