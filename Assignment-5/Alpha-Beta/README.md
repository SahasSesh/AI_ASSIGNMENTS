# Alpha-Beta Pruning

## Aim

To implement the Alpha-Beta Pruning algorithm for a Tic-Tac-Toe game.

## Theory

Alpha-Beta Pruning is an optimization of the Minimax algorithm. It reduces the number of nodes that need to be evaluated in the game tree.

The algorithm maintains two values:

* Alpha: Best value that the maximizing player can guarantee.
* Beta: Best value that the minimizing player can guarantee.

When Alpha becomes greater than or equal to Beta, the remaining branches are not explored because they cannot affect the final decision.

## Working

1. Generate possible moves.
2. Evaluate game states recursively.
3. Update alpha and beta values.
4. Prune unnecessary branches.
5. Select the best move.

## Result

The AI successfully finds the optimal move while evaluating fewer states than Minimax.

