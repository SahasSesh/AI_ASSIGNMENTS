import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def check_winner(temp_board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
        a,b,c = combo

        if temp_board[a] == temp_board[b] == temp_board[c] and temp_board[a] != " ":
            return temp_board[a]

    if " " not in temp_board:
        return "Draw"

    return None

def random_playout(temp_board, player):
    while True:
        result = check_winner(temp_board)

        if result:
            return result

        moves = [i for i in range(9) if temp_board[i] == " "]

        move = random.choice(moves)

        temp_board[move] = player

        player = "O" if player == "X" else "X"

def best_move():
    best_score = -1
    best_index = -1

    for move in range(9):
        if board[move] == " ":

            wins = 0

            for _ in range(100):
                temp_board = board.copy()

                temp_board[move] = "X"

                result = random_playout(temp_board, "O")

                if result == "X":
                    wins += 1

            if wins > best_score:
                best_score = wins
                best_index = move

    board[best_index] = "X"

board[0] = "X"
board[1] = "X"
board[3] = "O"
board[4] = "O"

print("Before AI Move:")
print_board()

best_move()

print("\nAfter AI Move:")
print_board()

print("\nResult:", check_winner(board))
