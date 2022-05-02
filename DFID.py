def ret_value(k, var1, var = None):
    for key, value in var1.items():
        if var == None and key==k:
            return value
        if var == 'val' and value==k:
          return key
    
graph = {
    'A' : ['B', 'C',  'D'],#1
    'C' : ['E', 'F'],#2
    'G': ['H', 'J', 'I'],#3
    'K' : [None],#4
    'I' : ['K'],#5
    'B' : ['D'],#6
    'D' : ['L'],#7
    'L' : ['A', 'M'],#8
    'O' : ['N'],#9
    'N' : ['T', 'H', 'Q'],#10
    'H' : ['E'],#11
    'P' : ['O'],#12
    'Q' : ['H'],#13
    'R' : ['Q'],#14
    'S' : ['R'],#15
    'J' : ['S'],#16
    'U' : ['A', 'N', 'H'],#17
    'T' : ['A', 'B'],#18
    'E' : ['U', 'G'],#19
    'F' : ['G', 'M'],#20
    'M' : ['J', 'I'],#21
}

max_depth = int(input("\nEnter the maximum travesal depth : "))
start_node = input("Enter start node: ")
destn_node = input("Enter destination node: ")
path = []
def DFS(currentNode,destination,graph,maxDepth,curList):
    print("\n----- Next Iteration -----")
    print("Searching destination",currentNode)
    curList.append(currentNode)
    print(f"Path: {curList}")
    print("Queue: ", ret_value(curList[-1], graph))
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    open_list = list(graph.keys())
    closed_list = []
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,graph,i,curList):
            return True
    return False

if not iterativeDDFS(start_node, destn_node, graph, max_depth):
    print("\nPath unavailable!")
else:
    print("\nA path exists!")
'''
DFID() 
{ 
limit = 0; 
found = false; 
while (not found) 
 { 
found = DLS(root, limit, 0); 
limit = limit + 1; 
 } 
}

 Completeness : DFID is complete when the branching factor b is finite.
 Optimality : It is optimal when the path cost is a non-decreasing function of the depth of the node.
 Time complexity :
o Do you think in DFID there is a lot of wastage of time and memory in regenerating the same set of nodes again
and again ?
o It may appear to be waste of memory and time, but it’s not so. The reason is that, in a search tree with almost
same branching factor at each level, most of the nodes are in the bottom level which are explores very few times
as compared to those on upper level.
o The nodes on the bottom level that is level ‘d’ are generated only once, those on the next to bottom level are
generated twice, and so on, up to the children of the root, which are generated d times. Hence the time
complexity is O(bd
).
 Space complexity : Memory requirements of DFID are modest, i.e. O(bd
)
'''
