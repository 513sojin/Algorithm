import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [str(input().strip()) for _ in range(n)]
    arr.sort()

    flag = False
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            flag = True
            break

    if flag:
        print("NO")
    else:
        print("YES")