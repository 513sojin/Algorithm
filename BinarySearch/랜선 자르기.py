
k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)

result = 0 #랜선 길이

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in arr:
        total += i // mid

    if total >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
