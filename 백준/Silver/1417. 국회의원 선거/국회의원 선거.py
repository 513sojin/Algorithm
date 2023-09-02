n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

if n == 1:
    print(0)
    exit()
else:
    dasom = num[:1][0]
    others = num[1:]

    others.sort(reverse= True)
    count = 0

    while dasom <= max(others):
        others[0] -= 1
        dasom += 1
        count += 1
        others.sort(reverse= True)

    print(count)