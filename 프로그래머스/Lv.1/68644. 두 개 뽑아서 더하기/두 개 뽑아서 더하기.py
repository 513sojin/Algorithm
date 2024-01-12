answer = []
arr = []

def backtracking(idx, numbers):
    global answer
    global arr

    if len(arr) == 2:
        answer.append(sum(arr))
        return

    for i in range(idx, len(numbers)):
        arr.append(numbers[i])
        backtracking(i+1, numbers)
        arr.pop()


def solution(numbers):
    global answer
    backtracking(0, numbers)

    return sorted(list(set(answer)))
        