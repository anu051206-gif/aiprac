def dfs(a, b, target, visited): 
    if (a, b) in visited: 
        return False 
 
    visited.add((a, b)) 
    print(a, b) 
 
    if a == target or b == target: 
        return True 
 
    states = [ 
        (5, b), (a, 3), (0, b), (a, 0), 
        (a - min(a, 3 - b), b + min(a, 3 - b)), 
        (a + min(b, 5 - a), b - min(b, 5 - a)) 
    ] 
 
    for x, y in states: 
        if dfs(x, y, target, visited): 
            return True 
 
    return False 
 
 
print("Jug capacities: 5L and 3L") 
target = int(input("Enter target amount: ")) 
if not dfs(0, 0, target, set()): 
    print("Solution not found")
