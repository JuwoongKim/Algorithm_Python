from collections import deque

INF=99999

Graph = [
        [0,1,1,INF,INF,INF,INF,1],
        [1,0,INF,INF,INF,INF,1,INF],
        [1,INF,0,1,1,INF,INF,INF],
        [INF,INF,1,0,1,INF,INF,INF],
        [INF,INF,1,1,0,INF,INF,INF],
        [INF,INF,INF,INF,INF,0,1,INF],
        [INF,1,INF,INF,INF,1,0,1],
        [1,INF,INF,INF,INF,INF,1,0]
        ]

Deque = deque()

Invited = [False]*8

result= []


def BFS(graph, number, Invited):
        
        result.append(number)
        Deque.append(number)

        while Deque:
                number =Deque.popleft()
                Invited[number]=True
                for idx, ele in enumerate(graph[number]):
                        
                        if Invited[idx]==True:
                                continue
                        else:
                                if ele==1:
                                        Deque.append(idx)
                                        result.append(idx)
                                        Invited[idx]=True     
        return

BFS(Graph, 0, Invited)
print(result)