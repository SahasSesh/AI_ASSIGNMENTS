# Heuristic Alpha-Beta Search

## Aim

To implement Heuristic Alpha-Beta Search for a Tic-Tac-Toe game.

## Theory

Heuristic Alpha-Beta Search is an extension of Alpha-Beta Pruning. Instead of exploring the entire game tree, the search is limited to a fixed depth. A heuristic evaluation function is used to estimate the value of non-terminal states.

This reduces computation time and is useful for larger games where exploring the full game tree is expensive.

## Working

1. Generate possible moves.
2. Search up to a fixed depth.
3. Evaluate board states using a heuristic function.
4. Apply Alpha-Beta pruning.
5. Choose the move with the highest score.

## Result

The AI selects a good move using a depth-limited search and heuristic evaluation.

