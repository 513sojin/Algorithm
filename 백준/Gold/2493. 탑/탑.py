n = int(input())
arr = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n-1,-1,-1):
    while stack and stack[-1][1] < arr[i]:
        answer[stack[-1][0] - 1] = i + 1
        stack.pop()
    stack.append((i+1, arr[i]))

print(*answer)