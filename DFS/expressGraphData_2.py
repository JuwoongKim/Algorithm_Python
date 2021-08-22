'''
데이터는 다양한 자료구조를 통해서 저장된다.
DFS는 이러한 자료구조로 부터 데이터를 탐색하는 방법중 하나이다.

이번 코드에서는 그래프 자료구를 통해서 데이터를 표현하고 
이러한 데이터터를  DFS 알고리즘을 통해서 순차적으로 탐색하는 것을 목표로 한다.

그래프 자료구조는 <이것이 코딩테스트다>에서 첨부한 그래프 이미지를 활용하며  
이를 배열에 의한 표현, 리스트에 의한 표현 총 2가지 방식으로 구조화한다.
이번 코드에서는 리스트에의한 표현을 통해서 진행한다.
그래프는 리스트 통해서 나타낼 수 있다.  
'''

# graph by linked list + no weight 
# 그래프간 가중치가 없기때문에 탐색시 작은 노드 번호를 우선순위로 한다.
graph =[[] for _ in range(8)]

graph[0].append([1,1])
graph[0].append([2,2])
graph[0].append([7,7])

graph[1].append([0,0])
graph[1].append([6,6])

graph[2].append([0,0])
graph[2].append([3,3])
graph[2].append([4,4])

graph[3].append([2,2])
graph[3].append([4,4])

graph[4].append([2,2])
graph[4].append([3,3])

graph[5].append([6,6])

graph[6].append([1,1])
graph[6].append([5,5])
graph[6].append([7,7])

graph[7].append([0,0])
graph[7].append([6,6])


result =[]
stack = []


def DFS(number):

    result.append(number)
    stack.append(number)

    for ele in graph[number]:

        if ele[0] in result:
            ele[1] =-1
            continue

        else:
            ele[1] = -1
            DFS(ele[0])
        
    stack.pop()
    return

DFS(0)
print(result)








