N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
add_count = 0

first_max = max(arr)
arr.pop(arr.index(first_max))
second_max = max(arr)

for i in range(M):
    add_count += 1
    if add_count > K:
        result += second_max
        add_count = 0
    else:
        result += first_max

print(result)
