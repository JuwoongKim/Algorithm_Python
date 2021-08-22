# 해당 자료는 자료의 솔루션으로 나온 내용입니다,
# 해당 코드를 바탕으로  외워서 사용할 것 

def DFS(graph, number, visited):

    visited[number] =True
    print(number, end=' ')
    for ele in graph[number]:
        
        if not visited[ele]:
            DFS(graph, ele, visited)
    return

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

visited =[False]*8

DFS(graph,1, visited)

