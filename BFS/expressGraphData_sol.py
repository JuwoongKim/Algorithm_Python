from collections import deque

graph=[
    [1,2,7],
    [0,6,7],
    [0,3,4],
    [2,4],
    [2,3],
    [6,7],
    [1,5,7],
    [0,6]
        ]


Deque= deque()
result=[]
Invited=[False]*8

def BFS(graph, number, Invited):

    result.append(number)
    Deque.append(number)

    while Deque:
        number = Deque.popleft()
        Invited[number]=True

        for ele in graph[number]:

            if Invited[ele] ==True:
                continue
            else:
                Deque.append(ele)
                result.append(ele)
                Invited[ele]=True
    return 

BFS(graph,0,Invited)
print(result)
