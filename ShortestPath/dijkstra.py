
def makeGraph(graph, lines):
    for i in lines:
        start, end, cost = list(map(int, i.split()))
        graph[start].append((end, cost))

def findMin(cost,visited):

    min_n =-1
    min_v =INF

    for i,v in enumerate(cost):
        if visited[i] ==True:
            continue
        else:
            if v < min_v:
                min_n=i
                min_v = v
    
    return min_n

def dijkstra(graph, visited, cost, start):
    
    min_n = start

    # cost 자료구조 갱신 
    while False in visited :
        for ele in graph[min_n]:
            n, v = ele[0], ele[1]
            cost[n] = min(cost[n],cost[min_n]+v)

        min_n = findMin(cost, visited)
        visited[min_n]= True 

        print(cost)
        print(visited)
        print(min_n)


    '''

    0. graph 자료구조를 바탕으로 cost 자료구조를 갱신함 

        for ele in graph[min_n]:
            n = ele[0]
            v = [ele[1]]
            cost[n] = min(cost[n], cost[min_n]+v )

  
    1. 현재 cost 자료구조에서 가장  비용이 작은 노드를 선택 

    2. 해당 cost 값 갱신 

    3. 방문처리 갱신 

    2. 기존 cost 값과 선택한 노드를 반영한 것과 비교  
    
    '''


f = open("data_for_dijkstra.txt", 'r')

n, m = map(int, f.readline().split())
start = int(f.readline())
lines = f.readlines()

# 그래프는 미리 다 만들어주고 index로 찾아서 추가하자 
INF=999999
graph = [[] for _ in range(7)]
visited =[ False for _ in range(7)]
cost = [INF for _ in range(7)]
visited[0]= True
visited[start]= True
cost[start]= 0

makeGraph(graph, lines)
dijkstra(graph, visited, cost, start)


f.close()