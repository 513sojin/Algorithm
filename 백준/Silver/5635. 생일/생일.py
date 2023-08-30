n = int(input())
inform = []

for _ in range(n):
    inform.append(list(input().split()))

inform.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(inform[len(inform) -1][0])
print(inform[0][0])