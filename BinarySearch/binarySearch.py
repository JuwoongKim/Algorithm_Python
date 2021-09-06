# 재귀로 구현한 이진탐색 알고리즘 


def binarySearch(arr, target, start, end):
    
    if start >= end:
        return None

    mid = (start + end)//2

    if arr[mid] == target:
        return mid

    #target이 중간값보다 큰 위치에 있을때 
    elif arr[mid] <target:
        start = mid + 1
        return binarySearch(arr, target, start, end)

    #target이 중간값보다 직은 위치에 있을때     
    else :
        end = mid -1
        return binarySearch(arr, target, start, end)

test_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

target =4 

result_idx = binarySearch(test_list, target, 0, len(test_list)-1)

print("해당 target은 ", result_idx, " 번째에 존재합니다")