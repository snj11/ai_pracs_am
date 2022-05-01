graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['G', 'H'],
    'F' : ['I', 'J'],
    'J' : ['K'],
    'H' : ['L']
}

def DLS(start,goal,path,level,maxD):
  #print('\nCurrent level-->',level)
  #print('Goal node testing for',start)
  path.append(start)
  if start == goal:
    return path
  #print('Goal node testing failed')
  if level==maxD:
    return False
  #print('\nExpanding the current node',start)
  for child in graph[start]:
    if DLS(child,goal,path,level+1,maxD):
      return path
    path.pop()
  return False

start = 'A'
goal = input('Enter the goal node:-')
maxD = int(input("Enter the maximum depth limit:-"))
print()
path = list()
res = DLS(start,goal,path,0,maxD)
if(res):
    print("Path found!!")
    print("Path = ",path)
else:
    print("No path available for the goal node in given depth limit")

'''function DEPTH-LIMITED-SEARCH(problem, limit) returns a solution, or failure/cutoff
    return RECURSIVE-DLS(MAKE-NODE(problem. INITIAL-STATE), problem, limit)

function RECURSIVE-DLS(node, problem, limit) returns a solution, or failure/cutoff 
    if problem.GOAL-TEST(node.STATE) then return SOLUTION(node) 
    else if limit=0 then return cutoff
    else 
        cutoff-occurred? - false

        for each action in problem.ACTIONS(node.STATE) do 
            child CHILD-NODE(problem, node, action) 
            result RECURSIVE-DLS(child, problem, limit - 1) 
            if result = cutoff then cutoff_occurred? - true
            else if result failure then return result
        if cutoff occurred? then return cutoff else return failure'''
