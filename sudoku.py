def solve(b): 
    for r in range(9): 
        for c in range(9): 
            if b[r][c] == 0: 
                used = set(b[r]) 
                used.update(b[i][c] for i in range(9)) 
                used.update(b[i][j] for i in range(r//3*3, r//3*3+3) 
                            for j in range(c//3*3, c//3*3+3)) 
 
                for n in set(range(1, 10)) - used: 
                    b[r][c] = n 
                    if solve(b): 
                        return True 
                    b[r][c] = 0 
                return False 
    return True 
 
 
b = [ 
    [5,3,0,0,7,0,0,0,0], 
    [6,0,0,1,9,5,0,0,0], 
    [0,9,8,0,0,0,0,6,0], 
    [8,0,0,0,6,0,0,0,3], 
    [4,0,0,8,0,3,0,0,1], 
    [7,0,0,0,2,0,0,0,6], 
    [0,6,0,0,0,0,2,8,0], 
    [0,0,0,4,1,9,0,0,5], 
    [0,0,0,0,8,0,0,7,9] 
] 
 
if solve(b): 
    for row in b: 
        print(*row) 
else: 
    print("No solution")
