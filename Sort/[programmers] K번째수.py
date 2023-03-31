def solution(array, commands):
    answer = []
    for index in commands:
        i = index[0]
        j = index[1]
        k = index[2]

        arr = array[i - 1:j]
        arr.sort()

        answer.append(arr[k - 1])
    return answer
