#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:


def ret_value(k):
    for key, value in graph.items():
        if key==k:
            return value


# In[ ]:


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


# In[ ]:


start_node = 'Amravati'
end_node = 'Mumbai'
bfs(graph, start_node, end_node)

