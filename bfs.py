from queue import Queue
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
def bfs(graph, start_node, end_node):
  q = Queue()
  path = []
  if start_node in graph:
    q.put(start_node)
    while q.empty()==False:
      visit = q.get()
      path.append(visit)
      if path[-1] != end_node:
        eles = ret_value(visit)
        if eles != None:
          for i in eles:
            if i not in path:
              q.put(i)
      else:
        break
  path = list(dict.fromkeys(path))
  print('\nbfs path = ', path)

start_node = 'A'
end_node = 'N'
bfs(graph, start_node, end_node)

'''BFS (G, s)
let Q be queue.
Q.enqueue( s )
 
mark s as visited
while ( Q is not empty)
v = Q.dequeue( )
 
for all neighbors w of v in Graph G
if w is not visited
Q.enqueue( w )
mark w as visited


Completeness : It is complete, provided the shallowest goal node is at some finite depth.
 Optimality : It is optimal, as it always finds the shallowest solution.
 Time complexity : O(bd
), number of nodes in the fringe.
 Space complexity : O(bd), total number of nodes explored.'''
