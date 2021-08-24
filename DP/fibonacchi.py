

# 피보나치 수열구하기  with  단순 재귀  


'''
def Fibo(num):

    if num ==0:
        return 0
    elif num ==1:
        return 1
    else:
        return Fibo(num-1)+Fibo(num-2)

'''

# 피보나치 수열구하기  with  DP  topdown

NUM=10
GARBAGE=-1
memo=[GARBAGE]*NUM

'''
def Fibo(num):

    if memo[num]!=GARBAGE:
        return memo[num]

    else:
        if num ==0:
            memo[num]=0
            return 0
        elif num ==1:
            memo[num]=1
            return 1

        else:
            result = Fibo(num-1)+Fibo(num-2)
            memo[num] =result
            return result
'''     

# 피보나치 수열구하기  with  DP  topdown    (sol)


# 피보나치 수열구하기  with  DP  topdown


def Fibo(num):

    for i in range(num+1):

        if i==0:
            memo[0]=0
        elif i ==1:
            memo[1] =1
        else:
            memo[i]= memo[i-1]+memo[i-2]

    return memo[num]


# 결과표 

Sequence_list=[]

for i in range(NUM):
    Sequence_list.append(Fibo(i))

print(Sequence_list)
print(memo)

