


from typing_extensions import runtime_checkable


def test(arr):

    i =0

    while i<3:
        print(arr)
        temp = arr[1]
        arr[1]= arr[2]
        arr[2]= temp
        i +=1
    return arr


t = [1,2,3,4]
r = test(t)

print(r)