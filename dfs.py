#!/usr/bin/env python
# coding: utf-8

# In[1]:


from queue import Queue
from queue import LifoQueue


# In[ ]:


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


# In[3]:


def ret_value(k):
    for key, value in graph.items():
        if key==k:
            return value


# In[4]:


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


# In[5]:


start_node = input("Enter the starting node")
end_node = input("Enter the ending node")
dfs(graph, start_node, end_node)

