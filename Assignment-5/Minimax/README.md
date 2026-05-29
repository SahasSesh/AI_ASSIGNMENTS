# Minimax Algorithm

## Aim

To implement the Minimax algorithm for a Tic-Tac-Toe game and determine the best move for the AI player.

## Theory

Minimax is a search algorithm used in two-player games. It assumes that both players play optimally. The algorithm explores all possible future game states and chooses the move that gives the best outcome for the AI.

In this implementation, X represents the AI player and O represents the opponent.

## Working

1. Check whether the game has ended.
2. If X wins, return +1.
3. If O wins, return -1.
4. If the game is a draw, return 0.
5. Generate all possible moves.
6. Recursively evaluate each move.
7. Choose the move with the highest score.

## Result

The AI successfully selects the best possible move using the Minimax algorithm.

