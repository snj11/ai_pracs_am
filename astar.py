def aStarAlgo(start_node, stop_node):
        open_set = set(start_node)
        closed_set = set()
        g = {} # store distance from starting node
        parents = {} # parents contains an adjacency map of all nodes
 
        # distance of starting node from itself is zero
        g[start_node] = 0
        # start node is root node i.e it has no parent nodes
        # so start node is set to its own parent node
        parents[start_node] = start_node
        
        while len(open_set) > 0:
            n = None
            # node with lowest f() is found
            for v in open_set:
              if n == None or (g[v] + heuristic[v] < g[n] + heuristic[n]):
                  n = v
                     
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    # nodes 'm' not in first and last set are added to first
                    # n is set its parent
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n
                             
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
            if n == None:
                print('Path does not exist!')
                return None
            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()
                print("\nPath exists!")
                return path
 
            open_set.remove(n)
            closed_set.add(n)
        print('Path does not exist!')
        return None
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

Graph_nodes={
    'A' : [('B',37), ('C',10),  ('D', 30)],#1
    'C' : [('E', 35), ('F', 25)],#2
    'G': [('H', 29), ('J', 33), ('I', 11)],#3
    'K' : [None],#4
    'I' : [('K', 60)],#5
    'B' : [('D', 7)],#6
    'D' : [('L', 15)],#7
    'L' : [('A', 10), ('M', 39)],#8
    'O' : [('N', 47)],#9
    'N' : [('T', 50), ('H', 55), ('Q', 35)],#10
    'H' : [('E', 40)],#11
    'P' : [('O', 20)],#12
    'Q' : [('H', 31)],#13
    'R' : [('Q', 27)],#14
    'S' : [('R', 39)],#15
    'J' : [('S', 70)],#16
    'U' : [('A', 50), ('N', 20), ('H', 19)],#17
    'T' : [('A', 40), ('B', 15)],#18
    'E' : [('U', 21), ('G', 32)],#19
    'F' : [('G', 60), ('M', 17)],#20
    'M' : [('J', 15), ('I', 16)],#21
}

keys = []
for key in Graph_nodes:
    keys.append(key)

heuristic = {
             'A' : 81,
             'C' : 74,
             'G' : 30,
             'K' : 42,
             'I' : 47,
             'B' : 50,
             'D' : 100,
             'L' : 90,
             'O' : 41,
             'N' : 0,
             'H' : 19,
             'P' : 46,
             'Q' : 31,
             'R' : 46,
             'S' : 49,
             'J' : 64,
             'U' : 20,
             'T' : 57,
             'E' : 51,
             'F' : 63,
             'M' : 72,
         }

        
start_node = "A"
destn_node = "N"
path = aStarAlgo(start_node, destn_node)
cost = 0
for i in range(len(path)-1):
  neighbors = get_neighbors(path[i])
  if neighbors:
    for j in neighbors:
      if j[0] == path[i+1]:
        cost += j[1]
print("Path = ", path)
print('Cost = ', cost)

'''let openList equal empty list of nodes
let closedList equal empty list of nodes
put startNode on the openList (leave it's f at zero)
while openList is not empty
    let currentNode equal the node with the least f value
    remove currentNode from the openList
    add currentNode to the closedList
    if currentNode is the goal
        You've found the exit!
    let children of the currentNode equal the adjacent nodes
    for each child in the children
        if child is in the closedList
            continue to beginning of for loop
        child.g = currentNode.g + distance b/w child and current
        child.h = distance from child to end
        child.f = child.g + child.h
        if child.position is in the openList's nodes positions
            if child.g is higher than the openList node's g
                continue to beginning of for loop
        add the child to the openList'''
