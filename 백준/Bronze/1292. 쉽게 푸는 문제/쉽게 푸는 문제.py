a,b = map(int, input().split())
arr = []
for i in range(1,b+1):
    for _ in range(i):
        arr.append(i)
    if len(arr) >= b:
        break

print(sum(arr[a-1:b]))