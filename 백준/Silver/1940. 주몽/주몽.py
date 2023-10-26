import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

arr = list(map(int, input().split()))
dict = {}

arr.sort()
for a in arr:
    dict[a] = 1

answer = 0
for key, _ in dict.items():
    if key > m // 2:
        break

    if m-key in dict:
        if key * 2 == m:
            continue
        answer += 1

print(answer)