#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Describe your graph here  
graph = {}

print("""INPUT INSTRUCTIONS
1. Enter the graph as parent node and its children separated by spaces 
(the first letter will be considered as the parent followed by the class("None" in case of a leaf node)):
2. Enter the dist of each child node with the parent node separated by spaces: \n""")
while True:
    seq = input().split()
    
    if seq == ['-1']:
        break
        
    dist = list(map(int, input(("Distance of " + f'{seq[1:]}' + " from " + f'{seq[0]}' + ": ")).split()))
    
    if len(seq[1:]) == len(dist):
            edge = [[seq[x+1], dist[x]] for x in range(len(dist))]    
    else:
        print("Invalid Input!")
        break
        
    graph[seq[0]] = edge


# In[ ]:


start = 'S'
Closed = list()

def MOVEGEN(N):
    new_list = list()
    if N in graph.keys():
        new_list = graph[N]
    return new_list

def SORT(L):
    L.sort(key = lambda x: x[1])
    return L

def heu(Node):
    return Node[1]

def APPEND(L1,L2):
    new_list = list(L1) + list(L2)
    return new_list

def Hill_Climbing(start):
    global closed
    N = start
    child = MOVEGEN(N)
    SORT(child)
    N = [start,100]
    print("\nStart: ",N)
    print("Edges: ",child)
    newnode = child[0]
    closed = [N]

    while heu(newnode)<=heu(N):
        print('\n------------------')
        N=newnode
        print('Next visited node = ',N)
        closed = APPEND(closed,[N])
        child = MOVEGEN(N[0])
        SORT(child)
        print("Edges = ", child)
        newnode = child[0]
    Closed = closed
    

Hill_Climbing(start)


# In[ ]:




