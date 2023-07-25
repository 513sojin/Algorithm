n = int(input())
num = [float(input()) for _ in range(n)]

for i in range(1, n):
    num[i] = max(num[i], num[i] * num[i-1])

print('%0.3f' %max(num))