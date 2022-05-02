from queue import LifoQueue

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

def ret_value(k):
    for key, value in graph.items():
        if key==k:
            return value

def dfs(graph, start_node, end_node):
  stack = LifoQueue()
  path = []
  if start_node in graph:
    stack.put(start_node)
    while stack.empty()==False:
      visit = stack.get()
      path.append(visit)
      if path[-1] != end_node:
        eles = ret_value(visit)
        eles.reverse()
        if eles != None:
          for i in eles:
            if i not in path:
              stack.put(i)
      else:
        break
  path = list(dict.fromkeys(path))
  print('\ndfs path = ', path)
start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")
dfs(graph, start_node, end_node)

'''DFS(G, s, key):
      stack = new Stack()
      stack.push( s )            //Push s to stack 
      mark s as visited
      while ( stack is not empty):
            //Pop node from stack and start to visit its children
            v  =  stack.pop()
            
            if(v == key) return true //We found the key
            
            //Push all the unvisited neighbours of v to stack 
            for all neighbours w of v in Graph G:
                //unvisited neighbors
                if w is not visited :   
                     stack.push( w )         
                     mark w as visited
      return false
      
Completeness : Complete, if m is finite.
 Optimality : No, as it cannot guarantee the shallowest solution.
 Time Complexity : A depth first search, may generate all of the O(bm) nodes in the search tree, where m is the
maximum depth of any node; this can be much greater than the size of the state space.
 Space Complexity : For a search tree with branching factor b and maximum depth m, depth first search requires
storage of only O(bm
) nodes, as at a time only the branch, which is getting explored, will reside in memory'''
