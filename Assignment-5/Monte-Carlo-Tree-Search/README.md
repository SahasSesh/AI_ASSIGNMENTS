# Monte Carlo Tree Search

## Aim

To implement Monte Carlo Tree Search (MCTS) for a Tic-Tac-Toe game.

## Theory

Monte Carlo Tree Search is a decision-making algorithm that uses random simulations to determine the best move. Instead of exploring every possible state like Minimax, MCTS performs multiple simulations and chooses the move with the highest success rate.

The algorithm consists of four phases:

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

## Working

1. Generate possible moves.
2. Simulate random games from each move.
3. Count the number of wins.
4. Select the move with the highest score.

## Result

The AI chooses a move based on simulation outcomes rather than exhaustive search.

