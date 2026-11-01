 
import heapq 
 
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0) 
 
def h(s): 
    return sum(abs(i//3 - (x-1)//3) + abs(i%3 - (x-1)%3) 
               for i, x in enumerate(s) if x) 
 
def astar(start): 
    pq = [(h(start), 0, start, [])] 
    visited = set() 
 
    while pq: 
        f, g, s, path = heapq.heappop(pq) 
        if s in visited: 
            continue 
        visited.add(s) 
        path = path + [s] 
 
        if s == goal: 
            for p in path: 
                print(p[:3], p[3:6], p[6:]) 
            print("Moves:", len(path) - 1) 
            return 
 
        z = s.index(0) 
        for d in (-3, 3, -1, 1): 
            n = z + d 
            if 0 <= n < 9 and not ( 
                d == -1 and z % 3 == 0 or 
                d == 1 and z % 3 == 2 
            ): 
                t = list(s) 
                t[z], t[n] = t[n], t[z] 
                t = tuple(t) 
                if t not in visited: 
                    heapq.heappush(pq, (g + 1 + h(t), g + 1, t, path)) 
 
start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split())) 
astar(start)
