#!/usr/bin/env python
# coding: utf-8

# In[10]:


def ret_value(k, var1, var = None):
    for key, value in var1.items():
        if var == None and key==k:
            return value
        if var == 'val' and value==k:
          return key


# In[11]:


graph = {}

print("""INPUT INSTRUCTIONS
1. Enter the graph as parent node and its children separated by spaces 
(the first letter will be considered as the parent followed by the class("None" in case of a leaf node)):
2. Enter the dist of each child node with the parent node separated by spaces: \n""")
while True:
    seq = input().split()
    
    if seq == ['-1']:
        break
        
    edge = [seq[x+1] for x in range(len(seq)-1)]
        
    graph[seq[0]] = edge


max_depth = int(input("\nEnter the maximum travesal depth : "))
start_node = input("Enter start node: ")
destn_node = input("Enter destination node: ")

path = list()


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

