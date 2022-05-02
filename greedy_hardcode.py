graph={
    'S' : [('A', 19), ('B', 8), ('C', 7)],
    'A' : [('D', 6), ('B', 8)],
    'B' : [('D', 6), ('H', 7)],
    'C' : [('L', 6)],
    'D' : [('F', 4)],
    'H' : [('G', 3)],
    'L' : [('J', 9), ('I', 9)],
    'F' : [('G', 3)],
    'G' : [('E', 0)],
    'I' : [('K', 4)],
    'J' : [('K', 4)],
    'K' : [('E', 0)]    
}

start = input("Enter the start node : ")
end = input("Enter the end node : ")

def ret_value(k, var1, var = None):
    for key, value in var1.items():
        if var == None and key==k:
            return value
        if var == 'val' and value==k:
          return key
closed, opened = [], []
def greedy(closed, opened, start, end):
    N = start
    opened += ret_value(N, graph)
    opened.sort(key = lambda x: x[1])
    var = int(input(f"Enter the hierustic for {start} node : "))
    N = (start,var)
    newnode = opened[0]
    closed = [N]
    print("Path = ", N)
    while (len(opened)>0) and (closed[-1][0] != end):
        opened += ret_value(N[0], graph)
        opened = list(dict.fromkeys(opened))
        opened.sort(key = lambda x: x[1])
        print("open = ", opened)
        newnode = opened.pop(0)
        N=newnode
        print("\nnext visit = ", N)
        if N not in closed:
            closed.append(N)
        print("Path = ", closed)
    return closed
closed = greedy(closed, opened, start, end)

'''1. Completeness : It’s not complete as, it can get stuck in loops, also is susceptible to wrong start and quality of heuristic
function.
2. Optimality : It’s not optimal; as it goes on selecting a single path and never checks for other possibilities.
3. Time Complexity : O(bm
), but a good heuristic can give dramatic improvement.
4. Space Complexity : O(bm
) , It needs to keep all nodes in memory'''
