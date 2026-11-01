def solve(board, row): 
    if row == 8: 
        return True 
 
    for col in range(8): 
        if all(board[i] != col and 
               abs(board[i] - col) != abs(i - row) 
               for i in range(row)): 
 
            board[row] = col 
 
            if solve(board, row + 1): 
                return True 
 
            board[row] = -1 
 
    return False 
 
 
board = [-1] * 8 
 
if solve(board, 0): 
    for row in range(8): 
        print(" ".join("Q" if board[row] == col else "." 
                       for col in range(8))) 
else: 
    print("No solution found")
