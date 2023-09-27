n = int(input())
arr = list(map(int, input().split()))
start = 0
budget = int(input())
end = max(arr)

arr.sort()
while start <= end:
    mid = (start + end) // 2

    result = 0
    for i in arr:
        if i < mid:
            result += i
        else:
            result += mid

    if result > budget:
        end = mid - 1
    else:
        start = mid + 1

print(end)