import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

most = {}
most_result = 0

for i in arr:
    if i in most:
        most[i] += 1
    else:
        most[i] = 1

most_sorted = sorted(most.items(), key=lambda x: x[1], reverse=True)
most_result = most_sorted[0][0]

if len(most_sorted) > 1 and most_sorted[0][1] == most_sorted[1][1]:
    most_result = most_sorted[1][0]

# 평균
print(round(sum(arr) / len(arr)))
# 중앙값
print(arr[len(arr)//2])
# 최빈값
print(most_result)
# 범위
print(arr[len(arr)-1] - arr[0])