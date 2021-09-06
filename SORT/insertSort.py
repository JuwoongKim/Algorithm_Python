
# 삽입정렬 

'''
두번째 원소부터 그이전의 원소들과 비교를 한다는 점에서 bubble 정렬과  공통점이있다.
그러나 버블정렬은  이전연산과 비교할때마다 옮기지만 
파이썬 내장함수로 구현한 삽입정렬은, 비교할떄마다 값을 실제로 바꾸지 않고 
해당 부분의 인덱스를 통해서 특정지점에서 1번만 교환을 한다 
'''


import random 
test_list = [i for i in range(11)]
random.shuffle(test_list)

# 내장함수를 통한 구현 
def insertSort(_list):
    
    length = len(_list)

<<<<<<< HEAD
    for idx in range(1,length):

        for idx2 in range(idx-1, -1, -1):
            
            if _list[idx] > _list[idx2] or idx2==0: # 삽입대상이 되는 원소가 더이상 작지 않다면 해당 인덳스를 삭제하고 삽입함  
                obj = _list[idx]
                del _list[idx]
                _list.insert(idx2+1,obj) 
                break
        
    return _list
=======
    for idx in range(length-1):
        



>>>>>>> 0ff3ecdefdfc39c5723fadd88878b4b4c208a55a

print(test_list)
result = insertSort(test_list)
print(result)