'''
피보나치 수열을  DP 문제로 풀었을때는 비교의 과정이 없엇다. 이는 최적화 과정없이 정답이 정해져있기때문이다  

그러나 실제로  DP문제는 최적화 문제와 같이 연관되어서 사용된다.

기존 피보나치 문제와의 차이점은 값의 비교가  추가된다는 것이다.

'''



# top down 방식으로 풀어보기  

Num = int(input())
INF=99999
count_memo=[INF]*(Num+1)

'''
def func(_num, _count):

    num = _num
    count =_count

    if count <= count_memo[num]:
        count_memo[num]=count
    else:
        return         

    if num%5==0:
        func(num//5, count+1)
    
    if num%3==0:
        func(num//3, count+1)

    if num%2==0:
        func(num//2, count+1)

    if num-1>0 :
        func(num-1,count+1)
'''

# bottom up 방식으로 풀어보기  
'''
def func2(num):

    count_memo[1]=0    
    for i in range(2, num+1):
        print(i)
        count_list=[]

        if i%5==0:
            count_list.append(count_memo[i//5]+1)
    
        if i%3==0:
            count_list.append(count_memo[i//3]+1)

        if i%2==0:
            count_list.append(count_memo[i//2]+1)

        if i-1>0:
            count_list.append(count_memo[i-1]+1)

        result = min(count_list)
        count_memo[i] =result

    return count_memo[num]

'''

# 해설대로 풀기  : 좀더 직관적이고 깔끔함 





# 결과표 
#func (Num,0)
print(func2(Num))
#print(count_memo[1])
print(count_memo)


