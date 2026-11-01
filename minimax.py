def minimax(b, player): 
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6), 
            (1,4,7),(2,5,8),(0,4,8),(2,4,6)] 
 
    for a,c,d in wins: 
        if b[a] == b[c] == b[d] != " ": 
            return 1 if b[a] == "O" else -1 
 
    if " " not in b: 
        return 0 
 
    scores = [] 
    for i in range(9): 
        if b[i] == " ": 
            b[i] = player 
            scores.append(minimax(b, "X" if player == "O" else "O")) 
            b[i] = " " 
 
    return (max if player == "O" else min)(scores) 
 
 
b = [" "] * 9 
while " " in b: 
    print(b[:3], b[3:6], b[6:]) 
    i = int(input("Your move (1-9): ")) - 1 
    if i not in range(9) or b[i] != " ": 
        print("Invalid move!") 
        continue 
    b[i] = "X" 
 
    if minimax(b, "O") == -1: 
        print("You win!") 
        break 
 
    if " " not in b: 
        print("Draw!") 
        break 
 
    moves = [] 
    for j in range(9): 
        if b[j] == " ": 
            b[j] = "O" 
            moves.append((minimax(b, "X"), j)) 
            b[j] = " " 
    b[max(moves)[1]] = "O"
