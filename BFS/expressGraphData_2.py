'''
만약 그래프이 가중치를 표현한다면 ??? 

동작하지 않는 프로그램 
'''


from collections import deque

graph =[[] for _ in range(8)]

graph[0].append((1,1))
graph[0].append((2,2))
graph[0].append((7,7))

graph[1].append((0,0))
graph[1].append((6,6))

graph[2].append((0,0))
graph[2].append((3,3))
graph[2].append((4,4))

graph[3].append((2,2))
graph[3].append((4,4))

graph[4].append((2,2))
graph[4].append((3,3))

graph[5].append((6,6))

graph[6].append((1,1))
graph[6].append((5,5))
graph[6].append((7,7))

graph[7].append((0,0))
graph[7].append((6,6))



Deque= deque()
result=[]
Invited=[False]*8

def BFS(graph, number, Invited):

    result.append(number)
    Deque.append(number)

    while Deque:
        number = Deque.leftpop()
        Invited[number]=True

        for ele in graph[number]:

            if Invited[ele] ==True:
                continue
            else:
                Deque.append(ele)
                result.append(ele)

    
    return 

BFS(graph,0,Invited)
print(result)

