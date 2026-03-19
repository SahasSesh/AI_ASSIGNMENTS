import random

def update_obstacles(grid, prob=0.05):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if random.random() < prob:
                grid[i][j] = 1
    return grid

def simulate(start, goal):
    pos = start
    grid = [[0]*20 for _ in range(20)]

    while pos != goal:
        print("Position:", pos)
        grid = update_obstacles(grid)

        x, y = pos
        if x < goal[0]:
            x += 1
        elif y < goal[1]:
            y += 1

        pos = (x, y)

    print("Reached Goal")

simulate((0,0), (19,19))
