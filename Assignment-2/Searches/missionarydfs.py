start = (3, 3, 1)
goal = (0, 0, 0)

moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

visited = set()

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if 3-m > 0 and 3-m < 3-c:
        return False
    return True

def dfs(state, path):
    if state == goal:
        return path + [state]

    if state in visited:
        return None

    visited.add(state)

    m, c, b = state

    for mm, cc in moves:
        if b == 1:
            new = (m-mm, c-cc, 0)
        else:
            new = (m+mm, c+cc, 1)

        if valid(new[0], new[1]):
            result = dfs(new, path + [state])
            if result:
                return result

    return None

print(dfs(start, []))
