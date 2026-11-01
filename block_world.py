def blocks_world(blocks, goal): 
    stack = blocks[:] 
    print("Initial State:", stack) 
 
    for block in goal: 
        if block in stack: 
            stack.remove(block) 
        stack.append(block) 
        print("Move", block, "to top:", stack) 
 
    print("Goal State:", stack) 
 
 
blocks = input("Enter initial blocks (e.g. ABC): ").upper() 
goal = input("Enter goal order (e.g. CBA): ").upper() 
 
blocks_world(list(blocks), list(goal)) 
