'''
순차 정렬 ( =가장 기본이 되는 정렬)

'''

import random


# 테스트를 위해  임의의  숫자배열을 생성한다  범위는 0~10까지의 범위로 한다

test_list= [i for i in range(11)]
random.shuffle(test_list)


# 파이썬의 내장함수 min(), index()  사용해서 구현하기  
'''
def SequentialSort(_list):

    length=len(_list)

    for idx in range(length-1):
        
        min_value = min(_list[idx+1:length])
        
        min_idx= _list.index(min_value)
        
        if min_value < _list[idx]:
            _list[min_idx] = _list[idx]
            _list[idx] = min_value

    return _list
'''

# 내장함수 사용하기 않고 직접 구현하기 

'''
def  SequentialSort(_list):

    lenght = len(_list)

    for idx in range((lenght-1)):

        min_value = 99999
        min_idx =99999
        for idx2 in range(idx+1, lenght):

            if _list[idx2] < min_value:
                min_value=_list[idx2]
                min_idx=idx2

        temp = _list[idx]        
        if min_value <temp:        
            _list[idx]= min_value
            _list[min_idx] =temp

    return _list
'''


# 위의 과정중 첫번째 원소를 빼고 구분한다는 것이 불필요한 과정이라고 생각하고 전체적으로 비교해봄  (이게 맞음 )

def  SequentialSort(_list):
    lenght = len(_list)

    for idx in range(lenght):
        min_value = min(_list[idx:lenght])
        min_index = _list.index(min_value)

        temp = _list[idx]
        _list[idx] = min_value
        _list[min_index]=temp 
    
    return _list


print(test_list)
result = SequentialSort(test_list)
print(result)

