import heapq
import random

def generate_grid(size, density):
    return [[1 if random.random() < density else 0 for _ in range(size)] for _ in range(size)]

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def h(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    pq = [(0, start)]
    cost = {start: 0}

    while pq:
        _, curr = heapq.heappop(pq)

        if curr == goal:
            return True

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nxt = (curr[0]+dx, curr[1]+dy)

            if 0 <= nxt[0] < rows and 0 <= nxt[1] < cols:
                if grid[nxt[0]][nxt[1]] == 1:
                    continue

                new_cost = cost[curr] + 1
                if nxt not in cost or new_cost < cost[nxt]:
                    cost[nxt] = new_cost
                    heapq.heappush(pq, (new_cost + h(goal, nxt), nxt))

    return False


grid = generate_grid(20, 0.2)
print(astar(grid, (0,0), (19,19)))
