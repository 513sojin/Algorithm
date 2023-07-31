n, k = map(int, input().split())
arr = []

for i in range(2, n+1):
    arr.append(i)

cnt = 0
erase = []

while arr:
    num = arr[0]
    remain = []

    for i in arr:
        if i % num == 0:
            erase.append(i)
            cnt += 1
        else:
            remain.append(i)
    arr = remain

    if k <= cnt:
        break

print(erase[k-1])