from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if 3-m > 0 and 3-m < 3-c:
        return False
    return True

def bfs():
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, b), path = queue.popleft()

        if (m, c, b) == goal:
            return path + [(m, c, b)]

        if (m, c, b) in visited:
            continue

        visited.add((m, c, b))

        for mm, cc in moves:
            if b == 1:
                new = (m-mm, c-cc, 0)
            else:
                new = (m+mm, c+cc, 1)

            if valid(new[0], new[1]):
                queue.append((new, path + [(m, c, b)]))

print(bfs())
