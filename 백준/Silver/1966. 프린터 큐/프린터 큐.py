t = int(input())
result = []

for _ in range(t):
    priority = []
    max_num = []
    n, m = map(int,input().split())

    num = list(map(int, input().split()))
    for i in range(len(num)):
        priority.append([i, num[i]])
        max_num.append(num[i])

    max_num.sort(reverse=True)
    count = 0
    while True:
        if priority[0][1] != max_num[0]:
            priority.append(priority.pop(0))
        else:
            if priority[0][0] == m:
                result.append(count + 1)
                break
            priority.pop(0)
            max_num.pop(0)
            count += 1

for item in result:
    print(item)