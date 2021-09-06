


def sequentialSearch(arr, target):

    for i ,v in enumerate(arr):
        if v == target:
            return i

    print("존재하지 않습니다")
    

input_arr= input("입력할 문자열의 갯수와 공백키를 누르고 찾을 문자열을 입력하세요 ").split()

num_of_str = int(input_arr[0])
target = input_arr[1]

str_arr = input("공백을 기준으로 문자를 입력해주세요 ").split()

print(str_arr)

target_idx = sequentialSearch(str_arr, target)

print(" 행당문자열 ", str_arr[target_idx], "은  ", target_idx," 번째에 존재합니다")



