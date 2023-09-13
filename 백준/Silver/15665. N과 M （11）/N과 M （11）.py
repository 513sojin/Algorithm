n, m = map(int, input().split())
arr = list(map(int, input().split()))

num = []
arr.sort()

def backtracking():
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    prev = 0
    for i in range(len(arr)):
        if prev != arr[i]:
            num.append(arr[i])
            prev = arr[i]
            backtracking()
            num.pop()

backtracking()