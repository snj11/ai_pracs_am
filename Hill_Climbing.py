graph={
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
start = input("Enter the start node : ")
def ret_value(k, var1):
    for key, value in var1.items():
        if key==k:
            return value
    

def Hill_Climbing(start):
    closed = [start]
    child = ret_value(start, graph)
    child.sort(key = lambda x: x[1])
    var = int(input(f"Enter the hierustic for {start} node : "))
    print("\nStart: ",start)
    print("Edges: ",child)
    newnode = child[0]
    closed = [start,var]
    N = [start,var]

    while newnode[1]<=N[1]:
        print('\n------------------')
        N=newnode
        print('Next visited node = ',N)
        closed += [N]
        child = ret_value(N[0], graph)
        child.sort(key = lambda x: x[1])
        print("Edges = ", child)
        newnode = child[0]

Hill_Climbing(start)
