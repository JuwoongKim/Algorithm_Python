

def makeGraph ( n, v, info):

    graph = [[INF]*(n+1) for _ in range(n+1)]

    for ele in info:
        temp= list(map(int,ele.split()))
        start, end, v = list(map(int, ele.split()))
        graph[start][end] = v

    for i in range(1, n):
        graph[i][i] = 0

    return graph

def floyd(graph):

    n = len(graph)

    # i번째 노드를 거쳐지나가는것과  그렇지 않은 것을 비교해야함 
    for i in range(1,n):
        for row in range(1,n):
            if row ==i:
                continue
            else:
                for col in range(1,n):
                    if col == i:
                        continue
                    else:
                        graph[row][col]=min(graph[row][col], graph[row][i]+ graph[i][col])
                
    return graph


def PrintGraph(graph):

    for i in graph:
        print(i)


INF =99999

f= open("data_for_floyd.txt", 'r')
n,v= int(f.readline()), int(f.readline())
info = f.readlines()

graph = makeGraph(n,v,info)
print("이전")
PrintGraph(graph)

print()
print("이후")
result_graph =floyd(graph)
PrintGraph(result_graph)








f.close()