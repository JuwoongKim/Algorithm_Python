'''
this is for mergesort 
'''

import random

test_list= [i for i in range(11)]
random.shuffle(test_list)


# 파이썬 내장함수  sort와  merge
# 그러나 이미 내장된 sort 함수를 사용하면 무슨의미가 있겠니~~
'''
def merge(arr1,arr2):
    merge_arr=arr1+ arr2
    merge_arr.sort()
    return merge_arr
'''

# 직접구현 
def merge(arr1, arr2):

    merge_arr=[]
    len1 = len(arr1)
    idx1 =0
    len2 = len(arr2)
    idx2 =0

    while idx1 != len1 or idx2 != len2:

        if idx1==len1:
            merge_arr.append(arr2[idx2])
            idx2 +=1
            continue

        if idx2==len2:
            merge_arr.append(arr1[idx1])
            idx1 +=1
            continue

        if arr1[idx1] < arr2[idx2]:
            merge_arr.append(arr1[idx1])
            idx1 +=1
            continue
        else:
            merge_arr.append(arr2[idx2])
            idx2 +=1

    return merge_arr


def mergeSort (_min, _max, arr ):

    if _min == _max:
        result= [ arr[_min] ]
        return  result

    else:
        mid = (_min+_max)//2

        first =mergeSort(_min,mid, arr)
        second =mergeSort(mid+1, _max, arr)

        result = merge(first, second)
        return result

min_index = 0
max_index = len(test_list)-1

result = mergeSort(min_index, max_index, test_list)
print(test_list)
print(result)