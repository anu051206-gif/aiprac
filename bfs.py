from collections import deque 
 
def bfs(grid, start, goal): 
    q = deque([(start, [start])]) 
    visited = {start} 
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
 
    while q: 
        (x, y), path = q.popleft() 
 
        if (x, y) == goal: 
            return path 
 
        for dx, dy in moves: 
            nx, ny = x + dx, y + dy 
            if (0 <= nx < len(grid) and 
                0 <= ny < len(grid[0]) and 
                grid[nx][ny] == 0 and 
                (nx, ny) not in visited): 
                visited.add((nx, ny)) 
                q.append(((nx, ny), path + [(nx, ny)])) 
 
    return None 
 
grid = [ 
    [0, 0, 0, 0], 
    [1, 1, 0, 1], 
    [0, 0, 0, 0], 
    [0, 1, 1, 0] 
] 
 
start, goal = (0, 0), (3, 3) 
path = bfs(grid, start, goal) 
 
if path: 
    print("Path found:", path) 
    print("Steps:", len(path) - 1) 
else: 
    print("No path found")
