'''
데이터는 다양한 자료구조를 통해서 저장된다.
DFS는 이러한 자료구조로 부터 데이터를 탐색하는 방법중 하나이다.

이번 코드에서는 그래프 자료구를 통해서 데이터를 표현하고 
이러한 데이터터를  DFS 알고리즘을 통해서 순차적으로 탐색하는 것을 목표로 한다.

그래프 자료구조는 <이것이 코딩테스트다>에서 첨부한 그래프 이미지를 활용하며  
이를 배열에 의한 표현, 리스트에 의한 표현 총 2가지 방식으로 구조화한다.
이번 코드에서는 배열에의한 표현을 통해서 진행한다.
그래프는 2차원 배열을 통해서 나타낼 수 있다.  
'''

# graph by 2d array  + no weight
# 그래프간 가중치가 없기때문에 탐색시 작은 노드 번호를 우선순위로 한다.
# 0 => 자기자신,  1=> 연결됨 , INF=99999 => 연결안됨 , invite = -1 => 순회시 방문표시 
# 2차원 배열의 행과 열들의 원소는 노드 번호를 의미하며 이들의 교차점은 연결여부를 나타낸다.
# 예를 들어  graph[1][2] =1 일 경우  1번노드와 2번노드는 서로 연결되어있음을 의미한다. 

INF=99999
Invited =-1

graph = [
        [0,1,1,INF,INF,INF,INF,1],
        [1,0,INF,INF,INF,INF,1,INF],
        [1,INF,0,1,1,INF,INF,INF],
        [INF,INF,1,0,1,INF,INF,INF],
        [INF,INF,1,1,0,INF,INF,INF],
        [INF,INF,INF,INF,INF,0,1,INF],
        [INF,1,INF,INF,INF,1,0,1],
        [1,INF,INF,INF,INF,INF,1,0]
        ]

stack = []
result= []

# DFS function 1 
# function 1에서는 그래프가 전역변수여서 인자값없이 접근이 가능함을 의미한다.
# issue => 만약 전역변수가 아닌상태에서 그래프 탐색을 해야한다면? 
# 탐색은 가장 작은 노드번호인  1번 부터 시작한다. (우선순위 기준이 작은 노드번호이기때문)
# issue => 만약 기준이 달라진다면?? 또는 노드번호가 아닌 다른 정보만 존재한다면??

def DFS(number):
    # 모듈 1 : 방문처리 및 스택처리
      
    stack.append(number)
    result.append(number)
    print('the stack append: ', stack)  
    for i in range(len(graph[1])):
        ele = graph[i][number] 
        
        if ele ==1 or ele ==0:
            graph[i][number]= Invited
        else:
            continue
        
    # 모듈 3 : 인접노드 탐색 및 결정

    for i in range(len(graph[1])):
        ele = graph[number][i]

        if ele == 1 :
            DFS(i) 
        else : 
            continue

    poped = stack.pop()
    print("the stack pop : ", poped)
    return


DFS(0)

invite_order = result
print(invite_order)   





# graph by linked list + no weight 
# 그래프간 가중치가 없기때문에 탐색시 작은 노드 번호를 우선순위로 한다.

